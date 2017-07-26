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

# Lo hacemos por polling, por encuesta
while True:
    state = GPIO.input(BUTTON)
    GPIO.output(LED,state)
    print("el boton esta {}".format(state))
    time.sleep(0.1)
