## Recognising Objects

Your first step will be understand and test how we can use a machine learning model to recognise objects. Before you begin you'll need to have setup your Raspberry Pi Computer and connected A Raspberry Pi Camera. You can find instructions on how to do both in the following guides:

--- task ---
If you have not already done so, set up your new Raspberry Pi by following these instructions:

[Setting up your Pi](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up)
--- /task ---

--- task ---
Connect a Raspberry Pi Camera Module to your Raspberry Pi, by following these instructions:

[Getting started with the Camera Module](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera)

--- /task ---

### Machine Learning

 Unlike most animals, computers do not have a natural ability to learn. Most things that computers do have been directly programmed by a human. These make them great for tasks that have a few clearly defined rules, but they struggle with more human like tasks such as recognising different objects.

 During training, a computer is shown thousands and thousands of images, for each it makes it's best guess as to what the object is. It's guess is then either confirmed as correct or rejected as false, with each new guess helping make the computer guess the correct names much more likely.

 The end result of this process in called a **model** and once sufficiently trained can be used in the real world to perform a task. 

### Testing a model

 For this project you won't be creating and training your own model but using an example model that can recognise a range of objects.

 To get started first download the model files and recogniser program from rpf.io/robot-face-go. 
 
 --- task ---
 
 Make sure you are connected to the internet, then open a terminal window on your Raspberry Pi by pressing `Ctrl + Alt + T`.
 
 --- /task ---

 --- task ---
 At the prompt type:

 `wget rpf.io/p/en/robot-face-go`

 Press Enter and wait for the notification that download has completed.

--- /task ---

--- task ---
 Unzip the new download to the home folder. Type:

 `unzip robot-face.zip /home/pi`

 Press Enter and wait for the notification that the unzip has completed.

--- /task ---


 You'll find a range of files that will be useful for the project but for this step we're going to use:

 - `model.tflite` - The machine learning model file.
 - `labels.txt` - Text labels for each object the model can recognise
 - `classifer.py` - A python program to test the model

--- task ---

 Open Thonny on your Raspberry Pi and the `fileC` program, which will display what the camera is "seeing", the name of the main object in view that it recognises and how confident it is about the object as a percentage.

 ![Image of recogniser project running](images/classifier.png)

--- /task ---

 Try presenting the camera with different objects and investigate which it can recognise with confidence. Whilst doing this experiment with:
   - **The background** -  A busy scene may cause your camera to recognise other objects instead of your target.
   - **Object position** - where and how you hold the object may effect how well it is detected, experiment with the distance from the camera as well as the orientation.
   - **Lighting** - the lighting in your environment may impact on how well your object is detected. Experiment with different light sources, levels and locations.
   - **Images** - You may find it beneficial to show the camera images of objects rather than the object themselves.

### Challenge

Can you find approximately 5 objects (or images) that your camera can recognise reliably?


