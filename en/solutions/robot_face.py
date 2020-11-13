from build_hat import BuildHAT
bh = BuildHAT()

mouth_r = bh.port.C.motor
mouth_l = bh.port.D.motor
eb = bh.port.A.motor

def move_eb (pos,speed):
  if pos > 170:
    pos = 170
  elif pos < -170:
    pos = -170

  current_pos = eb.get()[2]
  eb.run_to_position(pos,speed)


def move_mouth (side, pos, speed=100):
  if pos > 45:
    pos = 45
  elif pos < -45:
    pos = -45

  if side == "l":
    pos = pos * -1
    mouth_l.run_to_position(pos,speed)
  elif side == "r":
    mouth_r.run_to_position(pos,speed)

move_mouth("l",45)
input()
move_mouth("l",-45)
input()
move_mouth("l",450)
input()
move_mouth("r",45)
input()
move_mouth("r",-45,10)
input()
move_mouth("R",45)
input()
