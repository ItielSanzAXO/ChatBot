from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

account_sid = 'AC4a72771d366606f20c83bb5d8fde1435'
auth_token = '40d2ea5a2c715fed97feb40f813e3f57'
client = Client(account_sid, auth_token)

def responder_mensaje(mensaje):
    # Aquí puedes implementar la lógica del chatbot para procesar el mensaje del usuario y generar una respuesta.
    if "Hola" in mensaje:
        return "Hola, ¿en qué puedo ayudarte?"
    elif "Resultados" in mensaje:
        return "Por supuesto, ¿cuál es el número de estudio?"
    elif "Ubicación" in mensaje:
        return "La ubicación del paciente es en la sala 203."
    elif "Otro lugar" in mensaje:
        return "¿A cuál área del hospital te refieres?"

def enviar_respuesta_twilio(respuesta, numero_destino):
    response = MessagingResponse()
    response.message(respuesta)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=respuesta,
        to=f'whatsapp:{numero_destino}'
    )

    return message.sid

# Manejo de mensajes entrantes
mensaje_usuario = "Hola"  # Simula un mensaje de usuario
numero_destino = "5215536688304"  # Reemplaza con el número de destino correcto

respuesta = responder_mensaje(mensaje_usuario)
enviar_respuesta_twilio(respuesta, numero_destino)
