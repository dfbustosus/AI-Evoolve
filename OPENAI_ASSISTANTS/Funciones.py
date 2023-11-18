gather_user_data = {
    "name": "gather_user_data",
    "description": "Obtener datos del paciente para agendar una cita medica",
    "parameters": {
        "type": "object",
        "properties": {
            "telefono": {"type": "string", "description": "Un telefono valido, e.g., 3362296959"},
            "nombre": {"type": "string", "description": "Primer nombre del paciente, e.g., David"},
            "apellido": {"type": "string", "description": "Apellido del paciente, e.g., Bustos"},
            "email": {"type": "string", "description": "Un email valido, e.g., david@gmail.com"},
        },
        "required": ["telefono", "nombre", "apellido", "email"]
    }
}

gather_health_data = {
    "name": "gather_health_data",
    "description": "Obtener la razon de la cita medica",
    "parameters": {
        "type": "object",
        "properties": {
            "razon_cita": {
                "type": "string",
                "description": "La razon del paciente para la cita "
            }
        },
        "required": ["razon_cita"]
    }
}

gather_appointment_data = {
    "name": "gather_appointment_data",
    "description": "Obtener los datos para la cita (date, time) para agendar la cita",
    "parameters": {
        "type": "object",
        "properties": {
            "fecha": {"type": "string", "description": "Fecha deseada de visita, e.g., Nov 11 2023"},
            "hora": {"type": "string", "description": "Hora deseada de visita, e.g., 4PM"}
        },
        "required": ["fecha", "hora"]
    }
}

not_talk = {
    "name": "not_talk",
    "description": "Preguntarle al usuario si quiere continuar hablando, si no desea terminar la ayuda del asistente",
    "parameters": {
        "type": "object",
        "properties": {
            "fin": {"type": "boolean", "description": "El usuario no quiere hablar mas"}
        },
        "required": ["fin"]
    }
}
