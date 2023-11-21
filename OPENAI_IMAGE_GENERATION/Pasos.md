1. Crear un ambiente virtual: python -m venv myenv
```cmd
python -m venv myenv
```
2. Activarlo: 
```cmd
.\myenv\Scripts\Activate.ps1
```
3. Instalar dependencias:
```cmd
pip install -r requirements.txt
```
4. Crear el archivo `Funciones.py` de acuerdo a lo que necesites
5. Crear el archivo `.env` con la credencial de OPENAI e.g
```cmd
OPENAI_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```
6. Correr el archivo `generacion.py` cambiando los prompts y ver los resultados
7. Correr el archivo `retrieve_generacion.py` y obtener tus imagenes

Listo !!!