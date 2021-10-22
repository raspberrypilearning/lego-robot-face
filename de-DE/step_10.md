## Changing faces

Now it's time to bring all your different functions together to change the whole face.

--- task ---

To begin with, you need to create a dictionary to store the different facial expressions you want to use. This will give values for the mouth motors, the eyebrow motor, and the eyes.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 22
line_highlights:
---

faces = { "neutral":{"mouth":0, "right_eye":neutral, "left_eye":neutral, "eyebrows":0}, "happy":{"mouth":45, "right_eye":wide, "left_eye":wide, "eyebrows":150}, "angry":{"mouth":-20, "right_eye":angry, "left_eye":angry, "eyebrows":-150}, "sad":{"mouth":-45, "right_eye":look_down, "left_eye":look_down, "eyebrows":-40} } --- /code ---

--- /task ---

--- task ---

Now create a function that will set the mouth, eyebrows, and eyes.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 50
line_highlights:
---
def set_face (face): change_eyes(face["right_eye"],face["left_eye"]) move_mouth(face["mouth"]) move_eyebrows(face["eyebrows"]) --- /code ---

--- /task ---

--- task ---

Run your code and then use the **Shell** to test your new function.

--- code ---
---
language: python filename: line_numbers: true line_number_start:
line_highlights:
---
> > > set_face(faces['angry']) set_face(faces['happy']) set_face(faces['neutral']) set_face(faces['sad']) --- /code ---

--- /task ---

--- save ---
