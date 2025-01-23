# GROUND CONTROL YELLOW
from microbit import *
import radio
"""
"The reset button on the microbit inside the rocket should not be pressed during the recording phase; 
It will delete the data and will not restart the recording, rendering the flight useless.
To prevent this, we covered the reset button with a styrofoam cutout perfectly covering the button and 
finely taping it. Buttons A and B on the microbit in the rocket don't need to be covered, as they do not do 
anything. Same goes for the PUSH-Button.
To measure the altitude we soldered a BMP180 adafruit preassure sensore to the microbit and used @shaoziyang 's 
GitHub repository as code-base.
A 3.70 V, 150mA battery pack was also taped to the microbit. BE SURE THE BATTERY IS POWERED AN THE MICROBIT'S LIGTH IS ON,
SO THAT DURING THE RECORDING THE MICROBIT DOESN'T SUDDENLY LOSE POWER. (subtle hinting as to what happened to us once :) )

The other Microbit was connected to my laptop near the rocket launch site. 
"""
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
