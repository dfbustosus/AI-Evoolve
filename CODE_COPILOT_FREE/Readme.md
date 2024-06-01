# Gihtub Copilot

Es una muy buena herramienta pero ...

1. Hay que pagar cerca de 10-12 USD al mes
2. Tu código se puede filtrar f'acilmente
3. La nueva herramienta de microsoft `recall` va a paermitir que puedan grabars tus pantallas
4. Al final es buena opción pero existen otras opciones, ... La respuesta es sí

# Benchmark de LLMs para código

Existen muchos benchmarks pero por ejemplo esta es uno bueno [EvalPlus](https://evalplus.github.io/leaderboard.html)

EvalPlus, un marco de evaluación de síntesis de código para evaluar rigurosamente la corrección funcional del código sintetizado por LLMs. EvalPlus complementa un conjunto de datos de evaluación con una gran cantidad de casos de prueba recién producidos por un generador automático de entradas de prueba. El [Paper](https://openreview.net/forum?id=1qvx610Cu7)

Actualmente el benchmark muestra este ranking

1. 🥇GPT-4-Turbo (April 2024) ✨ ⚡86.6
2. 🥈GPT-4-Turbo (Nov 2023) ✨⚡81.7
3. 🥉 GPT-4 (May 2023) ✨⚡79.3
4. CodeQwen1.5-7B-Chat ✨⚡78.7
5. claude-3-opus (Mar 2024) ✨⚡77.4
6. DeepSeek-Coder-33B-instruct ✨⚡75

Si bien los mejores modelos para programar son GPT-4 justo después aparecen otras alternativas open source como `CodeQwen1.5` y `DeepSeek-Coder`. En particular `CodeQwen1.5` es un modelo de 7B además admite cerca de 92 lenguajes de programación 

# Acoplar modelo local con tu código

1. Deberás tener instalado Ollama, si no lo tienes es muy fácil instalarlo [Ollama](https://ollama.com/)
2. Ahora vamos a la sección de [Models](https://ollama.com/library) y buscamos `codeqwen` 
3. Abre una terminal y copia el comando
```bash
ollama run codeqwen
```
Si no tienes el modelo se descargará, probablemente se demore algunos minutos dependiendo de tu conexión a internet.
4. Ahora puedes mandar cualquier mensaje para ver si funciona e.g
```bash
Create a fibonacci function
```
5. Luego podrás salir de la interfaz con 
```bash
/exit
```
6. Ahora instalaremos una extensión de VS Code llamada `Continue`, no tiene problema con sistemas operativos.
**Nota:** Seguramente te pedirá que inicies sesión en Github. Si no tienes una cuenta de Github será mejor crear una antes de activar está extensión
7. Ahora deberás hacer click en la extensión >> `Local Models` >> `Continue`. En la parte inferior verás el nombre del modelo, podrás elegir a `codeqwen`
8. Automaticamente podrás crear un mensaje y verás los resultados e.g `Hello`
9. Creamos un archivo de prueba en cualquier lenguaje e.g `main.go`
10. Ahora podremos generar código con `CTRL+I` >> Ingresa lo que quieras generar y el código comenzará a generarse. Una vez terminado podrás aceptar o rechazar los cambios.
También puedes seleccionar el código `Ctrl+Mayús+P` y luego `CTRL+L` para añadir el código al contexto
11. Y así podrás hacer con cualquier lenguaje de programación
```bash
Create a sample ML project for a classification model
```

```bash
Create a simple WebUI example
```
12. **Opción de autocompletado** deberás hacer click en configuración abajo a la izquierda, se abrirá un archivo `config.json` y en la sección de Autocompletado cambiar de esto
```bash
tabAutocompleteModel": {
    "title": "Starcoder 3b",
    "provider": "ollama",
    "model": "starcoder2:3b"
  }
```
A esto:
```bash
"tabAutocompleteModel": {
    "title": "CodeQwen",
    "provider": "ollama",
    "model": "codeqwen:latest"
  },
```
Guarda los cambios y ahora podrás ir a tu código y verás que el autocompletado. Cool

13. También puedes usar cualquier modelo para el autocompletado si lo quieres por ejemplo el modelo (StarCoder)[https://ollama.com/library/starcoder2] lo único que debes hacer es descargar el modelo y utilizarlo como quieras
14. Ahora también si no tienees una GPU podrá susar groq como API para utilizar los modelos a través de este servicio (Groq)[https://console.groq.com/keys]
15. Luego vuelve a VS Code y da click en `+` y elige Groq, coloca tu Api Key
16. Luego puedes ir abajo y elegir `AutoDetect` y podrás ver los modelos de Groq
17. También lo puedes usar con muchos provedores sin problema

Fin!