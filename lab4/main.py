import json

f = open("data.json")

data = json.load(f)

print("Interface Status")
print("=" * 90)
print("{:<50} {:<20} {:<10} {:<10}".format("DN", "Description", "Speed", "MTU"))
print("-" * 90)


for i in data['imdata']:
    attributes = i['l1PhysIf']['attributes']
    dn = attributes['dn']
    description = attributes.get('descr', '')
    speed = attributes.get('speed', 'inherit')
    mtu = attributes.get('mtu', 'inherit')
    print("{:<50} {:<20} {:<10} {:<10}".format(dn, description, speed, mtu))
