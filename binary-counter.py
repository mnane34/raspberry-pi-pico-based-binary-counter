# Binary Counter


# Module Definition
import machine
import utime


# Pin Definition
increaseButton = 15
decreaseButton = 14
resetButton = 13
dataBit0 = 16
dataBit1 = 17
dataBit2 = 18
dataBit3 = 19


# Configration Definition
Bit0 = machine.Pin(dataBit0,machine.Pin.OUT) 
Bit1 = machine.Pin(dataBit1,machine.Pin.OUT)
Bit2 = machine.Pin(dataBit2,machine.Pin.OUT)
Bit3 = machine.Pin(dataBit3,machine.Pin.OUT)

Bit0.value(0)
Bit1.value(0)
Bit2.value(0)
Bit3.value(0)

upButton = machine.Pin(increaseButton,machine.Pin.IN,machine.Pin.PULL_DOWN)  
downButton = machine.Pin(decreaseButton,machine.Pin.IN,machine.Pin.PULL_DOWN)
zeroButton = machine.Pin(resetButton,machine.Pin.IN,machine.Pin.PULL_DOWN)


# Veriables Definition
Count = 0
arcDelay = 0.01
logicHigh = 1
logicLow = 0


# Function Definiton
def showDigits(desimalCount):
    binaryCount=[0,0,0,0]
    for loop in range(0,4):
        binaryCount[loop]=int(desimalCount%2);    
        desimalCount=desimalCount/2;
        
    Bit0.value(int(binaryCount[0]))
    Bit1.value(int(binaryCount[1]))
    Bit2.value(int(binaryCount[2]))
    Bit3.value(int(binaryCount[3]))


# İnfinity Loop Definition
while True:
        if upButton.value() == logicHigh:
            while upButton.value() == logicHigh:
                utime.sleep(arcDelay)
            Count = Count + 1
            if Count==16:
                Count=15
            
        elif downButton.value() == logicHigh:
            while downButton.value() == logicHigh:
                utime.sleep(arcDelay)
            Count = Count - 1
            if Count== -1:
                Count=0
           
        elif zeroButton.value() == logicHigh:
            while zeroButton.value() == logicHigh:
                utime.sleep(arcDelay)         
            Count = 0
            
        showDigits(Count)
  