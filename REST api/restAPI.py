import requests
import urllib3
import json
import sys

PLCnext = requests.Session()

DO1 = False
DO2 = False
DO3 = False
DO4 = False
DO5 = False
DO6 = False
DO7 = False
DO8 = False
DO9 = False
DO10 = False
DO11 = False
DO12 = False
DO13 = False
DO14 = False
DO15 = False
DO16 = False


def Pullloop():
    data = PLCnext.request('GET',
                           'https://localhost/_pxc_api/api/variables/?pathPrefix=Arp.Plc.Eclr/&paths=DI1,DI2,DI3,DI4,DI5,DI6,DI7,DI8,DI9,DI10,DI11,DI12,DI13,DI14,DI15,DI16,tCycle',
                           verify=False)
    parsed = json.loads(data.content)
    input1 = parsed['variables'][0]['value']
    input2 = parsed['variables'][1]['value']
    input3 = parsed['variables'][2]['value']
    input4 = parsed['variables'][3]['value']
    input5 = parsed['variables'][4]['value']
    input6 = parsed['variables'][5]['value']
    input7 = parsed['variables'][6]['value']
    input8 = parsed['variables'][7]['value']
    input9 = parsed['variables'][8]['value']
    input10 = parsed['variables'][9]['value']
    input11 = parsed['variables'][10]['value']
    input12 = parsed['variables'][11]['value']
    input13 = parsed['variables'][12]['value']
    input14 = parsed['variables'][13]['value']
    input15 = parsed['variables'][14]['value']
    input16 = parsed['variables'][15]['value']
    cycleTime = parsed['variables'][16]['value']

    return input1, input2, input3, input4, input5, input6, input7, input8, input9, input10, input11, input12, input13, input14, input15, input16, cycleTime


def Postloop(O1, O2, O3, O4, O5, O6, O7, O8, O9, O10, O11, O12, O13, O14, O15, O16):
    suburl = "/_pxc_api/api/variables/"
    URL = "https://192.168.1.10" + suburl
    header = {
        "Content-Type": "application/json;charset=UTF-8"
    }
    payload = {
        "pathPrefix": "Arp.Plc.Eclr/",
        "variables": [
            {"path": "DO1",
             "value": O1,
             "valueType": "Constant"
             },
            {"path": "DO2",
             "value": O2,
             "valueType": "Constant"
             },
            {"path": "DO3",
             "value": O3,
             "valueType": "Constant"
             },
            {"path": "DO4",
             "value": O4,
             "valueType": "Constant"
             },
            {"path": "DO5",
             "value": O5,
             "valueType": "Constant"
             },
            {"path": "DO6",
             "value": O6,
             "valueType": "Constant"
             },
            {"path": "DO7",
             "value": O7,
             "valueType": "Constant"
             },
            {"path": "DO8",
             "value": O8,
             "valueType": "Constant"
             },
            {"path": "DO9",
             "value": O9,
             "valueType": "Constant"
             },
            {"path": "DO10",
             "value": O10,
             "valueType": "Constant"
             },
            {"path": "DO11",
             "value": O11,
             "valueType": "Constant"
             },
            {"path": "DO12",
             "value": O12,
             "valueType": "Constant"
             },
            {"path": "DO13",
             "value": O13,
             "valueType": "Constant"
             },
            {"path": "DO14",
             "value": O14,
             "valueType": "Constant"
             },
            {"path": "DO15",
             "value": O15,
             "valueType": "Constant"
             },
            {"path": "DO16",
             "value": O16,
             "valueType": "Constant"
             }
        ]
    }

    PLCnext.put(
        URL,
        headers=header,
        data=json.dumps(payload),
        verify=False
    )


i = 1
currentI = 1
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
try:
    print("Press Ctrl+C to stop the script.")
    while 1:
        DI = Pullloop()
        if DO1:
            print("Cycle time is " + str(DI[16]/1000) + " seconds.")
        if DI[0]:
            if (currentI != i) and not(DO1 or DO2 or DO3 or DO4 or DO5 or DO6 or DO7 or DO8 or DO9 or DO10 or DO11 or DO12 or DO13 or DO13 or DO13 or DO14 or DO15 or DO16):
                DO1 = True
            if (currentI != i) and DO1:
                DO1 = False
                DO2 = True
                currentI = i
            if (currentI != i) and DO2:
                DO2 = False
                DO3 = True
                currentI = i
            if (currentI != i) and DO3:
                DO3 = False
                DO4 = True
                currentI = i
            if (currentI != i) and DO4:
                DO4 = False
                DO5 = True
                currentI = i
            if (currentI != i) and DO5:
                DO5 = False
                DO6 = True
                currentI = i
            if (currentI != i) and DO6:
                DO6 = False
                DO7 = True
                currentI = i
            if (currentI != i) and DO7:
                DO7 = False
                DO8 = True
                currentI = i
            if (currentI != i) and DO8:
                DO8 = False
                DO9 = True
                currentI = i
            if (currentI != i) and DO9:
                DO9 = False
                DO10 = True
                currentI = i
            if (currentI != i) and DO10:
                DO10 = False
                DO11 = True
                currentI = i
            if (currentI != i) and DO11:
                DO11 = False
                DO12 = True
                currentI = i
            if (currentI != i) and DO12:
                DO12 = False
                DO13 = True
                currentI = i
            if (currentI != i) and DO13:
                DO13 = False
                DO14 = True
                currentI = i
            if (currentI != i) and DO14:
                DO14 = False
                DO15 = True
                currentI = i
            if (currentI != i) and DO15:
                DO15 = False
                DO16 = True
                currentI = i
            if (currentI != i) and DO16:
                DO16 = False
                DO1 = True
                currentI = i
        else:
            DO1 = False
        Postloop(DO1, DO2, DO3, DO4, DO5, DO6, DO7, DO8, DO9, DO10, DO11, DO12, DO13, DO14, DO15, DO16)
        i += 1
except KeyboardInterrupt:
    sys.exit()
