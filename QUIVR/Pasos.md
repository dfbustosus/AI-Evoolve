# Pasos para usar Quivr (nube)
1. Ir a la pagina oficial : https://www.quivr.app/
2. Crear un cuenta con el boton de Sign up
3. La documentación general está disponible en : https://docs.quivr.app/home/intro
4. Para crear un nuevo Brain ir a >> Add Brain
5. Seleccionar el tipo de datos que va a manejar (default Documents)
6. Elegir los parametros (Brain name y Descripcion general) también si el scope es público o privado
7. Definir los Resources (puedes subir un archivo pdf o incluso una url con un website)
8. Dar Click en Create
9. Listo tendras un nuevo Brain creado
10. Ahora podrás ir a Home y en la barra de busqueda primero deberas referenciar con que Brain quieres hablar con la siguiente notacion `@Brain_name`
11. Posteriormente en Search podrás hacer cualquier pregunta referente al texto
Eso es todo para el setup en la nube

**Nota:** Para el caso de los planes Free tier tienes las siguientes limitaciones (maximo 3 Brains, 100 preguntas gratis, hasta 30Mb de storage)


# De forma local xD
1. Primero instalar superbase: https://supabase.com/docs/guides/cli/getting-started?platform=windows
Para el caso de Windows
```bash
scoop bucket add supabase https://github.com/supabase/scoop-bucket.git
scoop install supabase
scoop update supabase
```
2. Verificar que este instalado
```bash
scoop list
```
3. Ver en que directorio esta superbase
```bash
(Get-Command supabase).Source
```
4. Verificar version
```bash
C:\Users\david\scoop\shims\supabase.exe -v
```
5. Clonar el repo
```bash
git clone https://github.com/StanGirard/Quivr.git
```
6. Ir al proyecto
```bash
cd Quivr
```
7. Copiar el env example en e, archivo real a usar
```bash
cp .env.example .env
```
8. Modificar `OPENAI_API_KEY` en el nuevo `.env` file con tu nueva API KEY
9. Tener instalado Docker y abrirlo
10. Verificar que Docker este con
```bash
docker -v
```
11. Inicializar el proyecto
```bash
C:\Users\david\scoop\shims\supabase.exe start
```
12. Deberan comenzar a descargarse las layers del proyecto (esto tomará algunos segundos)
13. Levantar la imgen del proyecto con:
```bash
docker compose pull
docker compose up
```
**Nota:** No es tan rapido tendras que tener paciencia
14. Si estás en Mac deberas hacer estos pasos adicionales: Docker Desktop > Settings > General asegurarse que "file sharing implementation" este en VirtioFS.
15. Ahora puedes logearte en la app en:
```bash
localhost:3000
```
En las credenciales poner
```markdown
user: admin@quivr.app
pwd: admin
```
Dar en `Login`
16. Ya puedes hablar con quivr
17. Si quieres ver los logs de la app puedes ir a 
```bash
localhost:8000
```
18. En credenciales 
```bash
user: admin
pwd: admin
```
19. Tambien se puede jugar con Ollama si no te gusta OpenAI pero no esta disponible aún para Windows así que mejor lo dejamos apra otro video.

