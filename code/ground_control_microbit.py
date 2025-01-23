# GROUND CONTROL YELLOW
from microbit import *
import radio
"""
Contributers: @jostoelz, +2 

The reset button on the microbit inside the rocket should not be pressed during the recording phase; 
It will delete the data and will not restart the recording, rendering the flight useless.
To prevent this, we covered the reset button with a styrofoam cutout perfectly covering the button and 
finely taping it. Buttons A and B on the microbit in the rocket don't need to be covered, as they do not do 
anything. Same goes for the PUSH-Button.
To measure the altitude we soldered a BMP180 adafruit preassure sensore to the microbit and used @shaoziyang 's 
GitHub repository as code-base.
A 3.70 V, 150mA battery pack was also taped to the microbit. BE SURE THE BATTERY IS POWERED AN THE MICROBIT'S LIGTH IS ON,
SO THAT DURING THE RECORDING THE MICROBIT DOESN'T SUDDENLY LOSE POWER AND STOP RECORDING. (subtle hinting as to what happened to us once :) )
The other Microbit was connected to my laptop near the rocket launch site which was held in my hand. 


The Rocket and launch station:

The rocket was made by simply adding a garden-hose-to-bottle-lid-translator-object to act as a nozzle. 
The 1.5 Litre bottle was then filled up to about a third with water, the rest left with air. 
As seen on video launch1.MP4 the launch station is just a simple wooden contraption with a hose connected below,
into which the water-rocket's nozzle is placed. 
The other end of the hose is then connected to a bike pump. 
Our rocket would blast off by itself at about 7.5 bar. To ignite anything below that, a string connected to the wooden contraption can be pulled 
to release the hose from the nozzle maually. 
On top of the "fuel bottle" we just lightly placed (balanced) another cut-open bottle into which we carefully rolled up a parachute.
At the top of the flight-parabola, this balanced bottle fell off and automatically released the parachute, which worked surprisingly well!
Then above the parachute compartment we stuck the microbit-contraption as stated above.


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
