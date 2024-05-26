
1. Ir a la [URL](https://github.com/open-webui/open-webui)
2. Tener instalado Docker, puedes verificarlo abriendo el terminal y poniendo
```bash
docker --version
```
3. Si no tienes instalado Docker puedes instalarlo siguiendo este tutorial [Instalando Docker](https://www.youtube.com/watch?v=-qNPeA4y90E&list=PLcB6GPlW-yDqJ0WlPGJS1rX-WpVpu6nox&index=24)

Tambien tienes una intrducción acerca de como funciona Docker [aqui](https://www.youtube.com/watch?v=hJzMsN_Lz2g&list=PLcB6GPlW-yDqJ0WlPGJS1rX-WpVpu6nox&index=23)

4. Es importante que también tengas instalado `Ollama`, sino lo tienes puedes instaalrlo facilmente [aqui](https://ollama.com/)

5.  Luego de tener `Docker` y `Ollama` es muy sencillo generar la instalación del entorno UI
Si tienes ollama en una maquina local puedes utilizar el siguiente comando
```bash
docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```
**Explicación**
- `docker run`: Es el comando base para ejecutar un contenedor de Docker.
- `-d`: Significa "detached mode", lo que hace que el contenedor se ejecute en segundo plano y no bloquee la terminal.
- `-p 3000:8080`: Mapea el puerto 3000 del host al puerto 8080 del contenedor. Esto significa que cualquier solicitud a localhost:3000 en el host se redirigirá al puerto 8080 del contenedor.
- `--add-host=host.docker.internal:host-gateway`: Añade una entrada en el archivo /etc/hosts del contenedor, haciendo que host.docker.internal apunte a la dirección IP del host-gateway. Esto facilita que el contenedor se comunique con el host.
- `-v open-webui:/app/backend/data`: Monta un volumen. En este caso, open-webui es el nombre del volumen en el host, y /app/backend/data es el punto de montaje dentro del contenedor. Esto permite persistir datos entre reinicios del contenedor y compartir datos entre el host y el contenedor.
- `--name open-webui`: Asigna el nombre open-webui al contenedor. Esto facilita la gestión del contenedor, permitiendo usar su nombre en lugar de su ID para las operaciones.
- `--restart always`: Configura el contenedor para que se reinicie automáticamente en caso de fallar o cuando el Docker daemon se reinicia. Esto es útil para asegurar que el servicio dentro del contenedor siempre esté disponible.
- `ghcr.io/open-webui/open-webui:main`: Especifica la imagen de Docker que se utilizará para crear el contenedor. En este caso, la imagen está alojada en GitHub Container Registry (ghcr.io), en el repositorio open-webui/open-webui y la etiqueta main.

Si ollama esta corriendo en otro terminal el comando será el siguiente

```bash
docker run -d -p 3000:8080 -e OLLAMA_BASE_URL=https://example.com -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

Finalmente en caso de que quieras utilizar recursos de GPU puedes usar este comando:
```bash
docker run -d -p 3000:8080 --gpus all --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:cuda
```

5. Luego de que tu imagen este lista podrás ir a la siguiente URL
```bash
http://localhost:3000/auth/
```
6. Luego deberás crear una cuenta dando click en `Sign up`. Ten en cuenta que esto es una cuenta local así que si remueves el container y lo vuelves a lanzar tendrás que volver a hacerlo de nuevo
7. Posteriormente podrás entrar con esa cuenta

!!LISTO ya puedes usar ollama junto con todos los modelos en la interfaz gráfica!!
