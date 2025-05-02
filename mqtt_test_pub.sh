#!/bin/bash

# Send a simple Hello World to the MQTT broker (test topic)
mosquitto_pub -t test -m '{"items": "Hello MQTT!"}'
