# Inspired by: https://pypi.org/project/paho-mqtt/#publish
import json
import datetime as dt
import paho.mqtt.client as mqtt

# Broker information
broker = 'localhost'
port = 1883

def current_timestamp():
    return dt.datetime.now(tz=dt.timezone.utc).strftime("%Y-%m-%d %H:%M:%S.%f") 

def create_payload():
    data_dict = {
            "timestamp": current_timestamp(),
            "tag": "examples/tag0",
            "value": 42,
            "units": "magic"
            }

    return json.dumps(data_dict)

client = mqtt.Client()
client.connect(broker, port, 60)

topic = "publisher/test"
payload = create_payload()
qos = 0
retain = False

client.publish(topic, payload, qos, retain)

client.disconnect()
