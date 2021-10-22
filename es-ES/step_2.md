## Prueba el modelo de aprendizaje automático

Su primer paso es comprender y probar cómo puede usar un modelo de aprendizaje automático para reconocer objetos. Para este proyecto, no creará ni entrenará su propio modelo, sino que utilizará un modelo de ejemplo que pueda reconocer una variedad de objetos.

Antes de comenzar, deberá haber configurado su computadora Raspberry Pi y conectado una cámara Raspberry Pi. Puede encontrar instrucciones sobre cómo hacer ambas cosas en las siguientes guías:

--- tarea --- Conecte un módulo de cámara Raspberry Pi a su Raspberry Pi siguiendo estas instrucciones:

[Introducción al módulo de la cámara](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera){: target = "_ blank"}

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Las computadoras no tienen una habilidad natural para aprender. La mayoría de las cosas que hacen las computadoras han sido <span style="color: #0faeb0">programadas directamente por un ser humano</span>. Esto los hace excelentes para tareas que tienen algunas reglas claramente definidas, pero luchan con tareas más similares a las humanas, como reconocer diferentes objetos.

Mediante el aprendizaje automático, una computadora puede mostrar miles y miles de imágenes, cada una de las cuales ha sido etiquetada. Poco a poco, el programa puede aprender las características de un grupo de imágenes y luego darles la etiqueta correcta.

El resultado final de este proceso se llama modelo <span style="color: #0faeb0"></span>. Una vez entrenados, los modelos se pueden utilizar en el mundo real para realizar tareas. 
</p>

### Probando un modelo

--- task ---

 Para comenzar, descargue los recursos para este proyecto en su Raspberry Pi [haciendo clic aquí](http://rpf.io/p/en/robot-face-go){: target = "_ blank"}.

 --- /task ---

 --- task ---

 Descomprima los archivos y luego mueva el directorio descomprimido a su directorio `/ home / pi`.

 --- /task ---

 Encontrará una variedad de archivos que serán útiles para el proyecto, pero para este paso, usará:

 - `model.tflite` : el archivo del modelo de aprendizaje automático
 - `labels.txt` : etiquetas para cada objeto que el modelo puede reconocer
 - `classifer.py` - Un programa de Python para probar el modelo

--- task ---

Abra **Thonny**, que se encuentra en el menú **** en el menú Inicio de su Raspberry Pi ****.

 --- /task ---

--- task ---

Abierta y **Run** al `classifier.py` programa.

Tu Raspberry Pi mostrará:
+ Qué está "viendo" la cámara
+ El nombre del objeto principal en vista de que reconoce

 ![Imagen del proyecto del reconocedor en ejecución.](images/classifier.png)

--- /task ---

--- task ---

 **Intente** presentar a la cámara diferentes objetos e investigue cuáles puede reconocer con confianza.

 Mientras hace esto, experimente con:
   - **El fondo**: la cámara puede reconocer objetos en lugar del objeto que sostiene frente a la cámara.
   - **Posición del objeto**: dónde y cómo sostiene el objeto puede afectar la forma en que se reconoce. Experimente con la distancia de la cámara y gire el objeto en diferentes direcciones.
   - **Iluminación**: La iluminación de su habitación puede afectar la detección de un objeto. Intente encender más luces o apagar algunas luces.
   - **Imágenes**: puede resultarle útil mostrar a la cámara imágenes impresas de objetos en lugar de los objetos en sí.

--- /task ---

--- task ---

Busque **al menos** cuatro objetos (o imágenes) que su cámara pueda reconocer de manera confiable; los necesitará para su modelo de aprendizaje automático.

--- /task ---

--- save ---
