
# Listen to data flow on ttn MQTT server

import paho.mqtt.client as mqtt
import sys
import json

# Set the type of test this sketch is being used for (only one set True)
TEST_SOIL = True
TEST_SPACE = False

# Debug option to view the collected data files
OUTPUT_FILE_DEBUG = True

# set up generic constants
HOSTNAME = 'eu.thethings.network'
PORT = 1883
TOPICS = ['#']

# set-up constants specific to test being conducted
if TEST_SOIL:
    PASSWORD = 'ttn-account-v2.e9JegmBAyp7GHOTwk2nEBJg_-7ue1ZhXPh3P9xhLX-A'
    USERNAME = 'robs_mqtt_test'
elif TEST_SPACE:
    PASSWORD = 'ttn-account-v2.Nwq3ZyFqIsBxEWtdtPV8CebU9Kc1s3ceuwM5pZHdWeo'
    USERNAME = 'robs_ls200_beta'
else:
    sys.exit("Requested field type unknown.")


CONNECT_RESULTS = {
    0: "Connection successful",
    1: "Connection refused - incorrect protocol version",
    2: "Connection refused - invalid client identifier",
    3: "Connection refused - server unavailable",
    4: "Connection refused - bad username or password",
    5: "Connection refused - not authorised"
    }

# reports connection status
def on_connect(mqttc, mosq, obj,rc):
    print("Connected with result code " + str(rc) + " : " + CONNECT_RESULTS[rc])
    # subscribe for all devices of user
    mqttc.subscribe('#')

# reports message from device
def on_message(mqttc,obj,msg):
    # append full data as bytestrings to text file in pseudo json format
    text_file.write(str(msg.payload))
    # append data to json file
    # turn the file into a python dictionary object
    # but after decoding the data from a bytestring to string
    try:
        # for debugging perform a simple unformatted print of the data
        # print topic i.e. ttn path with the device ID at the penultimate level and 'up'
        # print(msg.topic)
        # print the payload using any decoder specified in ttn application
        # print(msg.payload)

        # print selected fields from the message received and save to csv file
        x = json.loads(msg.payload.decode('utf-8'))
        device = x["dev_id"]
        counter = x["counter"]
        payload_raw = x["payload_raw"]
        payload_fields = x["payload_fields"]
        datetime = x["metadata"]["time"]
        gateways = x["metadata"]["gateways"]
        # print for every gateway that has received the message and extract RSSI
        for gw in gateways:
            gateway_id = gw["gtw_id"]
            rssi = gw["rssi"]
            selected_output = datetime + "," + device + "," + str(counter) + ","+ gateway_id + ","+ str(rssi) + "," + str(payload_fields) +"\n"
            print(selected_output)
            csv_file.write(selected_output)
    except Exception as error_statement:
        print(error_statement)
        pass


def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))

def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(mqttc,obj,level,buf):
    print("message:" + str(buf))
    print("userdata:" + str(obj))

mqttc= mqtt.Client()
# Assign event callbacks
mqttc.on_connect=on_connect
mqttc.on_message=on_message
# Log all MQTT protocol events and exceptions in callbacks
mqttc.on_log = on_log

mqttc.username_pw_set(USERNAME, PASSWORD)
mqttc.connect(HOSTNAME,PORT,60)

# Open a file to store message data
data_file_name = "MQTT_" + USERNAME
# full data as byte strings including metadata
text_file_name = data_file_name + '.txt'
# selected message fields output into CSV format
csv_file_name = data_file_name + '.csv'

text_file = open(text_file_name,"a")
csv_file = open(csv_file_name,"a")

# Listen to server
run = True
try:
    while run:
        mqttc.loop()
except KeyboardInterrupt:
    print("\n MQTT session terminated with Ctrl-C.")

if OUTPUT_FILE_DEBUG:
    # print contents of text file
    print("\n Debug of text file: \n")
    text_file = open(text_file_name,"r")
    print(text_file.read())
    # print contents of csv file
    print("\n Debug of csv file: \n")
    csv_file = open(csv_file_name,"r")
    print(csv_file.read())
    '''
    with open(json_file_name) as json_file:
        #print(json_file.read())
        # turn file contents into a python dictionary object
        data = json.load(json_file)
        # create a pretty json version of the file
    pretty = json.dumps(data, indent=4)
    print(pretty)
    '''

# tidy up and close files
text_file.close()
csv_file.close()
