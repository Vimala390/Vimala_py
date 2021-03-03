#JSON is less verbose compare to XML and XML parsing can take long time compare to JSON
# JSON structure is readable and uses map data structure i.e. key value pair and easy to undestand

import json

people_string = '''
{
    "people":[
        {
            "emp_name":"Vimala",
            "emp_phone":"1234",
            "emp_email":"vimalarevanuru@gmail.com"
        },
        
        {
            "emp_name":"Veera",
            "emp_phone":"4567",
            "emp_email":"veera@gmail.com"
        }
         
             ]
}
'''

data = json.loads(people_string)

#for i in data:
 #   print(i)

print(type(data['people']))

for person in data['people']:
    print(person['emp_name'],person['emp_email'])


sam_string = '''
{
    "totalCount": "400",
    "imdata": [
        {
            "l1PhysIf": {
                "attributes": {
                    "adminSt": "up",
                    "autoNeg": "on",
                    "brkoutMap": "none",
                    "bw": "0",
                    "childAction": "",
                    "delay": "1",
                    "descr": "",
                    "dn": "topology/pod-1/node-201/sys/phys-[eth1/33]",
                    "dot1qEtherType": "0x8100",
                    "ethpmCfgFailedBmp": "",
                    "ethpmCfgFailedTs": "00:00:00:00.000",
                    "ethpmCfgState": "0",
                    "fecMode": "inherit",
                    "id": "eth1/33",
                    "inhBw": "unspecified",
                    "layer": "Layer3",
                    "lcOwn": "local",
                    "linkDebounce": "100",
                    "linkLog": "default",
                    "mdix": "auto",
                    "medium": "broadcast",
                    "modTs": "2016-11-28T16:03:29.317-05:00",
                    "mode": "trunk",
                    "monPolDn": "uni/fabric/monfab-default",
                    "mtu": "9150",
                    "name": "",
                    "pathSDescr": "",
                    "portT": "fab",
                    "prioFlowCtrl": "auto",
                    "qiqL2ProtTunMask": "",
                    "routerMac": "not-applicable",
                    "snmpTrapSt": "enable",
                    "spanMode": "not-a-span-dest",
                    "speed": "inherit",
                    "status": "",
                    "switchingSt": "disabled",
                    "trunkLog": "default",
                    "usage": "fabric,fabric-ext"
                }
            }
        }
    ]
    }
    '''

data1 = json.loads(sam_string)
print(type(data1))

for req_data in data1['attributes']:
    print(req_data['dn'],req_data['speed']) 

#print(data1)