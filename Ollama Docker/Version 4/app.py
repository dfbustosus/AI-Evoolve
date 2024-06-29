from fastapi import FastAPI, HTTPException
import requests
import json
import time

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API ollama"}

@app.post("/generate")
async def generate_text(prompt: str):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "phi",
        "prompt": prompt,
        "stream": False,
        "options": {
            "num_keep": 5,
            "seed": 42,
            "num_predict": 100,
            "top_k": 20,
            "top_p": 0.9,
            "tfs_z": 0.5,
            "typical_p": 0.7,
            "repeat_last_n": 33,
            "temperature": 0.8,
            "repeat_penalty": 1.2,
            "presence_penalty": 1.5,
            "frequency_penalty": 1.0,
            "mirostat": 1,
            "mirostat_tau": 0.8,
            "mirostat_eta": 0.6,
            "penalize_newline": True,
            "numa": False,
            "num_ctx": 1024,
            "num_batch": 2,
            "num_gpu": 1,
            "main_gpu": 0,
            "low_vram": False,
            "f16_kv": True,
            "vocab_only": False,
            "use_mmap": True,
            "use_mlock": False,
            "num_thread": 8
        }
    }
    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error communicating with Ollama: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)