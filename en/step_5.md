## Adding the eyes

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">The LED matrices used in the example face connect to the Raspberry pi using 4 common GPIO pins and communicate using a protocol called <span style="color: #0faeb0">I2C</span>. Devices using I2C are connected in a line or <span style="color: #0faeb0">bus</span> and all instructions from the Raspberry Pi are transmitted along the whole bus. For the Raspberry Pi to communicate with the correct device, each is given an address. Each message is sent with an address meaning that each device only responds to instructions matching it's own address. </p>

--- task ---

Before you connect them up you need to follow the relevant [assembly instructions](https://learn.adafruit.com/adafruit-led-backpack/0-8-8x8-matrix-assembly){:target="_blank"}. Assembly of the LED arrays requires some soldering, so get permission from an adult before you use any tools. 

--- /task ---


![I2C Diagram](images/i2c.jpg)

However the matrices used in this project all come with the same I2C address, meaning that for 2 to work together, one of them needs a new address. For this some soldering is needed.

--- task ---

Using your soldering kit, close the `A0` connection of **only one** of your matrices.

![Image of soldered / unsoldered board](images/soldering.jpg)

--- /task ---

--- task ---
Place the eyes into the square sockets on your robot face, making sure the pins are at the top.

![Image showing 8 by 8 arrays mounted in lego face](images/array_eyes.jpg)

--- /task ---

Now that the basic construction of the robot face is complete we need to add the Raspberry Pi Computer and connect our components to it.