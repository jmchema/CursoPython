#!/usr/bin/env python
#ledPy.py
 
import time
import pigpio
pi = pigpio.pi()
 
pi.set_mode (17, pigpio.OUTPUT) #Ponemos el pin 17 como salida
 
pi.set_servo_pulsewidth (17, 1300) #Iniciamos pulsos cada 1.3 segundos para encender el LED
time.sleep(15) 
pi.stop() #Terminamos el programa.
