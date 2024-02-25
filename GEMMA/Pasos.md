# Ollama

1. Ir a la pagina de `Ollama` y descargar la tool `https://ollama.com/download/windows`
2. Instalar la herramienta en caso de que no la tengas
3. Abrir una temrinal y verificar que tengas instalado Ollama
```bash
ollama -v
```
4. Luego de eso simplemente deberas descargar el modelo con:
```bash
ollama run gemma
```
5. Por defecto te descargará el modelo de 2Billones de params lo cual pueedees verificar en esta pagina `https://ollama.com/library/gemma`. También puedes descargar cualquiera de los dos models con
```bash
ollama run gemma:7b
```
6. Luego de eso simplemente podras usar el modelo y conversar con el

Algunos features adicionales

`/show`
- `/show info`         Show details for this model
- `/show license`      Show model license
- `/show modelfile`    Show Modelfile for this model
- `/show parameters`   Show parameters for this model
- `/show system`       Show system message
- `/show template`     Show prompt template

`/set`
- `/set parameter ...`     Set a parameter
- `/set system <string>`   Set system message
- `/set template <string>` Set prompt template
- `/set history`           Enable history
- `/set nohistory`         Disable history
- `/set wordwrap`          Enable wordwrap
- `/set nowordwrap`        Disable wordwrap
- `/set format json`       Enable JSON mode
- `/set noformat`          Disable formatting
- `/set verbose`           Show LLM stats
- `/set quiet`             Disable LLM stats

`/load` 
- /load <model>   Load a session or model

`/save`
- /save <model>   Save your current session

`/bye`
- /bye            Exit

`Ayuda`
- /?, /help       Help for a command
- /? shortcuts    Help for keyboard shortcuts

# Preguntas 
1. whats the difference between LLAMA, Alpaca and Stable Vicuna
```bash
/bye
ollama run gemma
/set verbose
/set history
```
2.  What is the law of Faraday
3. What are the main drawbacks of GPT-4
4. Write an email saying to an recruiter that i need a couple of months to finish my Phd before I accept the IT offer
5. Can you explain the math behing the transformers arquitecture
6. Create a python function to implement dynamic programming to solve an integral complex with numeric methods
7.  Provide a simple golang code to apply dynamic programming
8. Calculate the compound interest if I invest 2000 USD today and the interest rate if 5.75% yearly and my invest is gonna be 14 months with the bank