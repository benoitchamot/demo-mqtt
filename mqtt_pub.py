# Inspired by: https://pypi.org/project/paho-mqtt/#publish
import json
import datetime as dt
import paho.mqtt.client as mqtt
import sys

# Broker information
broker = 'localhost'
port = 1883


def current_timestamp():
    return dt.datetime.now(tz=dt.timezone.utc).strftime("%Y-%m-%d %H:%M:%S.%f")


def create_payload(value: int = 42):
    data_dict = {
            "timestamp": current_timestamp(),
            "tag": "examples/tag0",
            "value": value,
            "units": "magic"
            }

    return json.dumps(data_dict)


def publish_value(value: int):
    client = mqtt.Client()
    client.connect(broker, port, 60)

    topic = "publisher/test"
    payload = create_payload(value)
    qos = 1
    retain = False

    client.publish(topic, payload, qos, retain)

    client.disconnect()


if __name__ == '__main__':
    print(len(sys.argv))

    if len(sys.argv) < 2:
        print("Missing argument value")

    else:
        val = int(sys.argv[1])
        publish_value(val)
