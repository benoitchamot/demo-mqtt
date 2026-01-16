# A simple MQTT client
import logging
import random
import json
import sqlite3
import time
from paho.mqtt import client as mqtt_client

# Broker settings
broker = 'localhost'
port = 1883

# Client settings
QoS = 2

# Topics
topics = ['test', 'publisher/test']

# Set up logging
logging.basicConfig(
        filename='logs/sub.log',
        filemode='a',
        format='%(asctime)s - %(message)s',
        level=logging.INFO
        )


def write_to_db(msg_topic, msg_json):
    # Connect to database
    con = sqlite3.connect("mqtt.db")
    cur = con.cursor()

    # Write to database
    table = "messages"
    query = f"""INSERT INTO {table} (timestamp, topic, tag, value, units)
    VALUES
        ('{msg_json['timestamp']}',
         '{msg_topic}',
         '{msg_json['tag']}',
         '{msg_json['value']}',
         '{msg_json['units']}'
        );
    """

    cur.execute(query)

    con.commit()
    con.close()


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        """
        On-connect callback. Executed on connection only
        """

        # Connect to all topics
        for topic in topics:
            client.subscribe(topic, qos=QoS)

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

        # Get the message topic and payload
        msg_topic = msg.topic
        msg_json = json.loads(msg.payload)

        if msg_topic == 'test':
            # For the test topic, simply print the message
            print(f"JSON: {msg_json}")
        else:
            # For any other topic, process the message
            # (not implemented yet)
            print("message received on", msg_topic)
            write_to_db(msg_topic, msg_json)

            # TODO: remove verbose
            print(f"JSON: {msg_json}")

    # Create a persistent client
    # client_id = f'subscribe-{random.randint(0, 100)}'
    client_id = f"sub-client-qos{QoS}"
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
