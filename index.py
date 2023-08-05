import pyautogui
import keyboard
import time
import clipboard

def enviar_mensaje(chat_box_coordinates):
    # Simula un clic en el cuadro de chat para que el texto se escriba allí
    pyautogui.click(chat_box_coordinates)

    # Escribe los mensajes en el chat
    mensajes = [
        "😀",
        "¡Buenos tardes estimado! ☀️😊",
        "¿Qué modelo es tu vehículo? 🚗🤔💨",
        " ¿Qué medida de llantas o aros deseas? 🚗🛣️💨",
        "📞😊 Pasame tu número de WhatsApp 📲 para pasarte el catálogo 📚 y el precio 💰. ¡Estoy emocionado por ayudarte! 🎉🤗",
        "👍 Llantas: https://aroszehlendorf.com/llantas-zehlendorf/ 🛍️ Haces clic en un producto y luego en el botón de Whatsapp de ese producto para pedir precio. 📲💬😄",
        "👍 Aros: https://aroszehlendorf.com/aros-zehlendorf/ 🛍️ Haces clic en un producto y luego en el botón de Whatsapp de ese producto para pedir precio. 📲💬😄",
        ""
    ]

    for mensaje in mensajes:
        clipboard.copy(mensaje)  # Copia el mensaje al portapapeles
        pyautogui.hotkey('ctrl', 'v')  # Pega el mensaje
        pyautogui.press('enter')
        time.sleep(0.5)  # Puedes ajustar este retraso según tus necesidades

# Combinación de teclas para activar la automatización (Ctrl+Alt+R)
combinacion_teclas = 'ctrl+shift+alt+r'

# Bandera para asegurarnos de que el mensaje solo se envíe una vez por combinación de teclas presionada
mensaje_enviado = False

while True:
    if keyboard.is_pressed(combinacion_teclas) and not mensaje_enviado:
        # Obtiene las coordenadas actuales del cursor del mouse
        chat_box_coordinates = pyautogui.position()

        # Activa la automatización solo cuando se presione la combinación de teclas y no se haya enviado el mensaje previamente
        enviar_mensaje(chat_box_coordinates)
        mensaje_enviado = True
    elif not keyboard.is_pressed(combinacion_teclas):
        # Restablece la bandera cuando la combinación de teclas se suelta
        mensaje_enviado = False
    time.sleep(0.1)
