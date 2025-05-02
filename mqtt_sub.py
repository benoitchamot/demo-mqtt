# A simple MQTT client
import logging
import random
import json
from paho.mqtt import client as mqtt_client

# Broker settings
broker = 'localhost'
port = 1883


# Topics
topics = ['test']

# Set up logging
logging.basicConfig(
        filename='logs/sub.log',
        filemode = 'a',
        format='%(asctime)s - %(message)s',
        level=logging.INFO
        )

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        """
        On-connect callback. Executed on connection only
        """

        # Connect to all topics
        for topic in topics:
            client.subscribe(topic)

    def on_disconnect(client, userdata, rc):
        """
        On-disconnect callback. Executed on any disconnection event.
        """

        # Try and reconnect if the disconnect was not voluntary
        if rc != 0:
            while True:
                try:
                    logging.info("Attempting to reconnect...")
                    client.reconnect()
                    logging.info("Connected to MQTT Broker!")
                    break

                except Exception as e:
                    logging.info(f"Reconnect failed: {e}")
                    time.sleep(5)  # Give it some time

    def on_message(client, userdata, msg):
        """
        On-message callback. Executed whenever a message is received.
        """

        # Print the message as is
        print(f"Raw: {msg}")
        
        # Get the message payload
        msg_json = json.loads(msg.payload)
        msg_items = msg_json["items"]

        print(f"JSON: {msg_json}")

    # Create a persistent client
    client_id = f'subscribe-{random.randint(0, 100)}'
    client = mqtt_client.Client(client_id, clean_session=False)

    # Assign callbacks
    client.on_message = on_message
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect

    # Connect the client
    client.connect(broker, port)

    return client


def run():
    client = connect_mqtt()
    client.loop_forever()

if __name__ == '__main__':
    run()
