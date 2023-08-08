import serial
from modbus_tk import modbus_rtu
import modbus_tk.defines as cst
from time import sleep

PORT = "COM2"

def settingup():
    master = modbus_rtu.RtuMaster(serial.Serial(port=PORT,baudrate=9600,bytesize=8,parity="N",stopbits=1))
    master.set_timeout(5,0)
    master.set_verbose(True)
    return master
def servoOn(master):
    master.execute(2,cst.WRITE_MULTIPLE_REGISTERS,0X2042,1,[1]) # master.execute(2,cst.READ_HOLDING_REGISTERS,0X100C,1)
    print("SERVO ON\n")
def servoOff(master):
    master.execute(2,cst.WRITE_MULTIPLE_REGISTERS,0X2042,1,[0])
    print("SERVO OFF\n")
def initial(master):
    master.execute(2,cst.WRITE_MULTIPLE_REGISTERS,0X2041,1,[0])
    print("原點歸位中",end="")
    while master.execute(2,cst.READ_HOLDING_REGISTERS,0x1021,1)[0]!=1:
        print(".",end="")
        sleep(2)
    print("原點歸位完成！\n")
def designatedLocation(master):
    desloc=input("請輸入位置 -- ")
    try:
        float(desloc)
        print("你輸入的位置是："+desloc+"\n")
    except:
        print("輸入無效，請再試一次。\n")
        designatedLocation(master)
def closeup(master):
    master.close()
    print("Program terminated.")