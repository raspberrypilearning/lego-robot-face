from build_hat import BuildHAT
from time import sleep
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

def change_eye(side,img):
  pass


faces = {
  "happy":{"mouth_r":45,"mouth_l":45,"right_eye":"happy.png","left_eye":"happy.png","eyebrows":40}
  "sad":{"mouth_r":-45,"mouth_l":-45,"right_eye":"happy.png","left_eye":"happy.png","eyebrows":-40}
}

def set_face (face):
  change_eye("l",face["eye_l"])
  change_eye("r",face["eye_r"])
  move_mouth(face["mouth_l"],face["mouth_r"])
  move_eb(face["eyebrows"])


set_face(faces[happy])
sleep(5)
set_face(faces[sad])
