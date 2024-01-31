// 1. Dependencies
import express from 'express';
import * as dotenv from 'dotenv';
import { OpenAI } from 'openai';
//import readlineSync from 'readline-sync';

// 2. Cargar variables de env
dotenv.config();
const key = process.env.OPENAI_KEY;
const id_assistant = process.env.ASSISTANT_ID;

if (!key || !id_assistant) {
  console.error('OpenAI API key o Assistant ID estan nulos. Chequear el .env file.');
  process.exit(1);
}

// 3. Definir cliente y asistente
const client = new OpenAI({ apiKey: key });
const assistant = await client.beta.assistants.retrieve(id_assistant);
const thread = await client.beta.threads.create();
const app = express();
const port = 3000;
let stop= true;

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// 4. Poner el HTML para el user input
app.get('/', (req, res) => {
  res.sendFile('C:/Users/david/Desktop/AI-Evoolve/ORDER_ASSISTANT_NODE/'+'index.html');
});

// 5. Manipular el input 
app.post('/submit', async (req, res) => {
  const user_input = req.body.user_input;
  const message = await client.beta.threads.messages.create(thread.id, {
    role: 'user',
    content: user_input,
  });

  let run = await client.beta.threads.runs.create(thread.id, {
    assistant_id: id_assistant,
  });

  let i = 0;
  while (run.status !== 'completed' && run.status !== 'failed' && run.status !== 'requires_action') {
    if (i > 0) {
      await new Promise(resolve => setTimeout(resolve, 1000)); // Esperar 1 seg
    }
    run = await client.beta.threads.runs.retrieve(thread.id, run.id);
    i++;
  }

  if (run.status === 'requires_action') {
    // Trabajar con el requires_action status 
    const toolsToCalls = run.required_action.submit_tool_outputs.tool_calls;
        //console.log("-----------------------------");
        //console.log(toolsToCalls)
        //console.log("-----------------------------");
        // 5.1 Ejecutar la accion correspondiente
        const toolOutputArray =[];
        for (const eachTool of toolsToCalls){
            const toolCallId = eachTool.id;
            const functionName = eachTool.function.name;
            const functionArg = eachTool.function.arguments;
            console.log("Tool id: ", toolCallId);
            console.log("Funcion llamada: ", functionName);
            console.log("Parametros a usar: ", functionArg);
            let output = "";
            // Manejar distinos tool functions
            if (functionName === "gather_user_data") {
                // Extraer data de la funcion para hacer cosas
                const { telefono, nombre, apellido, email } = JSON.parse(functionArg);
                console.log('Telefono: ', telefono, ' Nombre: ', nombre, ' Apellido: ', apellido, ' Email: ', email);
                output = "Ahora pregunta sobre los productos que desea ordenar";
              } else if (functionName === "gather_product_data") {
                output = "Ahora pregunta sobre detalles acerca de ubicación y momento para entregar la orden";
              } else if (functionName === "gather_order_data") {
                output = "Haz un resumen de la orden al cliente e informale que su pedido ha sido tomado satisfactoriamente";
              } else if (functionName === "not_talk") {
                if (JSON.parse(functionArg).fin === true) {
                  stop = false;
                }
                output = "Genial que tengas un gran día, fue un gusto ayudarte hoy día";
              }
            //console.log("Todo en orden");
            toolOutputArray.push({ tool_call_id: toolCallId, output });
            //console.log(toolOutputArray);
        }
        // 5.2 Retornar resultados
        //run = await client.beta.threads.runs.submit_tool_outputs(thread.id, run.id, toolOutputArray);
        //console.log("Entrando a error");
        const tool_outputs = toolOutputArray.map(({ tool_call_id, output }) => ({ tool_call_id, output }));
        //run = await client.beta.threads.runs.submitToolOutputs(thread.id, run.id, toolOutputArray);
        run = await client.beta.threads.runs.submitToolOutputs(thread.id, run.id, { tool_outputs });
        //console.log("Saliendo de error");
        // 5.3 Revisar el status de nuevo
        i = 0;
        while (run.status !== "completed" && run.status !== "failed" && run.status !== "requires_action") {
            if (i > 0) {
              await new Promise(resolve => setTimeout(resolve, 1000)); // Sleep  1 sec
            }
            run = await client.beta.threads.runs.retrieve(thread.id, run.id);
            i++;
          }
  }
  // 5.4 Obtener la respuesta del assistant
  const messagesResponse = await client.beta.threads.messages.list(thread.id);
  const messages = Array.isArray(messagesResponse.data) ? messagesResponse.data : [];

  const assistantMessage = messages.find(message => message.role === 'assistant');

  if (assistantMessage) {
    res.send({ response: assistantMessage.content[0].text.value });
  } else {
    res.send({ response: 'No assistant response found.' });
  }
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
// correr: node app.js