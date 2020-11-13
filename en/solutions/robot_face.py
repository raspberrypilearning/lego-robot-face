import board
from time import sleep
from build_hat import BuildHAT
from adafruit_ht16k33.matrix import Matrix8x8
from PIL import Image


i2c = board.I2C()
left_eye = Matrix8x8(i2c, address=0x71)
right_eye = Matrix8x8(i2c, address=0x70)
bh = BuildHAT()


mouth_r = bh.port.C.motor
mouth_l = bh.port.D.motor
eb = bh.port.A.motor

def move_eb (pos,speed=100):
  if pos > 170:
    pos = 170
  elif pos < -170:
    pos = -170

  current_pos = eb.get()[2]
  eb.run_to_position(pos,speed)

def move_mouth (l_pos,r_pos, speed=100):
    mouth_l.run_to_position(l_pos*-1,speed,blocking=False)
    mouth_r.run_to_position(r_pos,speed,blocking=False)

def change_eyes(left,right):
    left_eye.image(Image.open("neutral.png"))
 #   left_eye[0, 0] = 1
    right_eye[7,7] = 1
    left_eye.show()
    right_eye.show()
  


faces = {
  "neutral":{"mouth_r":0,"mouth_l":0,"eye_r":"happy.png","eye_l":"happy.png","eyebrows":0},
  "happy":{"mouth_r":45,"mouth_l":45,"eye_r":"happy.png","eye_l":"happy.png","eyebrows":40},
  "sad":{"mouth_r":-45,"mouth_l":-45,"eye_r":"happy.png","eye_l":"happy.png","eyebrows":-40}
}

def set_face (face):
  change_eyes(face["eye_r"],face["eye_l"])
  move_mouth(face["mouth_l"],face["mouth_r"])
  move_eb(face["eyebrows"])

set_face(faces["neutral"])
input()


#while True:
#  set_face(faces["happy"])
#  sleep(5)
#  set_face(faces["sad"])
#  sleep(5)
