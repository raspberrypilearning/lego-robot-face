## Add the Raspberry Pi

For this project you'll ideally want to use the Build Plate element to mount your Raspberry Pi and Build HAT:

![Image showing a magenta LEGO® build plate.](images/build_10.png)

--- task ---

Mount your Raspberry Pi onto the Build Plate using M2 bolts and nuts, making sure the Pi is on the flat side:

 ![Raspberry Pi bolted to a magenta LEGO® build plate.](images/build_11.jpg)

--- /task ---

Mounting the Raspberry Pi this way round enables easy access to the ports as well as the SD card slot.

### Mount the camera and Build HAT

Before adding the Build HAT, you'll first need to attach the camera ribbon cable to the Raspberry Pi and thread it through the hole in the Build HAT. If you haven't already connected the camera board to your Raspberry Pi, you can do so by following these instructions: [Getting started with the Camera Module](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera){:target="_blank"}.

![Animation showing the Raspberry Pi Camera Module being connected to the Raspberry Pi.](images/connect-camera.gif)

--- task ---

Leave the camera ribbon connected to the Raspberry Pi, but remove the camera board from the loose end of the ribbon by pushing up the small black clip and sliding the ribbon out:

![Image showing the rear of the camera board with closed clip.](images/build_12.jpg)

![Image showing the rear of the camera board with open clip and ribbon removed.](images/build_13.jpg)

--- /task ---

--- task ---

Poke the ribbon through the underside of the Build HAT and out through the top, making sure the ribbon isn't twisted: ![Image of the Picamera ribbon poking through the top of the Build HAT.](images/build_14.jpg)

--- /task ---

--- task ---

Line up the Build HAT with the Raspberry Pi, ensuring you can see the `This way up` label. Make sure all the GPIO pins are covered by the HAT, and press down firmly. (The example uses a [stacking header](https://www.adafruit.com/product/2223){:target="_blank"}, which makes the pins longer.)

![Image of GPIO pins poking through the top of the Build HAT.](images/build_15.jpg)

--- /task ---

--- task --- Re-attach the camera to the end of the ribbon cable, making sure it isn't twisted.

![Image of the Picamera attached to the ribbon cable.](images/build_16.jpg)

--- /task ---

--- task --- Connect the Build Plate to the back of your robot face using some black studs. ![Image of a Maker Plate and Raspberry Pi connected to the rear of the robot face.](images/build_17.jpg)

Mounting the Raspberry Pi this way gives the best access to ports and pins, and means your barrel jack is easily connected to power the robot face.

--- /task ---

--- task ---

Connect up your small LEGO® Technic™ motors to ports A and B, ready to control the mouth.

![Image of two small LEGO® Technic™ motors connected to ports A and B on the Build HAT.](images/build_18.jpg)

--- /task ---

--- task ---

Connect up your large LEGO® Technic™ motor to port C, ready to control the eyebrows.

![Image showing a large LEGO® Technic™ motor connected to port C on the Build HAT.](images/build_19.jpg)

--- /task ---

--- task ---

Using the adhesive pad on the bottom, stick a breadboard to the top of the frame that supports the large LEGO® motor.

![Image showing a breadboard stuck to the top of the robot face mechanism.](images/build_20.jpg)

--- /task ---

--- task ---

Mount the camera board in the holder on the top of the robot face by passing the ribbon under the holder and wedging the camra between the rubber stoppers on either side.

Secure the camera with an elastic band using the black lugs on either side.

![Image showing the camera board mounted using elastic bands, both front and rear.](images/build_21.jpg)

--- /task ---

To connect the pair of eyes to the Raspberry Pi GPIO, they first need to be connected together using a breadboard, and then to the GPIO pins from the breadboard.

--- task ---

Use eight male–female jumper wires to connect the four pins from each eye together on the breadboard. Make sure that both VCC pins are in the same row of the breadboard, both GND pins are in the same row, and so on. Then connect to the 3V3, GND, SDA, and SCL pins on the Raspberry Pi, as shown below.

![I2C diagram.](images/eye_wiring.png)

--- /task ---

Your robot face is now built, connected, and ready to be programmed!





