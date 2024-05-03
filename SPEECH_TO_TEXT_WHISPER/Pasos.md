# Usando Whisper de forma Local
## Instalar python
1. Descargar python 3.9.9 en : `https://www.python.org/downloads/release/python-399/`
2. Instalar en una ruta diferente si tienes mas de una version de python e.g `C:/Python399`
3. Agregar la ruta de python a variables de entorno
```
C:\Python399\Scripts
C:\Python399
```
4. Verificar que tengas la version 3.9.9 `python --version`
## Instalar Nvidia Cuda
5. Instalar Nvidia Cuda: `https://developer.nvidia.com/cuda-11-6-0-download-archive`
## Instalar dependencias de Pytorch
6. Instalar pytorch en la terminal: `https://pytorch.org/get-started/locally/` 
`python -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121`
## Instalar ffmpeg
7. Descargar ffmepg: `https://ffmpeg.org/download.html#build-windows`
8. Seleccionar Windows > Windows builds by BtnN . Elegir : `ffmpeg-master-latest-win64-gpl.zip` y descargar (pesa alrededor de 130mb)
9. Descomprimir los archivos:
```
ffmpeg
ffplay
ffprobe
```
10. Crear un nuevo path en `C:` por ejemplo: `C:/path` y poner los archivos de `.\Downloads\ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin` dentro
11. Agregar ffmepg a variables de entorno: `C:\path`
12. Verificar que se tenga activo en el terminal ffmpeg, debera salir un mensaje con la version: `ffmepg`
## Instalar Whisper y dependencias adicionales
13. Instalar dependencias:
```
python -m pip install setuptools-rust
python -m pip install git+https://github.com/openai/whisper.git
```
## Usar Whisper
14. Ahora verificamos que tengamos instalado whisper con: `whisper`
15. Puedes obtener ayuda sobre whisper con: `whisper -h`
16. Ahora podemos ir al proyecto de whisper: `https://github.com/openai/whisper`. Aqui podras encontrar todos los modelos disponibles:
- tiny
- base
- small
- medium
- large
17. Ahora puedes usar cualquier mp3 y convertirlo con whisper
18. Comando para transcripcion es: `whisper '.\LLAMA 2.mp3'`
19. Puedes abrir tu Task manager para ver lo que ocurre con tus recursos de computo
20. Si deseas usar un modelo en especifico puedes usar: `whisper '.\LLAMA 2.mp3' --model tiny`
21. Cuando el proceso termina debera sobservar tres archivos principales (sin embargo puede que aparezcan más!) en tu carpeta de destino
- `.srt` el dialogo con los tiempos y parrafos
- `.txt` el texto transcrito
- `.vtt` es un archivo mas completo de tiempos y parrafos
22. Si deseas transcribir de un idioma al ingles puedes usar lo siguiente:
`whisper '.\LLAMA 2.mp3' --language Spanish --task translate`
23. Otros ejemplo
```bash
whisper '.\audi.wav' --model tiny --task transcribe
whisper '.\audi.wav' --model tiny --task transcribe --temperature 0 --initial_prompt 'Audi audi'

whisper '.\audi.wav' --model base --task transcribe
whisper '.\audi.wav' --model base --task transcribe --temperature 0 --initial_prompt 'Audi audi'

whisper '.\audi.wav' --model small --task transcribe
whisper '.\audi.wav' --model small --task transcribe --temperature 0 --initial_prompt 'Audi audi'

whisper '.\audi.wav' --model medium --task transcribe
whisper '.\audi.wav' --model medium --task transcribe --temperature 0 --initial_prompt 'Audi audi'

whisper '.\audi.wav' --model large --task transcribe
whisper '.\audi.wav' --model large --task transcribe --temperature 0 --initial_prompt 'Audi audi'
```
23. Fin!
