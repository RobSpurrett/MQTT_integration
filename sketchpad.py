import json

text_file_name = 'MQTT_robs_mqtt_test.txt'
json_file_name = 'MQTT_robs_mqtt_test.json'

print("\n Debug of text file: \n")
text_file = open(text_file_name,"r")
print(text_file.read())

print("\n Debug of json file: \n")
with open(json_file_name) as json_file:
    data = json.load(json_file)
    pretty = json.dumps(data, ensure_ascii=False, indent=4)
    print(pretty)
