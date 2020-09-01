

import json

# set-up a dictionary ready to export and play with JSON formats
data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

# write the dictionary as a JSON file
with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)


# reading back the JSON file and printing some data from it
with open('data.txt') as json_file:
    data = json.load(json_file)
    for p in data['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')

# to print the JSON file in pretty format:
print("Pretty formated output: ")
pretty = json.dumps(data, indent=4)
print(pretty)


# which could aslo be done from the command line e.g.
# echo '{"people":[{"name":"Scott", "website":"stackabuse.com", "from":"Nebraska"}]}' | python -m json.tool


USERNAME = 'robs_mqtt_test'

data_file_name = "MQTT_messages_for_" + USERNAME + ".txt"
#data_file = open(data_file_name,"a")

data_file = open(data_file_name,"r")
print("\n Straight print out of output file: \n ", data_file.read())



with open(data_file_name) as json_file:
    data = json.load(json_file)
    pretty = json.dumps(data, indent=4, ensure_ascii=False)
    print("\n Pretty print out output file: \n")
    print(pretty)
