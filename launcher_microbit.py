# THIS MICROBIT WILL BE LAUNCHED GREEN

from microbit import *
import radio
import time
import log
import math
import bmp180

b = bmp180.BMP180()


#radio config 
radio.config(group=7, power=7)
radio.on()

accelerometer.set_range(8)

def log_one_row():
    now = time.ticks_ms()
    time_in_sec = now / 1000
    sleep(10)

    # now all in m/s^2, not in milli-g's
    accel_x = accelerometer.get_x() * 9.81 / 1000
    accel_y = accelerometer.get_y() * 9.81 / 1000
    accel_z = accelerometer.get_z() * 9.81 / 1000
    accelleration = math.sqrt(accel_x ** 2 + accel_y ** 2 + accel_z ** 2)

    #in milli Teslas
    magnet_strength_x = compass.get_x() / 1000000
    magnet_strength_y = compass.get_y() / 1000000
    magnet_strength_z = compass.get_z() / 1000000
    magnet_strength_total = math.sqrt(magnet_strength_x ** 2 + magnet_strength_y ** 2 + magnet_strength_z ** 2)
    
    alt = (b.Altitude())

    temp = temperature()
    
    # format: TIME, total_accel, accel_x, accel_y, accel_z, temperature
    try:
        row = {
            "time":time_in_sec,
            "accelleration":accelleration,
            "x_accelleration":accel_x,
            "y_accelleration":accel_y,
            "z_accelleration":accel_z,
            "temperature":temp,
            "x_magnet_strength":magnet_strength_x,
            "y_magnet_strength":magnet_strength_y,
            "z_magnet_strength":magnet_strength_z,
            "total_magnet_strength":magnet_strength_total,
            "altitude":alt
        }
        log.add(row)
        print(alt)
    except Exception  as e:
        print (e)
        row = {"time":time_in_sec,
               "accelleration":0,
               "x_accelleration":0,
               "y_accelleration":0,
               "z_accelleration":0,
               "temperature":0,
               "x_magnet_strength":0,
               "y_magnet_strength":0,
               "z_magnet_strength":0,
               "total_magnet_strength":0,
               "altitude":0
              }
        log.add(row)
        

blastoff = False
mayday = False
while True:
    received = radio.receive()
    if received:
        if received == "BLASTOFF" and blastoff == False:
            print("blastoff")
            radio.send("blastoff commenced")
            blastoff = True
            log.delete()
            log.set_labels("time", 
                           "accelleration", 
                           "x_accelleration", 
                           "y_accelleration", 
                           "z_accelleration",
                           "temperature",
                           "x_magnet_strength",
                           "y_magnet_strength",
                           "z_magnet_strength",
                           "total_magnet_strength",
                           "altitude",
                           timestamp=log.MILLISECONDS
                          )
            while True:
                received = radio.receive()
                if received == "MAYDAY" and blastoff == True:
                    print("mayday")
                    mayday = True
                    blastoff = False

                    try:
                        print("DONE")
                        radio.send("Recording complete")
                        break
                    except:
                        radio.send("Recording fatal")
                        break

                log_one_row()
                    
               
        
