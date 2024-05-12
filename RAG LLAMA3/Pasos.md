# Fase 1: Interacción con Ollama
1. Tener instalado ollama previamente [Ollama](https://ollama.com/)
2. Traer el modelo llama3
```bash
ollama pull llama3
```
3. Puedes verificar que tangas el modelo previamente
```bash
ollama list
```
4. Puedes ponerlo como server (opcional)
```bash
ollama serve
```
5. Y lo puedes correr con
```bash
ollama run llama3
```
6. Probamos que tengamos al modelo funconando
```bash
curl http://localhost:11434/api/chat -d '{
    "model": "llama3",
    "messages": [
        { "role": "system", "content": "You are a service agent to schedule medical appointments" },
        { "role": "user", "content": "I need to schedule an appointment please" }
    ],
    "stream":false
  }'
```
# Fase 2: Creando estructura de app
7. Creamos un ambiente para trabajar aislado
```bash
python -m venv myenv
```
8. Activamos dependencias
```bash
.\myenv\Scripts\activate
```
8. Instalamos las dependencias de interes
```bash
python -m pip install -q langchain_community flask langchain-text-splitters fastembed pdfplumber chromadb langchain
```

9. Creamos nuestro archivo `app.py` con el bosquejo de la app
```python
from flask import Flask, request

app= Flask(__name__)

# Iniciar la app
@app.route("/model", methods=["POST"])
def modelPost():
    print("POST /model usado")
    json_content = request.json
    query= json_content.get("query")
    print(f"query: {query}")
    response_answer= "Respuesta de prueba"
    return response_answer

def start_app():
    app.run(host="0.0.0.0", port=8080, debug=True)

if __name__ =="__main__":
    start_app()
```
Puedes abrir Postman y colocar esta URL en un metodo POST `http://localhost:8080/model` y colocando este json `{"query":"Hola como estas"}` deberías obtener esta respuesta `Respuesta de prueba`

# Fase 3: Interactuando con el LLM

10. Ahora podemos hacer que el modelo responda a nuestras preguntas
```python
from flask import Flask, request
from langchain_community.llms import Ollama

app= Flask(__name__)

llm= Ollama(model="llama3")

# Iniciar la app
@app.route("/model", methods=["POST"])
def modelPost():
    print("POST /model usado")
    json_content = request.json
    query= json_content.get("query")
    print(f"query: {query}")
    response = llm.invoke(query)
    response_answer= {"respuesta": response}
    return response_answer

def start_app():
    app.run(host="0.0.0.0", port=8080, debug=True)

if __name__ =="__main__":
    start_app()
```

11. Puedes voolver a colocar cualquier pregunta y deberas ver la respuesta

# Fase 4: Integrando capacidad de subir pdf

12. Creamos un dir para subir nuestro archivo `pdf` por ejemplo
13. Creamos el nuevo metodo en la app para procesar un pdf
```python
@app.route("/pdf", methods=["POST"])
def pdfPost():
    file = request.files["file"]
    file_name= file.filename
    save_file= "pdf/"+ file_name
    file.save(save_file)
    print(f"filename: {file_name}")
    response= {"status":"Subida correcta","filename":file_name}
    return response
```
14. Ahora puedes ir a Postman y ver que funciona el metodo subiendo un archivo pdf cualquier (trata de que sea corto) en esta URL: `http://localhost:8080/pdf` dentro del Body deberas elegir `Key: file` y subir tu archivo, luego si ejecutas el metódo saldrá algo como esto. Bien tu archivo ya esta en el directorio de interes ``pdf`
```json
{
    "filename": "Paper Attention is All you Need.pdf",
    "status": "Subida correcta"
}
```

# Fase 5: Agregar embeddings

15. Debemos agregar algunas dependencias y las herramientas que vamos a usar para construir los embeddings:

```python
from flask import Flask, request
from langchain_community.llms import Ollama
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_community.document_loaders import PDFPlumberLoader

app= Flask(__name__)

llm= Ollama(model="llama3")
embedding = FastEmbedEmbeddings()
text_splitter= RecursiveCharacterTextSplitter(
    chunk_size= 1024, chunk_overlap=80, 
    length_function= len, is_separator_regex=False
)
```
17. Deberemos crear un nuevo directorio llamado `db` para almacenar la data de los embeddings
```python
app= Flask(__name__)

folder_path ="db"

llm= Ollama(model="llama3")
embedding = FastEmbedEmbeddings()
text_splitter= RecursiveCharacterTextSplitter(
    chunk_size= 1024, chunk_overlap=80, 
    length_function= len, is_separator_regex=False
)
```

18. Luego debemos adaptar el loader en el metodo pdf para que además de cargar el archivo podamos calculart los embeddings una vez se suba la data del pdf
```python
@app.route("/pdf", methods=["POST"])
def pdfPost():
    file = request.files["file"]
    file_name= file.filename
    save_file= "pdf/"+ file_name
    file.save(save_file)
    print(f"filename: {file_name}")

    loader= PDFPlumberLoader(save_file) # Cargar archivo subido
    docs = loader.load_and_split()  # Split docs
    print(f"docs len= {len(docs)}") 
    chunks = text_splitter.split_documents(docs) # Chunks de texto
    print(f"Chunks len= {len(chunks)}")
    # Base vectorial
    vector_store= Chroma.from_documents(
        documents= chunks,
        embedding= embedding,
        persist_directory= folder_path)
    vector_store.persist()

    response= {"status":"Subida correcta",
               "filename":file_name,
               "doc_len": len(docs),
               "chunks": len(chunks)}
    return response
```

19. Ahora podras volver a intentar mandar la información al metodo POST `pdf` (`http://localhost:8080/pdf`) y podras observar el resultado nuevo
```json
{
    "chunks": 34,
    "doc_len": 11,
    "filename": "Paper Attention is All you Need.pdf",
    "status": "Subida correcta"
}
```

# Fase 6: Agregar model response
20. Bien ahora podemos importar otras dependencias que nos hacen falta y definir un custom prompt
```python
from flask import Flask, request
from langchain_community.llms import Ollama
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_community.document_loaders import PDFPlumberLoader
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain.prompts import PromptTemplate

raw_prompt= PromptTemplate.from_template("""
    <s>[INST] You are a technical assistant to provide answers based on the provided information. If you dint know the answer with the provided information be honest and answer 'Sorry I do not know the answer for this question'. [/INST] </s>
    [INST] {input}
            Context: {context}
            Answer: 
    [/INST]
```

21. Posteriormente definimos un metodo POST para poder responder nuestras preguntas `ask_pdf`

```python
@app.route("/ask_pdf", methods=["POST"])
def askPDFPost():
    print("POST /ask_pdf usado")
    json_content = request.json
    query= json_content.get("query")
    print(f"query: {query}")
    
    print("Loading vector store")
    vector_store= Chroma(
        persist_directory=folder_path, embedding_function=embedding
    )
    # Creando el chain
    retriever = vector_store.as_retriever(
        search_type= "similarity_score_threshold",
        search_kwargs={
            "k":3,
            "score_threshold":0.1 # Limite de busqueda
        }
    )

    document_chain= create_stuff_documents_chain(
        llm, raw_prompt
    )
    chain= create_retrieval_chain(retriever, document_chain)
    result= chain.invoke({"input":query})
    
    response_answer= {"respuesta": result['answer']}
    return response_answer
```
22. Perfecto ahora podemos crear nuestra pregunta vamos al metódo POST en `http://localhost:8080/ask_pdf` y colocamos este input

```json
{
    "query":"How many layers there are in a transformer"
}
```
Y deberíamos obtener nuestra respuesta

```json
{
    "respuesta": "Based on the provided information, there are 6 layers in a transformer encoder and decoder stack."
}
```

23. Otro ejemplo de pregunta respueesta
```json
{
    "query":"What is a decoder"
}
```

```json
{
    "respuesta": "A decoder in the context of a Transformer model is a component that generates an output sequence (y1, ..., yN) of symbols one element at a time. It does this by consuming previously generated symbols as additional input when generating the next symbol. The decoder is composed of a stack of N identical layers, each having three sub-layers: two self-attention mechanisms and a feed-forward network."
}
```

Perfecto ahora tienes a tu propio asistente para repsonder preguntas