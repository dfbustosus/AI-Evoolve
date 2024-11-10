# Docling

🔔 Docling es una nueva libreria de IBM que parsea documentos en PDF, DOCX, y PPTX exportando a Markdown y JSON. Soporta entendimiento avanzado de PDF uy se integra facilmente a LlamaIndex y LangChain.

Paper: https://arxiv.org/html/2408.09869v3

Algunas cosas interesantes
- 🗂️ Maneja diversos formatos (PDF, DOCX, PPTX) a Markdown & JSON.
- 📑 Procesamiento avanzado de PDFs: incluyendo layout, ordenamiento y tablas
- 🧩 Representacion unificada de documentos para mayor facilidad de procesamiento
- 🤖 Integracion con LlamaIndex y LangChain para RAG .
- 🔍 Incluye OCR para PDFs escaneados, algo que es cool
- 💻 Facil de usar con una Python API.

# Pasos para usarlo

1. Crear un ambiente de python `python -m venv myenv`
2. Activar ambiente `myenv/Scripts/activate`
3. Instalar docling con `python -m pip install docling`. La instalacion puede demorar algunos segundos, ten paciencia
4. Ahora podemos usar la herrmienta, para eso mostraremos algunos ejemplos
5. `python -m Ejemplo1.py`
**Nota** La primera vez que lo uses descargara un repo con diveros files que permiten el proceso así que deberas tener paciencia veras algo así:
```
README.md: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 3.49k/3.49k [00:00<00:00, 6.86MB/s]
.gitattributes: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1.71k/1.71k [00:00<00:00, 3.35MB/s]
(…)del_artifacts/tableformer/tm_config.json: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 7.09k/7.09k [00:00<?, ?B/s]
.gitignore: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 5.18k/5.18k [00:00<00:00, 8.04MB/s]
config.json: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 41.0/41.0 [00:00<00:00, 371kB/s]
model.pt: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 202M/202M [00:06<00:00, 31.9MB/s]
otslp_all_fast.check: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 146M/146M [00:07<00:00, 20.1MB/s]
otslp_all_standard_094_clean.check: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 213M/213M [00:12<00:00, 17.2MB/s]
Fetching 9 files: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 9/9 [00:13<00:00,  1.52s/it]
otslp_all_standard_094_clean.check:  99%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▉  | 210M/213M [00:12<00:00, 42.5MB/s]
Downloading detection model, please wait. This may take several minutes depending upon your network connection.
Progress: |██████████████████████████████████████████████████| 100.0% 
```

Tambien de puede usar desde la terminal

```bash
docling https://arxiv.org/pdf/2206.01062
```

Otros ejemplos 

6. `python  Ejemplo2.py`
7. `python  Ejemplo3.py`
8. `python  Ejemplo4.py`