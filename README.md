# demo-mqtt
A simple demo of MQTT pub, sub and write to a small database

## Install sqlite3
This code uses sqlite as a local database. The data are stored in a file called `mqtt.db` that must be created by the user.

Read more: https://sqlite.org/cli.html

```bash
# Install sqlite CLI
sudo apt install sqlite3
```

The database can be set up by running the provided script:
```bash
./create_db.sh
```

This will create the `mqtt.db` file with a table called `messages` with the following columns:
- `timestamp`: UTC timestamp of the message
- `topic`: the topic on which the message was published
- `tag`: the tag to which the data is attached
- `value`: the value of the data (as text, even for numerical values)
- `units`: the engineering units (empty string if none)

Make sure to create the database before using the publisher client.

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
