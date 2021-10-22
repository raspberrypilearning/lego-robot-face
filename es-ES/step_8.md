## Programa las cejas

El tercer motor se utiliza para mover las cejas del rostro.

--- task ---

Configura un objeto para el motor de las cejas.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 3
line_highlights: 5
---
boca_r = Motor ('A') boca_l = Motor ('B') cejas = Motor ('C')

--- /code ---

--- /task ---

--- task ---

Asegúrese de que su motor grande esté posicionado de modo que el **piruleta** y el **círculo** estén alineados, y que las cejas de su cara estén colocadas horizontalmente. Si no es así, es posible que deba ajustar un poco su estructura.

![Motor girado para que la piruleta y el círculo estén alineados.](images/motor_0.jpg)

![La cara del robot con las cejas en posición horizontal.](images/horizontal_eyebrows.jpg)

--- /task ---

--- task ---

Ahora configure el motor para que gire a la posición `0` cuando comience el programa.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 7
line_highlights: 9
---
mouth_r.run_to_position (0) mouth_l.run_to_position (0) eyebrows.run_to_position (0) --- / código ---

--- /task ---

Hay tres posiciones de cejas que se mostrarán aquí, pero puede crear más.

- `0` hará que las cejas parezcan horizontales
- `150` bajará las cejas
- `-150` será levantar las cejas


--- task ---

Agregue una función que obtenga la posición actual de la ceja, y si la posición a la que se supone que debe moverse es menor que la actual, se moverá en sentido antihorario, de lo contrario, se moverá en sentido horario.

--- code ---
---
language: python filename: line_numbers: true line_number_start: 17
line_highlights:
---
def move_eyebrows (posición): current_position = eyebrows.get_aposition () if position < current_position: rotacion = 'antihorario' else: rotacion = 'sentido horario' cejass.run_to_position (posición, dirección = giro)

--- /code ---

--- /task ---

--- task ---

Ejecute su código y pruebe su nueva función en **Shell**.

--- code ---
---
language: python filename: line_numbers: false line_number_start:
line_highlights:
---
> > > move_eyebrows (-150) move_eyebrows (150) move_eyebrows (0) --- / código ---

--- /task ---

--- save ---
