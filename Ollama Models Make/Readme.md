
# Fase 1: Importando formato gguf
1. Download the model [ejemplo](https://huggingface.co/TheBloke/CapybaraHermes-2.5-Mistral-7B-GGUF)

Te recomiendo el formato `Q4_K_M` [Model example](https://huggingface.co/TheBloke/CapybaraHermes-2.5-Mistral-7B-GGUF/blob/main/capybarahermes-2.5-mistral-7b.Q4_K_M.gguf). El modelo base es el siguiente [Model card](https://huggingface.co/argilla/CapybaraHermes-2.5-Mistral-7B)

2. Pon el modelo en la ruta donde estas tarabajando
3. Ahora deberas crear la estructura para la creación, en tu ruta crea un archivo sin formato `Modelfile`, te recomiendo que lo hagas con VS Code o un editor de código.

```bash
FROM ./capybarahermes-2.5-mistral-7b.Q4_K_M.gguf
PARAMETER stop "<|im_start|>"
PARAMETER stop "<|im_end|>"
TEMPLATE """
<|im_start|>system
{{ .System }}<|im_end|>
<|im_start|>user
{{ .Prompt }}<|im_end|>
<|im_start|>assistant
"""
```
Toda la documentación de como generar los prompt templates los podrás ver [aqui](https://github.com/ollama/ollama/blob/main/docs/import.md)

4. Crear el modelo con las especificaciones
```bash
ollama create david-hermes -f Modelfile
```
5. Veras tus modelos con
```bash
ollama list
```
Ya debería ver tu nuevo modelo

6. Ahora podrás hacer el run del modelo con
```bash
ollama run david-hermes
```
7. Si quieres borrar el modelo solo debes poner:
```bash
ollama rm david-hermes
```

Perfecto ya puedes descargar cualquier modelo para poder experimentar

# Fase 2: Convirtiendo el modelo a formato gguf por ti mismo

1. Ir al modelo de interés [Model](https://huggingface.co/argilla/CapybaraHermes-2.5-Mistral-7B)
2. Click en `File and versions`
3. Click en los tres puntos > Clone repository
4. Deberas tener instalado lfs para procesar grandes volumenes de data
5. Si no lo tienes lo puedes instalar con 
```bash
git lfs install
```
6. Clonar el repo:
```bash
git clone https://huggingface.co/argilla/CapybaraHermes-2.5-Mistral-7B
```
Esto puede demorar cerca de 5-10min dependiendo de tu conexión
7. Deberás tener instalado docker y abrirlo
8. Crear el formato del modelo
```bash
docker run --rm -v .:model ollama/quantize -q q4_K_M /model 
```
Esto se demorara algunos minutos dependiendo de tu capacidad de computo
9. Ahora debería poder dos nuevos archivos
```bash
ls
```

Uno `f16.bin` y otro el `q4_K_M.bin`. Este ultimo archivo `q4_K_M.bin` es el que podrás usar en formato ``gguf` para crear el modelo con ollama