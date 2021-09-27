### Adding the eyes

The LED matrices used in the example face connect to the Raspberry pi using 4 common GPIO pins and communicate using a protocol call I2C. Before you connect them up you likely need to follow relevant [assembly instructions](https://learn.adafruit.com/adafruit-led-backpack/0-8-8x8-matrix-assembly)

Devices using I2C are connected in a line or **bus** and all instructions from the Raspberry Pi are transmitted along the whole bus. For the Raspberry Pi to communicate with the correct device, each is given an address. Each message is sent with an address meaning that each device only responds to instructions matching it's own address. 

![I2C Diagram](images/i2c.jpg)

However the matrices used in this project all come with the same I2C address, meaning that for 2 to work together, one of them needs a new address. For this some soldering is needed.

![Image of soldered / unsoldered board](images/soldering.jpg)

In this image the brand new board on the left has a default I2C address of *0x70* whilst the board on the right, with the A0 connection soldered, has the address *0x71*. To add up to 4 of these matrices you would solder connectors A1 (address 0x72) or A2 (address 0x73).

An additional step taken for the example model was to carefuly bend the header pins by 90&deg to make them easier to connect to and fit within the model.

![I2C Diagram](images/led_pins.jpg)


## Connecting the GPIO

To connect the pair of eyes the the Raspberry Pi GPIO they first need to be connected together using a breadboard and then to the GPIO pins from the Breadboard.

Use 8 Male-Female jumper wires to connect the 4 pins from each eye together on the breadboard, matching up each pin with its equivilant pin from the other board.

![I2C Diagram](images/breadboard_pins.jpg)

Using 4 more Male-Female wires connect the 4 pins from the boards to the following GPIO pins on the Build Hat.

- **VCC** to pin **5V**
- **GND** to pin **GND**
- **SDA** to pin **2**
- **SCL** to pin **3**

![I2C Diagram](images/gpio_pins.jpg)

Once wired, the breadboard could either be let loose, connected using some additional Lego or even stuck using the self adhesive pad.

![I2C Diagram](images/stick_breadboard.jpg)

Your now ready to insert your SD card, connect up your Raspberry Pi and begin programming your face.






