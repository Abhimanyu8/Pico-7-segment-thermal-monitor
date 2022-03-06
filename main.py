#      ___                    ___     
#     /\  \                  /\  \    
#    /::\  \                /::\  \   
#   /:/\:\  \              /:/\:\  \  
#  /::\~\:\  \            /:/  \:\__\ 
# /:/\:\ \:\__\          /:/__/ \:|__|
# \/__\:\/:/  /          \:\  \ /:/  /
#      \::/  /            \:\  /:/  / 
#      /:/  /              \:\/:/  /  
#     /:/  /                \::/__/   
#     \/__/                  ~~       
# Author: Avimanyu Dutta
# Date: Mar 06th, 2022
# Version: 0.6

# Import required libraries
from machine import Pin
import utime

#wire button to this pin
button = Pin(6, Pin.IN, Pin.PULL_DOWN)

#temperature sensor maths
sensor_temp = machine.ADC(4)
conversion_factor = 3.3/(65535)

# define GP ports to use , connect the displays parallely 
# Pins Matching: A, B, C, D, E, F, G
display_list = [18,19,13,14,15,17,16]
display_list2 = [18,19,13,14,15,17,16]
dotPin=12
display_obj = []

# Set all pins as output
for seg in display_list2:
    display_obj.append(Pin(seg, Pin.PULL_DOWN))
    
for seg in display_list:
    display_obj.append(Pin(seg, Pin.OUT))

dot_obj=Pin(dotPin, Pin.OUT)

# DIGIT map as array of array
arrSeg = [[1,1,1,1,1,1,0],\
          [0,1,1,0,0,0,0],\
          [1,1,0,1,1,0,1],\
          [1,1,1,1,0,0,1],\
          [0,1,1,0,0,1,1],\
          [1,0,1,1,0,1,1],\
          [1,0,1,1,1,1,1],\
          [1,1,1,0,0,0,0],\
          [1,1,1,1,1,1,1],\
          [1,1,1,1,0,1,1]]

arrSeg2 = [[0,0,0,0,0,0,1],\
          [1,0,0,1,1,1,1],\
          [0,0,1,0,0,1,0],\
          [0,0,0,0,1,1,0],\
          [1,0,0,1,1,0,0],\
          [0,1,0,0,1,0,0],\
          [0,1,0,0,0,0,0],\
          [0,0,0,1,1,1,1],\
          [0,0,0,0,0,0,0],\
          [0,0,0,0,1,0,0]]


def SegDisplay(toDisplay):
    numDisplay = int(toDisplay.replace(".", ""))
    for a in range(7):
        display_obj[a].value(arrSeg[numDisplay][a])
    # Manage DOT activation
    if toDisplay.count(".") == 1:
        dot_obj.value(1)
    else:
        dot_obj.value(0)
        
def SegDisplay2(toDisplay):
    numDisplay = int(toDisplay.replace(".", ""))
    for a in range(7):
        display_obj[a].value(arrSeg2[numDisplay][a])
    # Manage DOT activation
    if toDisplay.count(".") == 1:
        dot_obj.value(1)
    else:
        dot_obj.value(0)

#Main code -------------------------------------------------------------------------------
while True:
     if button.value():
        # reading the temperature value
        reading = sensor_temp.read_u16() * conversion_factor
        temperature = 27-(reading - 0.706)/0.001721
        print(temperature,"°C")

        #taking out the 10's place to display
        ten =int((temperature // 10))
        
        #taking out the 1's place
        one = int((temperature % 10))

        SegDisplay(str(ten))
        utime.sleep(1)
        SegDisplay2(str(one))
        utime.sleep(1)
        SegDisplay2('0')#sleep message


  
        
