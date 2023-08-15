import serial
from modbus_tk import modbus_rtu
import modbus_tk.defines as cst
from time import sleep

PORT = "COM2"

def settingup():
    return "SETUP done"
def servoOn(master):
    print("SERVO ON\n")
def servoOff(master):
    print("SERVO OFF\n")
def initial(master):
    print("原點歸位中",end="")

    for i in range(0,3):
        print(".",end="")
        sleep(2)
    print("\n原點歸位完成！\n")
def designatedLocation(master,desloc):
    try:
        desloc=float(desloc)
        desloc*=100
        print("你輸入的位置是：",desloc,"pulse\n")
        return 0
    except:
        print("輸入無效，請再試一次。\n")
        return "error"
def readCurrentLocation(master):
    print("讀取完成，目前位置...\n")
def closeup(master):
    print("若未SERVO OFF，已自動處理完畢。")
    print("Program terminated.")