import paho.mqtt.client as mqtt

# Para poder recibier mensajes (escribir)
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
 
# Para traza 
def on_log(client, userdata, level, buf):
    print("log: ",buf)

# Crear el cliente de mqtt
# client = mqtt.Client(client_id=””, clean_session=True, userdata=None, protocol=MQTTv311, transport=”tcp”)
# como lo anterior son cosas por defecto vale asi
client = mqtt.Client()
client.connect("127.0.0.1")

#Nos auto suscribimos
client.subscribe("casa")
# funcion de callback para leer el mensaje que mandamos
client.on_message=on_message
# asignamos el callback de la traza
client.on_log = on_log
client.loop_start()
msg = client.publish("casa","Estamos desde Thony")