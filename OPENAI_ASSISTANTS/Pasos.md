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
pip install r-r requirements.txt
```
4. Crear el archivo `Funciones.py` de acuerdo a lo que necesites
5. Crear el archivo `.env` con la credencial de OPENAI e.g
```cmd
OPENAI_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```
6. Utilizar el archivo `Creacion_asistente.py` para crear el asistente con funciones definidas
```cmd
python Creacion_asistente.py
```
7. Utilizar el archivo `Conversacion.py` para adaptar el flujo de la convrsacion
8. Ejecutar la conversacion:
```cmd
python Conversacion.py
```
9. Fin!