from buildhat import Motor
import board
from adafruit_ht16k33.matrix import Matrix8x8
from PIL import Image
from classifier import Classifier
from time import sleep

## モーターのセットアップ
mouth_r = Motor('A')
mouth_l = Motor('B')
eyebrows = Motor('C')

## モーターを0の位置に移動
mouth_r.run_to_position(0)
mouth_l.run_to_position(0)
eyebrows.run_to_position(0)

## 目の設定
i2c = board.I2C()
left_eye = Matrix8x8(i2c, address=0x70)
right_eye = Matrix8x8(i2c, address=0x71)

## 表情の名前と、目を表示するためのリソースディレクトリ内の画像を関連付け
neutral = Image.open("neutral.png").rotate(90)
wide = Image.open("wide.png").rotate(90)
angry = Image.open("angry.png").rotate(90)
look_down = Image.open("look_down.png").rotate(90)

## 表情の名前と、モーターの動作・辞書内の目の表示を関連付け
faces = {
    "neutral":{"mouth":0, "right_eye":neutral, "left_eye":neutral, "eyebrows":0},
    "happy":{"mouth":45, "right_eye":wide, "left_eye":wide, "eyebrows":-150},
    "angry":{"mouth":-20, "right_eye":angry, "left_eye":angry, "eyebrows":150},
    "sad":{"mouth":-45, "right_eye":look_down, "left_eye":look_down, "eyebrows":-40}
    }

## 様々な画像を認識させるために classifier.py を使用する (ファイルはリソースディレクトリにあります)
seen_items = Classifier(label_file="labels.txt",model_file="model.tflite",threshold=0.5)

## 様々なオブジェクトが認識された時のリアクションの設定
reactions = {"broccoli":"neutral", "teapot":"happy", "Indian cobra":"angry", "hotdog":"happy"}

def move_mouth (position):
    '''口を position パラメータの位置に移動'''
    mouth_l.run_to_position(position * -1, blocking=False)
    mouth_r.run_to_position(position, blocking=False)
    
    
def move_eyebrows (position):
    '''眉毛を position パラメータの位置に移動'''
    current_position = eyebrows.get_aposition()
    if position < current_position:
        rotation = 'anticlockwise'
    else:
        rotation = 'clockwise'
    eyebrows.run_to_position(position, direction = rotation)


def change_eyes(left, right):
    '''PILオブジェクトを左目と右目に表示する'''
    left_eye.image(left)
    right_eye.image(right)


def set_face (face):
    '''顔の辞書内の顔に合わせて、表情を変更する関数を全部呼び出す'''
    change_eyes(face["right_eye"],face["left_eye"])
    move_mouth(face["mouth"])
    move_eyebrows(face["eyebrows"])

## 無限ループで見られたアイテムを確認して、物が見られた時に正しい顔を設定する
while True:
    sleep(1)
    if seen_items.item != seen_items.last_item:
        item = seen_items.item
        if item in reactions.keys():
            set_face(faces[reactions[item]])
    sleep(1)