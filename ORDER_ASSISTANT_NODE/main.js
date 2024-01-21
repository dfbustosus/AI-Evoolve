// 1. Dependencies
import * as dotenv from 'dotenv';
import { OpenAI } from 'openai';
import readlineSync from 'readline-sync';

// 2. Cargar variables de env
dotenv.config();
const key = process.env.OPENAI_KEY;
const id_assistant= process.env.ASSISTANT_ID;
if (!key) {
  console.error('OpenAI API key is missing. Please check your .env file.');
  process.exit(1);
}

// 3. Definir cliente y asistente
const client = new OpenAI({apiKey: key});

const assistant = await client.beta.assistants.retrieve(
    id_assistant
);
//console.log(assistant);

// 4. Crear un nuevo Thread
const thread = await client.beta.threads.create();
//console.log(thread);

// 5. Loop de conversacion
let stop = true;

while (stop) {
    // 5.1 User input
    const user_input= readlineSync.question('user: ');
    // 5.2 Agregar mensaje al assistant
    const message = await client.beta.threads.messages.create(thread.id,{
        role: "user",
        content: user_input
    })
    // 5.3 Correr el asistente para obtener response
    let run = await client.beta.threads.runs.create(thread.id,{
        //thread_id: thread.id,
        assistant_id: assistant.id
        // Opcional instructions: "Algo adicional que quiero que haga"
    })
    // 5.4 Obtener status de corrida
    let i =0;
    while (run.status !== "completed" && run.status !== "failed" && run.status !== "requires_action"){
        if (i>0){
            await new Promise(resolve => setTimeout(resolve, 500)); // Sleep for 1 seconds
        }  
        run = await client.beta.threads.runs.retrieve(thread.id, run.id);
        i++;
    }

    // 5.5 Trabajar sobre requires_action status
    if (run.status == "requires_action"){
        const toolsToCalls = run.required_action.submit_tool_outputs.tool_calls;
        //console.log("-----------------------------");
        //console.log(toolsToCalls)
        //console.log("-----------------------------");
        // 5.5.1 Ejecutar la accion correspondiente
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
                // Extract data from the function to do something
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
        // 5.5.2 Retornar resultados
        //run = await client.beta.threads.runs.submit_tool_outputs(thread.id, run.id, toolOutputArray);
        //console.log("Entrando a error");
        const tool_outputs = toolOutputArray.map(({ tool_call_id, output }) => ({ tool_call_id, output }));
        //run = await client.beta.threads.runs.submitToolOutputs(thread.id, run.id, toolOutputArray);
        run = await client.beta.threads.runs.submitToolOutputs(thread.id, run.id, { tool_outputs });
        //console.log("Saliendo de error");
        // 5.5.3 Revisar el status de nuevo
        i = 0;
        while (run.status !== "completed" && run.status !== "failed" && run.status !== "requires_action") {
            if (i > 0) {
              await new Promise(resolve => setTimeout(resolve, 500)); // Sleep for 1 seconds
            }
            run = await client.beta.threads.runs.retrieve(thread.id, run.id);
            i++;
          }
    }

    // 5.6 Obtener la respuesta del assistant
    //const messages = await openai.beta.threads.messages.list(thread.id);
    //const reversedMessages = messages.reverse();
    //console.log('Assistant:', reversedMessages[0].content[0].text.value);
    //
    const messagesResponse = await client.beta.threads.messages.list(thread.id);
    const messages = Array.isArray(messagesResponse.data) ? messagesResponse.data : [];
    // Encontrar utlima respuesta del array 
    const assistantMessage = messages.find(message => message.role === 'assistant');
    // Logear la respuesta del asistente
    if (assistantMessage) {
    console.log('Assistant:', assistantMessage.content[0].text.value);
    } else {
    console.log('No assistant response found.');
    }
    // 5.7 Guargar la lista final de mensajes 
    if (!stop) {
        const listMessages = messages.map(each => ({ [each.role]: each.content[0].text.value }));
        console.log("===================================");
        console.log('Record de mensajes');
        console.log(listMessages);
        console.log("===================================");
        break;
    }
}