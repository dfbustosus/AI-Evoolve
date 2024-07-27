# XTTS model base

0. Tener instalado git lfs: `git lfs install`
1. Clonar el repo: `git clone git@github.com:dfbustosus/AI-Evoolve.git`
2. Ir a la carpeta de interes: `cd .\XTTS_API\`
3. Tener instalado python 3.11 (Idealmente `3.11.0`)
4. Crear ambiente virtual `python -m venv venv`
5. Activar entorno virtual `.\venv\Scripts\activate`
6. Levantar la API: `uvicorn app:app --host 0.0.0.0 --port 8000 --reload`
7. Si estás en Windows te recomiendo instalar `cygwin`, puedes seguir estos pasos si no lo tienes instalado: https://www.cygwin.com/install.html
7. Probar el funcionamiento abriendo `cygwin`

8. **Ingles**

```bash
time curl -X 'POST'   'http://localhost:8000/tts_stream'   -H 'accept: application/json'   -H 'Content-Type: application/json'   -d '{
  "lang": "en",
  "tts_text": "Artificial intelligence is revolutionizing the world of technology.",
  "temperature": 0.75,
  "length_penalty": 1,
  "repetition_penalty": 5,
  "top_k": 50,
  "top_p": 0.85,
  "sentence_split": true,
  "use_config": false
}' --output output_1.wav
```

```bash
time curl -X 'POST'   'http://localhost:8000/tts_stream'   -H 'accept: application/json'   -H 'Content-Type: application/json'   -d '{
  "lang": "en",
  "tts_text": "A good coffee in the morning can make your day much better",
  "temperature": 0.75,
  "length_penalty": 1,
  "repetition_penalty": 5,
  "top_k": 50,
  "top_p": 0.85,
  "sentence_split": true,
  "use_config": false
}' --output output_2.wav
```
9. **Español**

```bash
time curl -X 'POST'   'http://localhost:8000/tts_stream'   -H 'accept: application/json'   -H 'Content-Type: application/json'   -d '{
  "lang": "es",
  "tts_text": "La música es el lenguaje universal que une a las personas de todas las culturas",
  "temperature": 0.75,
  "length_penalty": 1,
  "repetition_penalty": 5,
  "top_k": 50,
  "top_p": 0.85,
  "sentence_split": true,
  "use_config": false
}' --output output_3.wav
```

```bash
time curl -X 'POST'   'http://localhost:8000/tts_stream'   -H 'accept: application/json'   -H 'Content-Type: application/json'   -d '{
  "lang": "es",
  "tts_text": "Las estrellas brillan más intensamente en las noches despejadas del invierno.",
  "temperature": 0.75,
  "length_penalty": 1,
  "repetition_penalty": 5,
  "top_k": 50,
  "top_p": 0.85,
  "sentence_split": true,
  "use_config": false
}' --output output_4.wav
```
10. **Frances**

```bash
time curl -X 'POST'   'http://localhost:8000/tts_stream'   -H 'accept: application/json'   -H 'Content-Type: application/json'   -d '{
  "lang": "fr",
  "tts_text": "La musique est le langage universel qui relie les gens de toutes les cultures.",
  "temperature": 0.75,
  "length_penalty": 1,
  "repetition_penalty": 5,
  "top_k": 50,
  "top_p": 0.85,
  "sentence_split": true,
  "use_config": false
}' --output output_5.wav
```

```bash
time curl -X 'POST'   'http://localhost:8000/tts_stream'   -H 'accept: application/json'   -H 'Content-Type: application/json'   -d '{
  "lang": "fr",
  "tts_text": "Les étoiles brillent plus fort lors des nuits claires dhiver.",
  "temperature": 0.75,
  "length_penalty": 1,
  "repetition_penalty": 5,
  "top_k": 50,
  "top_p": 0.85,
  "sentence_split": true,
  "use_config": false
}' --output output_6.wav
```

11. **Portugues**
```bash
time curl -X 'POST'   'http://localhost:8000/tts_stream'   -H 'accept: application/json'   -H 'Content-Type: application/json'   -d '{
  "lang": "pt",
  "tts_text": "A beleza da arte está na sua capacidade de emocionar.",
  "temperature": 0.75,
  "length_penalty": 1,
  "repetition_penalty": 5,
  "top_k": 50,
  "top_p": 0.85,
  "sentence_split": true,
  "use_config": false
}' --output output_7.wav
```

```bash
time curl -X 'POST'   'http://localhost:8000/tts_stream'   -H 'accept: application/json'   -H 'Content-Type: application/json'   -d '{
  "lang": "pt",
  "tts_text": "Viajar amplia nossos horizontes e nos enriquece como pessoas",
  "temperature": 0.75,
  "length_penalty": 1,
  "repetition_penalty": 5,
  "top_k": 50,
  "top_p": 0.85,
  "sentence_split": true,
  "use_config": false
}' --output output_8.wav
```

12. **Italiano**

```bash
time curl -X 'POST'   'http://localhost:8000/tts_stream'   -H 'accept: application/json'   -H 'Content-Type: application/json'   -d '{
  "lang": "it",
  "tts_text": "La bellezza dell arte risiede nella sua capacità di emozionare",
  "temperature": 0.75,
  "length_penalty": 1,
  "repetition_penalty": 5,
  "top_k": 50,
  "top_p": 0.85,
  "sentence_split": true,
  "use_config": false
}' --output output_9.wav
```

```bash
time curl -X 'POST'   'http://localhost:8000/tts_stream'   -H 'accept: application/json'   -H 'Content-Type: application/json'   -d '{
  "lang": "it",
  "tts_text": "Viaggiare amplia i nostri orizzonti e ci arricchisce come persone",
  "temperature": 0.75,
  "length_penalty": 1,
  "repetition_penalty": 5,
  "top_k": 50,
  "top_p": 0.85,
  "sentence_split": true,
  "use_config": false
}' --output output_10.wav
```
Perfecto terminamos!