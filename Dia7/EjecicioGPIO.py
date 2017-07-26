# Importo el diccionario morse
import morse
import time
import RPi.GPIO as GPIO

frase = input("Introduce una  frase: ")



"""
frase_morse =  []
for c in frase:
    c_morse = morse.CODE[c.upper()]
    frase_morse.append(c_morse)
    print("Traduccion: {} --> {}".format(c,c_morse))

Esto era lo mio lo abandona por las funciones para la placa
"""

# Incializacion
LED = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT, initial=0)

def emite_punto():
    GPIO.output(LED, 1)
    time.sleep(0.6)
    GPIO.output(LED, 0)
    time.sleep(0.1)
    print(".")

def emite_raya():
    print("-")

def pausa():
    print(" ")
    time.sleep(1)


def en_morse(letra):
    codigo = morse.CODE[letra]
    for simbolo in codigo:
        if simbolo == ".":
            emite_punto()
        elif simbolo == '-':
            emite_raya()
        else:
            pass
        pausa()

for c in frase.upper():
    en_morse(c)
        


