import random

from paho.mqtt import client as mqtt_client

broker = '149.162.184.124'  # MQTT broker ip address
port = 1883
topic = "test"
client_id = f'python-mqtt-{random.randint(0, 100)}'  # Randomly generated client ID
username = ''
password = ''


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, error code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode('ISO-8859-2')}` from `{msg.topic}` topic")  # .decode()
        file = open('received.xml', 'wb')  # xml file for storing received data in binary
        file.write(msg.payload)  # store to local file
        file.close()

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
