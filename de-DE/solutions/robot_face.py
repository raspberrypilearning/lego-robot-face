from buildhat import Motor
import board
from adafruit_ht16k33.matrix import Matrix8x8
from PIL import Image
from classifier import Classifier
from time import sleep

## Motoren einrichten
mund_r = Motor('A')
mund_l = Motor('B')
augenbrauen = Motor('C')

## Bewege die Motoren in die Null-Position
mund_r.run_to_position(0)
mund_l.run_to_position(0)
augenbrauen.run_to_position(0)

## Augen einrichten
i2c = board.I2C()
auge_links = Matrix8x8(i2c, address=0x70)
auge_rechts = Matrix8x8(i2c, address=0x71)

## verknüpfe Ausdrücke mit Bildern im Ressourcenverzeichnis zur Anzeige der Augen
neutral = Image.open("neutral.png").rotate(90)
grosz = Image.open("wide.png").rotate(90)
veraergert = Image.open("angry.png").rotate(90)
hinunterschauen = Image.open("look_down.png").rotate(90)

## Gesichts-Ausdrücke mit motorischen Bewegungen und Augenanzeigen in einem dictionary verknüpfen
gesichter = {
    "neutral":{"mund":0, "auge_rechts":neutral, "auge_links":neutral, "augenbrauen":0},
    "gluecklich":{"mund":45, "auge_rechts":grosz, "auge_links":grosz, "augenbrauen":-150},
    "boese":{"mund":-20, "auge_rechts":veraergert, "auge_links":veraergert, "augenbrauen":150},
    "traurig":{"mund":-45, "auge_rechts":hinunterschauen, "auge_links":hinunterschauen, "augenbrauen":-40}
    }

## Verwende classifier.py, um verschiedene Bilder zu erkennen (Datei befindet sich im Ressourcenverzeichnis)
gesehenes = Classifier(label_file="labels.txt",model_file="model.tflite",threshold=0.5)

## Lege Reaktionen für verschiedene Objekte fest, die erkannt werden
reaktionen = {"broccoli":"neutral", "teapot":"happy", "snake":"boese", "hotdog":"gluecklich"}

def mund_bewegen (position):
    '''Mund zum Wert des Positionsparameters bewegen'''
    mund_l.run_to_position(position * -1, blocking=False)
    mund_r.run_to_position(position, blocking=False)
    
    
def augenbrauen_bewegen (position):
    '''Brauen auf Wert des Positionsparameters verschieben'''
    position_jetzt = augenbrauen.get_aposition()
    if position < position_jetzt:
        rotation = 'anticlockwise'
    else:
        rotation = 'clockwise'
    augenbrauen.run_to_position(position, direction = rotation)


def wechsle_augen(links, rechts):
    '''Anzeige der PIL-Objekte auf dem linken und rechten Auge'''
    auge_links.image(left)
    auge_rechts.image(right)


def gesicht_machen (gesicht):
    '''alle Funktionen aufrufen, die den Gesichtsausdruck entsprechend dem Gesicht aus dem dictionary gesichter ändern'''
    wechsle_augen(gesicht["auge_rechts"],gesicht["auge_links"])
    mund_bewegen(gesicht["mund"])
    augenbrauen_bewegen(gesicht["augenbrauen"])

## Endlosschleife zur Überprüfung der Liste der gesehenen Gegenstände und Einstellung des richtigen Gesichts ein, wenn ein Objekt gesehen wurde
while True:
    sleep(1)
    if gesehenes.item != gesehenes.last_item:
        bild = gesehenes.item
        if bild in reaktionen.keys():
            gesicht_machen(gesichter[reaktionen[bild]])
    sleep(1)