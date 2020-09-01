
# Very simple example of subscription for Paho MQTT

# import context  # Ensures paho is in PYTHONPATH - not required

import paho.mqtt.subscribe as subscribe
import sys

print(sys.path)

HOSTNAME = 'eu.thethings.network'
PORT = '1883'

TOPICS = ['#']
PASSWORD = 'ttn-account-v2.e9JegmBAyp7GHOTwk2nEBJg_-7ue1ZhXPh3P9xhLX-A'
USERNAME = 'robs_mqtt_test'

data = subscribe.simple(
    hostname = 'eu.thethings.network',
    port = 1883,
    # subscribe to all topics
    topics = '#',
    # USERNAME is the TTN application ID (the name you assigned to it)
    # PASSWORD is the applciation access key begining 'ttn-account-v2.<etc>'
    auth = {'username': USERNAME, 'password': PASSWORD },
    # number of seconds to keep the connection alive for (600 = 10 mins)
    keepalive = 600,
    # waits for msg_count number of messages to be ready before it relays them
    msg_count = 2
    )

for a in data:
    print(a.topic)
    print(a.payload)


"""
The commends below and answer are using the MQTT CLI for comparison with the output from this program

    Robs-Home-iMac:~ rob$ source ~/.venvs/lacuna/bin/activate
(lacuna) Robs-Home-iMac:~ rob$ mosquitto_sub -h eu.thethings.network -p 1883 -t '#' -u 'robs_mqtt_test' -P 'ttn-account-v2.e9JegmBAyp7GHOTwk2nEBJg_-7ue1ZhXPh3P9xhLX-A' -v
robs_mqtt_test/devices/ttn_uno/up {"app_id":"robs_mqtt_test","dev_id":"ttn_uno","hardware_serial":"0004A30B001C3551","port":1,"counter":384,"payload_raw":"Azs=","payload_fields":{"length":2,"moisture":827},"metadata":{"time":"2020-08-23T17:33:32.881383425Z","frequency":867.1,"modulation":"LORA","data_rate":"SF7BW125","airtime":46336000,"coding_rate":"4/5","gateways":[{"gtw_id":"eui-3133303721003a00","timestamp":1573586961,"time":"2020-08-23T17:33:31.886882Z","channel":3,"rssi":-71,"snr":9,"rf_chain":0}]}}
robs_mqtt_test/devices/ttn_uno/up {"app_id":"robs_mqtt_test","dev_id":"ttn_uno","hardware_serial":"0004A30B001C3551","port":1,"counter":385,"payload_raw":"Azw=","payload_fields":{"length":2,"moisture":828},"metadata":{"time":"2020-08-23T17:34:35.001864077Z","frequency":868.1,"modulation":"LORA","data_rate":"SF7BW125","airtime":46336000,"coding_rate":"4/5","gateways":[{"gtw_id":"eui-3133303721003a00","timestamp":1635701433,"time":"2020-08-23T17:34:34.000717Z","channel":0,"rssi":-71,"snr":8,"rf_chain":0},{"gtw_id":"eui-3133303721003a00","timestamp":1635701433,"time":"2020-08-23T17:34:34.001128Z","channel":5,"rssi":-115,"snr":-6,"rf_chain":0}]}}


"""
