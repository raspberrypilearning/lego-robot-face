## Respuestas emocionales a los objetos

Para finalizar el proyecto, puedes hacer que la cara del robot muestre diferentes expresiones en función de lo que ve la cámara.

![Programa a la izquierda con la vista de la cámara que muestra diferentes imágenes que se sostienen frente a la cámara. A la derecha, la cara del robot reacciona a las imágenes.](images/completed_project.gif)

--- task ---

Comienza importando la clase `Classifier` del archivo que utilizaste anteriormente, junto con la función `sleep`.

--- code ---
---
language: python 
filename: robot_face.py 
line_numbers: true 
line_number_start: 7
line_highlights:
---
from classifier import Classifier 
from time import sleep
--- /code ---

--- /task ---

--- task ---

Luego, crea una lista de objetos que el clasificador pueda reconocer. Puedes ajustar el `umbral` más tarde para que el clasificador sea más o menos preciso con su reconocimiento.

--- code ---
---
language: python 
filename: 
line_numbers: true 
line_number_start: 31
line_highlights:
---

objetos_vistos = Classifier(archivo_palabras="labels.txt",archivo_modelo="model.tflite",threshold=0.5)
--- /code ---

--- /task ---

--- task ---

Ahora crea un diccionario que vincule objetos con diferentes emociones. Puedes elegir tus propios objetos y emociones según lo que tengas a tu alrededor, o las imágenes que hayas impreso.

--- code ---
---
language: python 
filename: robot_face.py 
line_numbers: true 
line_number_start: 33
line_highlights:
---

reacciones = {"brócoli":"neutral","tetera":"neutral","serpiente":"enojado","perro caliente":"feliz"}
--- /code ---

--- /task ---

--- task ---

Por último, puedes crear un ciclo para verificar lo que está en la lista `objetos_vistos` cada dos segundos, y luego mostrar la expresión facial de acuerdo con su diccionario de `reacciones`.

--- code ---
---
language: python 
filename: robot_face.py 
line_numbers: true 
line_number_start: 61
line_highlights:
---
while True: 
    sleep (1) 
    if objetos_vistos.item != objetos_vistos.last_item: 
        objeto = objetos_vistos.item 
        if item in reacciones.keys(): 
            fijar_cara(caras[reacciones[item]]) 
    sleep (1)
--- /code ---

--- /task ---

--- save ---
