from buildhat import Motor
import board
from adafruit_ht16k33.matrix import Matrix8x8
from PIL import Image
from classifier import Classifier
from time import sleep

## Configurar los motores
boca_d = Motor ('A')
boca_i = Motor ('B')
cejas = Motor ('C')

## Mueve los motores a la posición 0
boca_d.run_to_position(0)
boca_i.run_to_position(0)
cejas.run_to_position(0)

## Configura los ojos
i2c = board.I2C()
ojo_izquierdo = Matrix8x8(i2c, address= 0x70)
ojo_derecho = Matrix8x8(i2c, address= 0x71)

## Vincular los nombres de expresiones a imágenes en el directorio de Recursos para que los ojos las muestren
neutral = Image.open ("neutral.png").rotate(90)
abierto = Image.open("wide.png").rotate(90)
enojado = Image.open("angry.png").rotate(90)
abajo = Image.open("look_down.png").rotate(90)

## Vincular los nombres de expresiones al movimiento de los motores y a la imagen de los ojos en un diccionario
caras = {
    "neutral": {"boca": 0, "ojo_derecho": neutral, "ojo_izquierdo": neutral, "cejas": 0},
    "feliz": {"boca": 45, "ojo_derecho": abierto, "ojo_izquierdo": abierto, "cejas": -150},
    "enojado": {"boca": - 20, "ojo_derecho": enojado, "ojo_izquierdo": enojado, "cejas": 150},
    "triste": {"boca": - 45, "ojo_derecho": abajo, "ojo_izquierdo": abajo, "cejas": - 40}
    }

## Usa classifier.py para reconocer diferentes imágenes (el archivo está en el directorio de recursos)
objetos_vistos = Classifier(archivo_palabras = "labels.txt", archivo_modelo = "model.tflite",threshold=0.5)

## Establecer reacciones para diferentes objetos que se reconocen
reacciones = {"brócoli": "neutral", "tetera": "feliz", "cobra india": "enojado", "perro caliente": "feliz"}

def mover_boca(posicion):
    '' 'Mueve la boca al valor del parámetro de posición' ''
    boca_i.run_to_position (posicion * -1, blocking=False)
    boca_d.run_to_position (posicion, blocking=False)
    
    
def mover_cejas(posicion):
    '''Mueve las cejas al valor del parámetro de posición'''
    posición_actual = cejas.get_aposition ()
    if posicion <posicion_actual:
        rotacion = 'anticlockwise'
    else:
        rotacion = 'clockwise'
    cejas.run_to_position (posicion, direccion = rotacion)


def cambiar_ojos(izquierda, derecha):
    '''muestra los objetos PIL en el ojo izquierdo y derecho'''
    ojo_izquierdo.image(izquierda)
    ojo_dercho.image(derecha)


def set_face (cara):
    '''llama a todas las funciones que cambian la expresión, según el rostro del diccionario de caras'''
    cambiar_onos(cara ["ojo_derecho"], cara ["ojo_izquierdo"])
    mover_boca(cara ["boca"])
    mover_cejas(cara ["cejas"])

## Haz un bucle para siempre y verifica la lista de elementos vistos y selecciona la cara correcta si el objeto ha sido visto
while True:
    sleep(1)
    if objetos_vistos.item != objetos_vistos.last_item:
        objeto = seen_items.item
        if objeto in reacciones.keys():
            set_face(caras[reaccions[objeto]])
    sleep(1)