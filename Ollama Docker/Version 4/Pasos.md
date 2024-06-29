1. Instalar dependencias y levantar imagen
```bash
docker build -t ollama-fastapi .
```
2. Ejecutar contenedor
```bash
docker run -p 11434:11434 -p 8000:8000 ollama-fastapi
```
3. Listo puedes ir a :
```bash
curl http://localhost:8000
```
4. También puedees ejecutar tu modelo
```bash
curl -X POST http://localhost:8000/generate -H "Content-Type: application/json" -d '{"prompt": "Hello, how are you?"}'
```