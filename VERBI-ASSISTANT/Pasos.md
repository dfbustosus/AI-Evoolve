# Paso a paso
1. `python --version`
2. `python -m venv env`
3. `source/env/bin/activate` (python -m venv env)

Alternativamente puedes usar conda o miniconda

`conda create --name env_assistant python=3.10`

4. `python -m pip list`
5. `python -m pip install -r .\requirements.txt`
6. Crear un archivo `.env`

```bash
OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key
DEEPGRAM_API_KEY=your_deepgram_apikey
LOCAL_MODEL_PATH=path/to/local/model
ELEVENLABS_API_KEY=your_elevenlabs_api_key
CARTESIA_API_KEY=your_cartesia_api_key
```

9. Editar el `config.py`

```python
 class Config:
        # Model selection
        TRANSCRIPTION_MODEL = 'deepgram'  # Options: 'openai', 'groq', 'deepgram', 'fastwhisperapi' 'local'
        RESPONSE_MODEL = 'openai'       # Options: 'openai', 'groq', 'ollama', 'local'
        TTS_MODEL = 'openai'        # Options: 'openai', 'deepgram', 'elevenlabs', 'local', 'melotts'

        # API keys and paths
        OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        GROQ_API_KEY = os.getenv("GROQ_API_KEY")
        DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")
        LOCAL_MODEL_PATH = os.getenv("LOCAL_MODEL_PATH")
```

10. Lanzar el run  `python run_voice_assistant.py`