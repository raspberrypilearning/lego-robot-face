## Respuestas emocionales a los objetos.

Para finalizar el proyecto, puede hacer que la cara del robot muestre diferentes expresiones en función de lo que pueda ver la cámara.

![Código a la izquierda con la vista de la cámara que muestra diferentes imágenes que se sostienen frente a la cámara. A la derecha, la cara del robot reacciona a las imágenes.](images/completed_project.gif)

--- task ---

Comience importando la `Classifier` del archivo que utilizó anteriormente, junto con la función `sleep`.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 7
line_highlights:
---
desde el clasificador import Clasificador desde el tiempo import sleep --- / código ---

--- /task ---

--- task ---

Luego, cree una lista de objetos que el clasificador pueda reconocer. Puede ajustar el umbral `` más tarde para que el clasificador sea más o menos preciso con su reconocimiento.

--- code ---
---
language: python filename: line_numbers: true line_number_start: 31
line_highlights:
---

seen_items = Classifier (label_file = "labels.txt", model_file = "model.tflite", umbral = 0.5) --- / código ---

--- /task ---

--- task ---

Ahora cree un diccionario que vincule objetos con diferentes emociones. Puedes elegir tus propios objetos y emociones según lo que tengas a tu alrededor, o las imágenes que hayas impreso.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 33
line_highlights:
---

reacciones = {"brócoli": "neutral", "tetera": "neutral", "serpiente": "enojado", "perrito caliente": "feliz"} --- / código ---

--- /task ---

--- task ---

Por último, puede crear un ciclo para verificar lo que está en la `seen_items` cada dos segundos, y luego mostrar la expresión facial de acuerdo con su diccionario de `reacciones`

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 61
line_highlights:
---
while True: sleep (1) if seen_items.item! = seen_items.last_item: item = seen_items.item if item in set_face (caras [reacciones[item]]) sleep (1) --- / código ---

--- /task ---

--- save ---
