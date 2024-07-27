from fastapi import FastAPI, Form, HTTPException, Request, Response
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import torch
import torchaudio
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import Xtts
import warnings
import os
import io
import time

warnings.filterwarnings("ignore")

app = FastAPI()

XTTS_MODEL = None
SAMPLE_RATE = 24000  # Assuming the model outputs at 24kHz

class TTSRequest(BaseModel):
    lang: str
    tts_text: str
    temperature: float = 0.75
    length_penalty: float = 1.0
    repetition_penalty: float = 5.0
    top_k: int = 50
    top_p: float = 0.85
    sentence_split: bool = True
    use_config: bool = False

def clear_gpu_cache():
    if torch.cuda.is_available():
        torch.cuda.empty_cache()

def load_model(xtts_checkpoint: str, xtts_config: str, xtts_vocab: str, xtts_speaker: str):
    global XTTS_MODEL
    clear_gpu_cache()
    config = XttsConfig()
    config.load_json(xtts_config)
    XTTS_MODEL = Xtts.init_from_config(config)
    XTTS_MODEL.load_checkpoint(config, checkpoint_path=xtts_checkpoint, vocab_path=xtts_vocab, speaker_file_path=xtts_speaker, use_deepspeed=False)
    if torch.cuda.is_available():
        XTTS_MODEL.cuda()
    print("Model Loaded!")

@app.on_event("startup")
async def startup_event():
    xtts_checkpoint = "./model/model.pth"
    xtts_config = "./model/config.json"
    xtts_vocab = "./model/vocab.json"
    xtts_speaker = "./model/speakers_xtts.pth"
    load_model(xtts_checkpoint, xtts_config, xtts_vocab, xtts_speaker)

def generate_audio(tts_request: TTSRequest):
    if XTTS_MODEL is None:
        raise HTTPException(status_code=400, detail="Model not loaded")

    reference_audio = "./reference_22050.wav"

    gpt_cond_latent, speaker_embedding = XTTS_MODEL.get_conditioning_latents(
        audio_path=reference_audio,
        gpt_cond_len=XTTS_MODEL.config.gpt_cond_len,
        max_ref_length=XTTS_MODEL.config.max_ref_len,
        sound_norm_refs=XTTS_MODEL.config.sound_norm_refs
    )

    if tts_request.use_config:
        out = XTTS_MODEL.inference(
            text=tts_request.tts_text,
            language=tts_request.lang,
            gpt_cond_latent=gpt_cond_latent,
            speaker_embedding=speaker_embedding,
            temperature=XTTS_MODEL.config.temperature,
            length_penalty=XTTS_MODEL.config.length_penalty,
            repetition_penalty=XTTS_MODEL.config.repetition_penalty,
            top_k=XTTS_MODEL.config.top_k,
            top_p=XTTS_MODEL.config.top_p,
            enable_text_splitting=True
        )
    else:
        out = XTTS_MODEL.inference(
            text=tts_request.tts_text,
            language=tts_request.lang,
            gpt_cond_latent=gpt_cond_latent,
            speaker_embedding=speaker_embedding,
            temperature=tts_request.temperature,
            length_penalty=tts_request.length_penalty,
            repetition_penalty=float(tts_request.repetition_penalty),
            top_k=tts_request.top_k,
            top_p=tts_request.top_p,
            enable_text_splitting=tts_request.sentence_split
        )

    return out["wav"].cpu().numpy() if torch.is_tensor(out["wav"]) else out["wav"]

@app.post("/tts_stream")
async def tts_stream(tts_request: TTSRequest):
    audio_numpy = generate_audio(tts_request)
    
    def iterfile():
        with io.BytesIO() as buffer:
            # Convert numpy array to torch tensor
            audio_tensor = torch.from_numpy(audio_numpy).unsqueeze(0)
            torchaudio.save(buffer, audio_tensor, SAMPLE_RATE, format="wav")
            buffer.seek(0)
            yield from buffer

    return StreamingResponse(iterfile(), media_type="audio/wav")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
