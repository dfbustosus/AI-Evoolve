from flask import Flask, request
from langchain_community.llms import Ollama
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_community.document_loaders import PDFPlumberLoader
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain.prompts import PromptTemplate

app= Flask(__name__)

folder_path ="db"

llm= Ollama(model="llama3", temperature=0.3, num_predict=512)
embedding = FastEmbedEmbeddings()
text_splitter= RecursiveCharacterTextSplitter(
    chunk_size= 1024, chunk_overlap=80, 
    length_function= len, is_separator_regex=False
)


raw_prompt= PromptTemplate.from_template("""
    <s>[INST] You are a technical assistant to provide answers based only on the provided information.If you dont know the answer with the provided information be honest and answer: 'Sorry I do not know the answer for this question' [/INST] </s>
    [INST] {input}
            Context: {context}
            Answer: 
    [/INST]
"""
)

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

# Subir pdf
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

# Preguntar pdf
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
    print(result)
    
    response_answer= {"respuesta": result['answer'].replace("<s>[INST]", "").replace("[/INST]</s>","").strip()}
    return response_answer


def start_app():
    app.run(host="0.0.0.0", port=8080, debug=True)

if __name__ =="__main__":
    start_app()
