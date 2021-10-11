## Emotional responses to objects

To finish off the project, you can make the robot face display different expressions depending on what the camera can see.

![code on the left with camera view showing different images being held infront of the camera. On the right the robot face is reacting to the images](images/completed_project.gif)

--- task ---

Start by importing the `Classifier` class from a the file that you used earlier, along with the `sleep` function.

--- code ---
---
language: python
filename: robot_face.py
line_numbers: true
line_number_start: 7
line_highlights: 
---
from classifier import Classifier
from time import sleep
--- /code ---

--- /task ---

--- task ---

Then create a list of objects that the classifier can recognise. You can adjust the `threshold` later to make the classifier more or less accurate with it's recognition.

--- code ---
---
language: python
filename: 
line_numbers: true
line_number_start: 31
line_highlights: 
---

seen_items = Classifier(label_file="labels.txt",model_file="model.tflite",threshold=0.5)
--- /code ---

--- /task ---

--- task ---

Now create a dictionary that links objects to different emotions. You can choose your own objects and emotions depending on what you have around you, or images that you have printed out.

--- code ---
---
language: python
filename: robot_face.py
line_numbers: true
line_number_start: 33
line_highlights: 
---

reactions = {"broccoli":"neutral","teapot":"neutral","snake":"angry","hotdog":"happy"}
--- /code ---

--- /task ---

--- task ---

Lastly, you can create a loop to check what is in the `seen_items` list every two seconds, and then display the facial expression according to your `reactions` dictionary.

--- code ---
---
language: python
filename: robot_face.py
line_numbers: true
line_number_start: 61
line_highlights: 
---
while True:
    sleep(1)
    if seen_items.item != seen_items.last_item:
        item = seen_items.item
        if item in reactions.keys():
            set_face(faces[reactions[item]])
    sleep(1)
--- /code ---

--- /task ---

--- save ---