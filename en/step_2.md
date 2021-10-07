## Test the machine learning model

Your first step will be understand and test how we can use a machine learning model to recognise objects. For this project you won't be creating and training your own model but using an example model that can recognise a range of objects.

Before you begin, you'll need to have setup your Raspberry Pi Computer and connected A Raspberry Pi Camera. You can find instructions on how to do both in the following guides:

--- task ---
If you have not already done so, set up your new Raspberry Pi by following these instructions:

[Setting up your Pi](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up){:target="_blank"}
--- /task ---

--- task ---
Connect a Raspberry Pi Camera Module to your Raspberry Pi, by following these instructions:

[Getting started with the Camera Module](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera){:target="_blank"}

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Computers do not have a natural ability to learn. Most things that computers do have been <span style="color: #0faeb0">directly programmed by a human</span>. These make them great for tasks that have a few clearly defined rules, but they struggle with more human-like tasks such as recognising different objects.

Using machine learning, a computer can be shown thousands and thousands of images each of which has a label. Gradually the program can learn the characteristics of a group of images and then give them the correct label.

The end result of this process is called a <span style="color: #0faeb0">model</span>. Once trained, models can be used in the real world to perform tasks. 
</p>

### Testing a model

--- task ---

 To get started, download the resources for this project to your Raspberry Pi [by clicking here](http://rpf.io/p/en/robot-face-go){:target="_blank"}.

 --- /task ---
 
 --- task ---
 
 Unzip the files and then move the unzipped directory to your `/home/pi` directory.
 
 --- /task ---
 
 You'll find a range of files that will be useful for the project, but for this step we're going to use:

 - `model.tflite` - The machine learning model file.
 - `labels.txt` - Labels for each object the model can recognise
 - `classifer.py` - A python program to test the model

--- task ---

Open Thonny (under Programming) in your Raspberry Pi start Menu. 
 
 --- /task ---

--- task ---

Open and Run the `classifier.py` program. 

The Pi will display: 
+ what the camera is "seeing", 
+ the name of the main object in view that it recognises

 ![Image of recogniser project running](images/classifier.png)

--- /task ---

--- task ---

 **Try** presenting the camera with different objects and investigate which ones it can recognise with confidence. 
 
 Whilst doing this, experiment with:
   - **The background** -  the camera may recognise objects instead of the object you are holding in front of the camera.
   - **Object position** - where and how you hold the object may effect how well it is recognised, experiment with the distance from the camera and turn it in different directions.
   - **Lighting** - the lighting in your room may effect how well an object is detected. Try turning on more lights, or turning some lights off.
   - **Images** - You may find it helpful to show the camera printed images of objects rather than the object themselves.

--- /task ---

--- task ---

Find **at least** 5 objects (or images) that your camera can recognise reliably - you'll need them for your machine learning model.

--- /task ---

--- save ---