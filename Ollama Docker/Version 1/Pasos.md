# Docker + Ollama V1
1. Debes tener instalado docker
2. Creamos la imagen 
```bash
docker build . -t david-ollama
```
3. Podras ver las imagenes
```bash
docker images
```
4. Ahora levantamos los dos servicios
```bash
docker-compose up
```
5. Ahora podras hacer una simple petición a 
```bash
curl http://localhost:11434/
```
Y deberías obtener esto:
```bash
StatusCode        : 200
StatusDescription : OK
Content           : Ollama is running
RawContent        : HTTP/1.1 200 OK
                    Content-Length: 17
                    Content-Type: text/plain; charset=utf-8
                    Date: Sat, 29 Jun 2024 15:27:22 GMT

                    Ollama is running
Forms             : {}
Headers           : {[Content-Length, 17], [Content-Type, text/plain; charset=utf-8], [Date, Sat, 29 Jun 2024 15:27:22 GMT]}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 17
```
6. Puedes ver los containers con 
```bash
docker ps
```
7. Descargamos el modelo de interes
```bash
docker exec -it ollamadocker-ollama-container-1 ollama run phi
```
Luego puedes escribir `/bye` para salir
Veras que el modelo está en la carpeta `data/`
8. Ahora podras hacer peticiones a traves de streamlit en `http://localhost:8501/``
9. Si quieres terminar el servicio solo debes usar `CTRL+C` y luego
```bash
docker-compose down
```

