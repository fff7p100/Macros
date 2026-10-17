nano ~/tecla_1.py
python3 ~/tecla_1.py


from pynput import keyboard
import time


controller = keyboard.Controller()
bloqueo = False

def on_press(key):
    global bloqueo
    if bloqueo:
        return

    try:
       
        if hasattr(key, 'char') and key.char == '1':
            bloqueo = True

          
            for _ in range(3):
                controller.press(' ')
                controller.release(' ')
                time.sleep(0.01) 

            time.sleep(0.05)
            bloqueo = False
    except AttributeError:
        pass

print("Script activo. Presiona 1 en cualquier lado (Ctrl+C para salir).")
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

