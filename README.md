# Waterpowered-Rocket

Schoolproject from the 20th to the 24th of January 2025 (Monday to Friday 8:00 AM to 3:00 PM).

**Task:** Study the basic physics behind a rocket and build a functioning water rocket. Collect and analyse data using a microbit.

**Goal:** Understand the principles of momentum and learn to correctly analyse data.

## **Instructions:**

### Material

- 2x 1.5 litre PET Bottles
- 1 Gardena to PET-lid adapter
- 1 Bicycle pump
- garden hose
- plenty of sticky tape
- waterproof tape
- 2 microbits
- 3.70V 150mAh battery with microbit adapter
- bmp180 Altimeter
- wooden contraption with rope to release garden hose from rocket (acting as a launch pad)
- wool, cloth, styrofoam or some other soft material to polster the module in which the microbit is placed
- some string
- a parachute (made or bought; we used an umbrella top)

### **Steps:**

#### **Building the rocket:**

First we took one bottle and added the special bottle-lid-to-hose translator to it to act as the nozzle. Then we cut off the top part and the bottom part of the second bottle so we were left with a tube. The parachute's eight ends were then connected to one. Then we connected two strings to the part where all eight parachute strings came together. One of the strings we tightly knotted around the nozzle, and the other string we stuck to the inside of the parachute-container. Finally we used the cutoff top of the second bottle and filled it with wool and cutout styrofoam and hotglue to make a kind of bed for the microbit. This bottle top also had a little hole where we could feed the altitude measurement device through and stick it to the outside of this top compartment. Once the "Launcher" microbit had been placed accordingly with a battery and code, we made sure the microbit couldn't fall out, then we stuck this "cockpit" onto one end of the parachute tube and taped them together.
That's it for the actual rocket!

The second microbit, the "ground_control", was connected to my laptop and held in my hand near the actual launch sight, so that I could make sure that the microbit in the rocket was actually recording data.

#### **Further information:**

The reset button on the microbit inside the rocket should not be pressed during the recording phase; It will delete the data and will not restart the recording, rendering the flight useless.
To prevent this, we covered the reset button with a styrofoam cutout perfectly covering the button and
finely taping it. Buttons A and B on the microbit in the rocket didn't need to be covered, as they do not do anything. Same goes for the PUSH-Button.

To the power supply: BE SURE THE BATTERY IS POWERED AN THE MICROBIT'S LIGHT IS ON, SO THAT DURING THE RECORDING THE MICROBIT DOESN'T SUDDENLY LOSE POWER AND STOP RECORDING. (subtle hinting as to what had happened to us once)

To the parachute: To make the parachute works as successfully as possible we only placed the parachute compartment onto the fuel take. No tape and no pushing it in! You could almost say we layed it ontop or balanced it there.

### **Launching the rocket:**

The rocket would release by itself at around 7.5 bar of pressure applied from the bike pump. Otherwise we just manually pulled at a string that released the hose from the nozzle. We used a string to have some distance from the water spray, as we did this in January and none of us wanted to get very wet. Anything below 2 bar and the rocket would barely take off.
We made sure to add some extra tape around the rocket so that we could add a little extra preassure in there without it exploding.
At the top of the rocket flight parabola the parachute compartment would just fall off due to it just being placed on top without any sort of fastening. This is ideal and since the parachute was connected to its own tube with the microbit compartment AND the then empty fuel tank nothing would crash land and everything would safely glide down to earth.

<video controls src="slow_mo_close_shot.MP4" title="Title"></video>

slow_mo_close_shot.MP4

Contributers: github.com/jostoelz, +2
bmp180 for the microbit: code from github.com/shaoziyang
