# GROUND CONTROL YELLOW
from microbit import *
import radio

radio.config(group=7, power=7)
radio.on()

while True:
    if button_a.get_presses():
        radio.send("BLASTOFF") #press before launch to start recording data 
        print("blastoff sent")
        display.show(Image.HAPPY)
        sleep(100)
        display.clear()
    elif button_b.get_presses():
        radio.send("MAYDAY") #press after landing to signal to stop recording data
        print("mayday sent")
        display.show(Image.ANGRY)
        sleep(100)
        display.clear()
    else:
        pass
    received = radio.receive()
    if received:
        data = received.split(";")
        display.show(Image.HEART)
        print(data)
        display.clear()
