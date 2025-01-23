# GROUND CONTROL YELLOW
from microbit import *
import radio

#time config (with respect to launch time)
def fillup_string(s, n): #string s up to len n
    if len(s) == n :
        return s
    return (n - len(s)) * "0" + s
        
    
def time_as_string(n): #input millis as int
    millis_raw = int(n % 1000)
    secs_raw = int(((n - millis_raw) / 1000) % 60)
    mins_raw = int((((n - millis_raw) / 1000) - secs_raw) / 60)

    millis = fillup_string(str(millis_raw), 3)
    secs = fillup_string(str(secs_raw), 2)
    mins = fillup_string(str(mins_raw), 2)
    
    return mins + ":" + secs + ":" + millis



radio.config(group=7, power=7)
radio.on()

while True:
    if button_a.get_presses():
        radio.send("BLASTOFF") #press shortly before launch to start recording data 
        print("blastoff sent")
        display.show(Image.HAPPY)
        sleep(100)
        display.clear()
    elif button_b.get_presses():
        radio.send("MAYDAY") #press shortly before landing to signal to stop recording data
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
