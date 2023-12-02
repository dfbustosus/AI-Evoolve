1. Instalar python 3.10.9
2. Crear virtual env con: virtualenv myenv
3. .\myenv\Scripts\activate
4. git clone https://github.com/oobabooga/text-generation-webui.git
5.  cd .\text-generation-webui\
6. Inicializar GPU: .\start_windows.bat
7. Poner la version de GPU que tengas: A
8. Poner N (en caso de que quieras bajar tu version actual).
Ahora se instalaran las dependencias necesarias para que funcione todo
9. Ahora deberas dar click en la url que se genere:  http://127.0.0.1:7860
Veras un entorno de UI para interactuar 
10. Ir a la pestana de Models
11. En Download model or LoRA poner: TheBloke/Llama-2-13B-chat-GPTQ
Esto lo encuentras en: https://huggingface.co/TheBloke/Llama-2-13B-chat-GPTQ
!!!!!Ten en cuenta tus requerimientos de RAM!!!!!!!!

12. Click en Download
13. Comenzara el proceeso de descarga esto va a tomar bastante tiempo probablemente (el modelo quedara guardado en ./models)
14. Click en Refresh (Boton azul para actualizar) y elegir el modelo que estas usando : TheBloke_Llama-2-13B-Chat-fp16. Luego click en Load
15. Esperar por mas tiempo (depende de nuevo de varios factores: velocidad conexión, ram, gpu, etc...)
16. Click en parameters incrementa la cantidad maxima de tokens. Puedes cambiar las cosas que necesites
17. Ahora probemos que tan bien funciona
- Tell me a joke
- Write a script in python to print numbers from 0 to 50
- Implement a chatbot code in python
- Create a poeam about AI in exactly 30 words
- Write en email to my boss that i am busy this day
- Who was the first president in USA killed
- How to hack the pentagon
- Pregunta lo que quieras btw!!!

Otros modelos disponibles:

1. KoalaAI_OPT-1.3b-Chat
2. TheBloke/koala-7B-HF
3. TheBloke/Llama-2-13B-chat-GPTQ


