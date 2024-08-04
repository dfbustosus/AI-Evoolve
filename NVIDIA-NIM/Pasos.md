# NVIDIA NIM

Es un microservice para poder deployar y testear modelos LLM

Cuanta con modelos relacionados con imagen, video, 3D models, ASR, TTS, VLM entre otros

Ademas de que cuenta con una infraestructura y recursos adecuados para soportar todo los resources y sobre todo incrementar velocidad (tokens/sec).

![NVIDIA NIM](NVIDIA_NIM.jpeg)

# Pasos 

1. Ir a esta web: https://www.nvidia.com/en-us/ai/
2. Dar click en `Try now`. Si es la primer a vez que usas deberás poner to correo y luego dar click en Next

Luego te enviaran un mensaje de verificación al correo el cual deberás revisar para autenticarte

3. Luego te pediran si quieres generar algún mecanismo de seguridad adicional (Authenticator App Code, Hardware Security Device), esto es opcional, pero recomendable.

4. Luego te pediran un `Account Name` y ahí finalmente podrás dar click en `Create NVIDIA Cloud Account` y posteriormente ya podrás logearte sin problema.

**Nota:** Te ofrecen cerca de 100 creditos free para que puedas probar este service

También debes tener presente que puedes crear todo desde cero con tu propia infraestructura usando docker containers. Pero para esto ten en cuenta que debes contar ocn sufcientes recursos.

5. Ahora ya logeados debemos seleccionar cualquier modelo de interés (e.g `llama-3.1-405b-instruct`), esto abrirar una interfaz para que puedas interactuar con el modelo y también código base para probar en `Python`, `Node` o `Shell`

6. Antes de poder usar el código deberás setear tu API KEY, para eso puedas dar click en Get API Key, luego copia tu key y crea un archivo `.env` 

```bash
NVIDIA_API_KEY=nvapi-XXXXXXXXXXXXXXXX-XXXXXXXXX
```

7. Copiamos el código fuente y lo podemos testear

```bash
python Llama-3.1-405b-instruct.py
```

8. Ahora puedes ejecutar cualquier modelo con la funcionalidad que desees


