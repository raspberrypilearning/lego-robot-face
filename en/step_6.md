## Adding the Raspberry Pi

For this project you'll ideally want to use the BBE element to mount your Raspberry Pi and Build Hat. For the example model a magenta beam was added to the BBE, this means it fits perfectly between the stands of the face.

--- task ---

Mount your Raspberry Pi to the Maker Plate using M2 bolts and nuts:

 ![Raspberry Pi bolted to a magenta LEGO build plate](images/build_11.jpg)

--- /task ---

Mounting the Raspberry Pi this way round enables easy access to the ports as well as the SD card slot.

### Mounting the camera and BuildHAT

Before adding the BuildHAT you'll first need to attach the camera ribbon cable to the Raspberry Pi and thread it through the hole in the build hat. If you haven't already connected the Camera board to your Pi, you can do so by following these instructions: [Getting started with the Camera Module](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera)

--- task ---
Leave the camera ribbon connected to the Pi, but remove the camera board from the loose end of the ribbon by pushing up the small black clip and sliding the ribbon out:

![Image showing rear of camera board with closed clip](images/build_12.jpg)

![Image showing rear of camera board with open clip and ribbon removed](images/build_13.jpg)

--- /task ---

--- task ---

Poke the ribbon through the underside of the buildHAT and out through the top, keeping it straight:
![Image of picamera ribbon poking through the top of the buildHAT](images/build_14.jpg)

--- /task ---

--- task ---

Line up the BuildHAT making sure all the GPIO pins are covered, and press down firmly. (The example uses a [stacking header](https://www.adafruit.com/product/2223){:target="_blank"} which makes the pins longer.)

![Image of GPIO pins poking through the top of the buildHAT](images/build_15.jpg)

--- /task ---

--- task ---
Re-attach the camera to the end of the ribbon cable, making sure it is straight. 

![Image of picamera attached to ribbon cable.](images/build_16.jpg)

--- /task ---

--- task ---
Connect the Maker Plate to the back of your robot face using some black studs.
![Image of Maker plate and raspberry pi connected to the rear of the robot face.](images/build_17.jpg)

Mounting the Raspberry Pi this way gives the best access to ports and pins, and means your barrel jack is easily connected for powering the robot face. 

--- /task ---

--- task ---

Connect up your small LEGO Spike motors to ports A and B, ready to control the mouth.

![Image of small LEGO Spike motors to ports A and B on buildHAT](images/build_18.jpg)

--- /task ---

--- task ---

Connect up your large LEGO motor to port C, ready to control the eyebrows.

![Image showing large LEGO motor connected to port C on buildHAT](images/build_19.jpg)

--- /task ---

--- task ---

Using the adhesive pad on the bottom, stick a breadboard to the top of the frame supporting the large LEGO motor.

![Image showing breadboard stuck to the top of the robot face mechanism](images/build_20.jpg)

--- /task ---

--- task ---

Mount the camera board in the holder on the top of the robot face, by passing the ribbon under the holder and wedging it between the rubber stoppers on either side. 
Secure it with an elastic band using the black lugs either side. 

![Image showing camera board mounted using elastic bands, both front and rear.](images/build_21.jpg)

--- /task ---

To connect the pair of eyes the the Raspberry Pi GPIO they first need to be connected together using a breadboard and then to the GPIO pins from the Breadboard.

--- task ---

Use 8 Male-Female jumper wires to connect the 4 pins from each eye together on the breadboard. Make sure that both VCC pins are in the same row of the breadboard, both GND pins are in the same row and so on. 

![I2C Diagram](images/breadboard_pins.jpg)

--- /task ---

--- task ---

Using 4 more Male-Female wires connect the 4 pins from the boards to the following GPIO pins on the Build Hat.

- **VCC** to pin **5V**
- **GND** to pin **GND**
- **SDA** to pin **2**
- **SCL** to pin **3**

![I2C Diagram](images/gpio_pins.jpg)
--- /task ---

Your robot face is now built, connected and ready to be programmed!





