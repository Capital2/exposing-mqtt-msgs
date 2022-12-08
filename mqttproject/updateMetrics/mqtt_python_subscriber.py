from paho.mqtt import client as mqtt_client
import random
import time

broker = 'localhost'
port = 1883
client_id = f'python-mqtt-{random.randint(0, 1000)}'
topics = ["projet/temperature", "projet/humidity"]

def connect_mqtt():
    """on_connect This function will be called after connecting the client, 
        and we can determine whether the client is connected successfully according to rc in this function. 
        Usually, we will create an MQTT client at the same time and this client will connect to localhost."""
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client, topic):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1

def subscribe(client: mqtt_client, topic):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        update_file(msg.payload.decode(), msg.topic)

    client.subscribe(topic)
    client.on_message = on_message

def update_file(payload: str, topic: str):
    subtop = topic.split('/')[-1]
    with open(f"{subtop}.txt", "w") as f:
        f.write(f"{subtop}: {payload}")
    pass

def run():
    client = connect_mqtt()
    for t in topics:
        subscribe(client, t)
    client.loop_forever()

if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        print("Bye!")
        exit(0)