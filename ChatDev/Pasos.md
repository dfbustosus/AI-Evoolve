# Crear software con Chat Dev
1. Ir a tu ruta de trabajo
2. Clonar el repo
```bash
git clone https://github.com/OpenBMB/ChatDev.git
```
3. ```bash
cd ChatDev
```
4. Setear tu api key como variable de entorno
```bash
$env:OPENAI_API_KEY="sk-XXXXXXXXXXXXXXXXXXXXXXX"
```
5. Crear un ambiente ailsado
```bash
python -m venv myenv
```
6. Activarlo
```bash
\myenv\Scripts\activate
```
7. Instalar dependencias
```bash
python -m pip install -r .\requirements.txt
```
8. Ìniciar el proceso de desarrollo
```bash
python run.py --task "a password app where users can create password, change it and delete it" --name "password"
```
9. Esperar a que termine, al final dentro de la carpeta `Warehouse` podras visualizar tu proyecto 
10. Ahora podremos visualizar como fue el flujo de conversaciones con:
````bash
python .\visualizer\app.py
```
