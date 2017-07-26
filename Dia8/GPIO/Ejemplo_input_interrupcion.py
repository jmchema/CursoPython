import RPi.GPIO as GPIO
import time

# Asignando pines a variables
LED = 17
BUTTON = 7
# Ponemos en modo BCM para contar los pines
GPIO.setmode(GPIO.BCM)

# Configuramos las entradas y salidas
GPIO.setup(LED, GPIO.OUT, initial=1)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Hacemos un pull down para poner un 0 por defecto (sin pulsar)

# Encendemos el LED poniendole un uno
GPIO.output(LED,1)

# Leemos el estado del boton y lo sacamos por pantalla
# Si esta activado ponemos un uno.

# Lo hacemos por interrupcion

count = 0

# Funcion que se ejecutara con la interrupcion
def subiendo(event):
    global count
    count += 1
    print("Pulsacion {} - Subiendo! (Pin: {})".format(count,event))
    
def bajando(event):
    global count
    count += 1
    print("Pulsacion {} - Bajando! (Pin: {})".format(count,event))
    
def cambio(event):
    global count
    count += 1
    print("Pulsacion {} - Cambiado! (Pin: {})".format(count,event))
    if GPIO.input(BUTTON) == 1:
        print("Subida!")
    else:
        print("Bajada")

# Declaracion de la interrupcion. Subida, bajada, cambio. Pero solo se puede una.
# Pulsado
#GPIO.add_event_detect(BUTTON,GPIO.RISING, callback=subiendo)
#Sin pulsar
#GPIO.add_event_detect(BUTTON,GPIO.FALLING, callback=bajando)
#Cualquiera
GPIO.add_event_detect(BUTTON,GPIO.BOTH, callback=cambio)




