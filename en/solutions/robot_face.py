from buildhat import Motor
import board
from adafruit_ht16k33.matrix import Matrix8x8
from PIL import Image
from classifier import Classifier
from time import sleep

mouth_r = Motor('A')
mouth_l = Motor('B')
eyebrows = Motor('C')

mouth_r.run_to_position(0)
mouth_l.run_to_position(0)
eyebrows.run_to_position(0)

i2c = board.I2C()
left_eye = Matrix8x8(i2c, address=0x70)
right_eye = Matrix8x8(i2c, address=0x71)

neutral = Image.open("neutral.png").rotate(90)
wide = Image.open("wide.png").rotate(90)
angry = Image.open("angry.png").rotate(90)
look_down = Image.open("look_down.png").rotate(90)

faces = {
    "neutral":{"mouth":0, "right_eye":neutral, "left_eye":neutral, "eyebrows":0},
    "happy":{"mouth":45, "right_eye":wide, "left_eye":wide, "eyebrows":150},
    "angry":{"mouth":-20, "right_eye":angry, "left_eye":angry, "eyebrows":-150},
    "sad":{"mouth":-45, "right_eye":look_down, "left_eye":look_down, "eyebrows":-40}
    }

seen_items = Classifier(label_file="labels.txt",model_file="model.tflite",threshold=0.5)

reactions = {"broccoli":"sad","teapot":"happy","Indian cobra":"angry","hotdog":"happy"}

def move_mouth (position):
    mouth_l.run_to_position(position * -1, blocking=False)
    mouth_r.run_to_position(position, blocking=False)
    
    
def move_eyebrows (position):
    current_position = eyebrows.get_aposition()
    if position < current_position:
        rotation = 'anticlockwise'
    else:
        rotation = 'clockwise'
    eyebrows.run_to_position(position, direction = rotation)


def change_eyes(left,right):
    left_eye.image(left)
    right_eye.image(right)


def set_face (face):
    change_eyes(face["right_eye"],face["left_eye"])
    move_mouth(face["mouth"])
    move_eyebrows(face["eyebrows"])


while True:
    sleep(1)
    if seen_items.item != seen_items.last_item:
        item = seen_items.item
        if item in reactions.keys():
            set_face(faces[reactions[item]])
    sleep(1)