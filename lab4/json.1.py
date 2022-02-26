import json
f = open('sample-data.json')
data = json.load(f)
print("Interface Status")
print('========================================================================')
print('DN                                          Description    Speed    MTU')
print('------------------------------------------  -------------  -------  ----')
for i in data['imdata']:
    s = str(i['l1PhysIf']['attributes']['dn'])
    print(s, end = " ")
    if len(s) == 41:
        print(" ", end = "") 
    t = str(i['l1PhysIf']['attributes']['descr'])
    print(t, end = "")
    if len(t) == 0:
        print("                ", end = "")
    print(i['l1PhysIf']['attributes']['speed'], "", i['l1PhysIf']['attributes']['mtu'])
f.close()