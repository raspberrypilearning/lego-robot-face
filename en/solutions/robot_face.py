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
#  if abs(pos - current_pos) > 170:
 #   eb.run_to_position(0,speed)

  eb.run_to_position(pos,speed)

move_eb(0,100)
input()
move_eb(300,100)
input()
move_eb(40,100)
input()
move_eb(170,100)
input()
move_eb(-170,100)



mouth_r.run_to_position(0,100)
mouth_l.run_to_position(0,100)
