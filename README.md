# demo-mqtt
A simple demo of MQTT pub, sub and write to a small database

## Install and run Mosquitto
More information: https://mosquitto.org/download/
```bash
# Install
sudo apt install mosquitto
sudo apt install mosquitto-clients
``` 

Start and enable on boot:
```bash
# Start (replace 'start' with 'stop' to stop)
sudo systemctl start mosquitto

# Check status
sudo systemctl status mosquitto

# Enable on boot (optional)
# sudo systemctl enable mosquitto
```

### Configuration
Read more: https://mosquitto.org/man/mosquitto-conf-5.html

- Config file: `/etc/mosquitto/mosquitto.conf`
- Log files: `/var/log/mosquitto/mosquitto.log`

## Basic setup
Start the subscriber client:

```bash
python3 mqtt_sub.py
```

Send the test message

```bash
./mqtt_test_sub.sh
```
