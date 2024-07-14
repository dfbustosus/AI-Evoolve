#!pip install -q TTS gradio
from TTS.config.shared_configs import BaseDatasetConfig
from TTS.tts.datasets import load_tts_samples
import torch
from TTS.api import TTS
import gradio as gr

print(TTS().models)

device= "cuda" if torch.cuda.is_available() else "cpu"
print(device)

def generate_audio(text="I need help with the task , please"):
  tts= TTS(model_name="tts_models/en/ljspeech/fast_pitch").to(device)
  tts.tts_to_file(text=text, file_path="./output.wav")
  return "./output.wav"
print(generate_audio())

# Multilingual
# Inicializar
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
# Correr TTS
# ❗ Como este es un modelo multi-lingual que usa una voz como referencia se debe setear un target speaker_wav y un lenguaje
wav = tts.tts(text="Hello world!", speaker_wav="../input/test-wav/Test.wav", language="en") # devuelve la curva de amplitud del sonido 
print(wav)
tts.tts_to_file(text="Hello nice to meet you my name is David. What I can do for you today?", speaker_wav="../input/test-wav/Test.wav", 
                language="en", file_path="output_1.wav")

tts.tts_to_file(text="Hola buen dia, es un gusto poder ayudarte hoy. Que necesitas?", speaker_wav="../input/test-wav/Test.wav",
                language="es", file_path="output_2.wav")

tts.tts_to_file(text="Buon giorno, bambino. Como stai oggi? Dove la donna?", speaker_wav="../input/test-wav/Test.wav",
                language="es", file_path="output_3.wav")

tts.tts_to_file(text="Buon giorno, bambino. Como stai oggi? Dove la donna?", speaker_wav="../input/test-wav/Test.wav",
                language="es", file_path="output_3.wav")