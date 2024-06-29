# CPU

1. Descargar imagen
```bash
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```
2. Descargar modelo 
```bash
docker exec -it ollama ollama run llama2
docker exec -it ollama ollama run phi
```
3. 

# GPU
1. Instalar dependencias de CUDA: [aqui](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#installation)
```bash
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list

sudo apt-get update
sudo apt-get install -y nvidia-container-toolkit
```
2. Descargar imagen
```bash
docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

3. Instalar modelo
```bash
docker exec -it ollama ollama run phi
```

4. Puedes usar toda la documentación de la API de ahora en adelante: https://github.com/ollama/ollama/blob/main/docs/api.md