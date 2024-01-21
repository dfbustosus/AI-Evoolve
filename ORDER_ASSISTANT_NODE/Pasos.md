# Crear asistente de pedido
1. Tener instalado node verificar comando
```bash
node --version
```
2. Crear una carpeta e inicializar proyecto
```bash
npm init
```
3. Instalar dependencias
```bash
npm install dotenv openai readline-sync
```
4. En el archivo `package.json` introducir la linea `"type":"module"`
```json
{
  "name": "order_assistant_node",
  "version": "1.0.0",
  "description": "",
  "main": "main.js",
  "type": "module",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "dotenv": "^16.3.2",
    "openai": "^4.25.0",
    "readline-sync": "^1.4.10"
  }
}
```
5. Definir el asistente para esto puedes utilizar el archivo en la siguiente url [Creacion de asistente](https://github.com/dfbustosus/AI-Evoolve/blob/main/OPENAI_ASSISTANTS/Creacion_asistente.py)
6. Utilizar el `assistant_id` y la `apiKey` que tengas para que puedas utilizar tu asistente
7. Correr el proyecto con el comando
```bash
node main.js
```
8. Perfecto ya tienes tu engine corriendo para que lo pruebes