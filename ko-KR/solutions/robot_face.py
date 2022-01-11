from buildhat import Motor
import board
from adafruit_ht16k33.matrix import Matrix8x8
from PIL import Image
from classifier import Classifier
from time import sleep

## 모터 설정
mouth_r = Motor('A')
mouth_l = Motor('B')
eyebrows = Motor('C')

## 모터를 0 위치로 이동
mouth_r.run_to_position(0)
mouth_l.run_to_position(0)
eyebrows.run_to_position(0)

## 눈 설정
i2c = board.I2C()
left_eye = Matrix8x8(i2c, address=0x70)
right_eye = Matrix8x8(i2c, address=0x71)

## 눈을 표시할 수 있도록 리소스 디렉토리의 이미지에 표현식 이름을 연결
neutral = Image.open("neutral.png").rotate(90)
wide = Image.open("wide.png").rotate(90)
angry = Image.open("angry.png").rotate(90)
look_down = Image.open("look_down.png").rotate(90)

## 딕셔너리 내 모터 움직임 및 눈 표시에 표현식 이름 연결
faces = {
    "neutral":{"mouth":0, "right_eye":neutral, "left_eye":neutral, "eyebrows":0},
    "happy":{"mouth":45, "right_eye":wide, "left_eye":wide, "eyebrows":-150},
    "angry":{"mouth":-20, "right_eye":angry, "left_eye":angry, "eyebrows":150},
    "sad":{"mouth":-45, "right_eye":look_down, "left_eye":look_down, "eyebrows":-40}
    }

## classifier.py를 사용하여 다른 이미지를 인식 (파일은 리소스 디렉토리에 있음).
seen_items = Classifier(label_file="labels.txt",model_file="model.tflite",threshold=0.5)

## 인식되는 다양한 객체에 대하여 반응 설정
reactions = {"broccoli":"neutral", "teapot":"happy", "Indian cobra":"angry", "hotdog":"happy"}

def move_mouth (position):
    '''입을 위치 매개변수의 값으로 이동'''
    mouth_l.run_to_position(position * -1, blocking=False)
    mouth_r.run_to_position(position, blocking=False)
    
    
def move_eyebrows (position):
    '''눈썹을 위치 매개변수의 값으로 이동'''
    current_position = eyebrows.get_aposition()
    if position < current_position:
        rotation = 'anticlockwise'
    else:
        rotation = 'clockwise'
    eyebrows.run_to_position(position, direction = rotation)


def change_eyes(left, right):
    '''왼쪽 및 오른쪽 눈에 PIL 개체를 표시'''
    left_eye.image(left)
    right_eye.image(right)


def set_face (face):
    '''얼굴 사전의 얼굴에 따라 표정을 바꾸는 모든 함수 호출'''
    change_eyes(face["right_eye"],face["left_eye"])
    move_mouth(face["mouth"])
    move_eyebrows(face["eyebrows"])

## 무한 반복을 돌려 seen_items 목록을 확인하고 객체를 본 경우 올바른 얼굴을 설정
while True:
    sleep(1)
    if seen_items.item != seen_items.last_item:
        item = seen_items.item
        if item in reactions.keys():
            set_face(faces[reactions[item]])
    sleep(1)