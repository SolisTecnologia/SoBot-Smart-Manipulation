import serial
import serial.tools.list_ports
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib_arm.DobotDllType import *


Desc_Dobot_serial = "Virtual COM Port - Hiker sudio"
ports = serial.tools.list_ports.comports()

for port in ports:
    # Check if the port description contains the device name
    if Desc_Dobot_serial in port.description:
        print(f"Device found: {port.device} - {port.description}")
        serial_Dobot = port.device
    else:
        print(f"Device '{Desc_Dobot_serial}' not found.")

CON_STR = {
    DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"
    }


#Load Dll
api = load()

#Connect Dobot
state = ConnectDobot(api, serial_Dobot, 115200)[0]
print("Connect status:",CON_STR[state])

if (state == DobotConnect.DobotConnect_NoError):

    #Set Home
    SetHOMEParams(api, 220, 0, 100, 0, isQueued = 1) 
    SetHOMECmd(api, temp = 0, isQueued = 1)

    while True:
        opc = input("Deseja coletar a posição ?")
        x,y,z,r,j1,j2,j3,j4 = GetPose(api)
        print('GetPose: X:%.4f Y:%.4f Z:%.4f R:%.4f J1:%.4f J2:%.4f J3:%.4f J4:%.4f' %(x,y,z,r,j1,j2,j3,j4))



