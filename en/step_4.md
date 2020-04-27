# Making a face

Now that we know which object will trigger whgich responses we need robotic face to animate them with. In this step we're going to walk through an example model, but you should adapt to suit your needs, available resources and ideas.

## Equipment 
For the project your going to need:

- 2 Lego "Powered up" Motors to change the mouth
- A flexible element for the mouth itself
- 2 LED matrix boards (or similar) to display the eyes.
- Raspberry Pi Camera
- Assortment of Lego elements to constuct the face itself.

1. Our first step was to build the main part of the face for which we used 2 panel plates, connected with a series of pins.

  ![Image of step 1](images/build_01.jpg)

2. Next some horizontal supports were added to help the face stand up. Here some technic panels were used but, beams or frames would have worked just as well.

  ![Image of step 2](images/build_02.jpg)

  ![step 2 alternatives](images/build_02a.jpg)

3. Two small motors were added to the rear of the model to control the corners of the mouth. Importantly for the next step the motors' position was set to 0.

  ![Image of step 3](images//build_03.jpg)

4. Round the front of the model short axles were attached to 90&deg connectors before being joined with a flexible hose and then mounted in the motors holes.

  ![Image of step 4](images/build_04.jpg)

  ![Image of step 4](images/build_05.jpg)

5. Next for the eyes a pair of 8x8 LED matrices were used. The 4 connection pins were carefuly bent to 90&deg and then both mounted to the face using 4 double length connector pegs and a pair of 3x5 L shaped beams.

  ![Image of step 4](images/build_06.jpg)

  ![Image of step 4](images/build_07.jpg)

6. To mount the Raspberry Pi Camera in the model a custom Lego compatible [part](https://www.thingiverse.com/thing:3273396) was found and 3D printed.  

  ![Image of step 4](images/build_08.jpg)

  This could then be mounted on top of the Lego face

  ![Image of step 4](images/build_09.jpg)

  ![Image of step 4](images/build_10.jpg)

This completes the construction of our example face model, however you may wish to add other features suchs a ears, a nose or hair. There are also many other materials you might use including cardboard, paper, string, tape etc.

In the next step we'll connect up each component of the face to the Raspberry Pi computer and build hat.
