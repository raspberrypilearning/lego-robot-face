## Programa las cejas

El tercer motor se utiliza para mover las cejas del rostro.

--- task ---

Configura un objeto para el motor de las cejas.

--- code ---
---
language: python 
filename: robot_face.py 
line_numbers: true 
line_number_start: 3
line_highlights: 5
---
boca_d = Motor('A') 
boca_i = Motor('B') 
cejas = Motor('C')

--- /code ---

--- /task ---

--- task ---

Asegúrate de que tu motor grande esté posicionado de modo que la **paleta** y el **círculo** estén alineados, y que las cejas de la cara estén colocadas horizontalmente. Si no es así, es posible que debas ajustar un poco la estructura.

![Motor girado para que la paleta y el círculo estén alineados.](images/motor_0.jpg)

![La cara del robot con las cejas en posición horizontal.](images/horizontal_eyebrows.jpg)

--- /task ---

--- task ---

Ahora configura el motor para que gire a la posición `0` cuando comience el programa.

--- code ---
---
language: python 
filename: robot_face.py 
line_numbers: true 
line_number_start: 7
line_highlights: 9
---
boca_d.run_to_position(0) 
boca_i.run_to_position(0) 
cejas.run_to_position(0)
--- /code ---

--- /task ---

Aquí vamos a mostrar tres posiciones de cejas, pero puedes crear más.

- `0` hará que las cejas parezcan horizontales
- `150` bajará las cejas
- `-150` será levantar las cejas


--- task ---

Agrega una función que obtenga la posición actual de la ceja, y si la posición a la que se supone que debe moverse es menor que la actual, se moverá en sentido antihorario, de lo contrario, se moverá en sentido horario.

--- code ---
---
language: python 
filename: 
line_numbers: true 
line_number_start: 17
line_highlights:
---
def mover_cejas(posicion): 
    posicion_actual = cejas.get_aposition() 
    if posicion < posicion_actual: 
        rotacion = 'anticlockwise' 
    else: 
        rotacion = 'clockwise' 
    cejas.run_to_position(posicion, direction = rotacion)

--- /code ---

--- /task ---

--- task ---

Ejecuta tu código y prueba tu nueva función en la **Consola**.

--- code ---
---
language: python 
filename: 
line_numbers: false 
line_number_start:
line_highlights:
---
>>> mover_cejas(-150) 
>>> mover_cejas(150) 
>>> mover_cejas(0)
--- /code ---

--- /task ---

--- save ---
