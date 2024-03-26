# Pasos comparacion CLAUDE vs OPENAI Functions

1. Crear ambiente (puedes tener python 3.8 en adelante)
```bash
python -m venv myenv
```
2. Activar ambiente
```bash
.\myenv\Scripts\Activate
```
3. Instalar dependencias
```bash
python -m pip install anthropic openai python-dotenv termcolor tenacity
```
4. Crear un archivo `.env` con las API keys de ambos servicios
```python
OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
CLAUDE_API_KEY=sk-ant-XXXXXXXXXXXXXXXXXXXXXXXXX
```
5. Ejecutar los scripts sin problema
```bash
python test_1_stock.py
python test_2_temp.py
```
Eso es todo!!