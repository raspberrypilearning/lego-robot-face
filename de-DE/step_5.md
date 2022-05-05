## Füge die Augen hinzu

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">Die im Beispiel verwendeten LED-Matrizen werden mit dem Raspberry Pi <span style="color: #0faeb0">I2C</span> Bus verbunden. Geräte, die I2C verwenden, werden mit einer bestimmten Nummer verbunden, die als Adresse bezeichnet wird. Da du zwei Matrizen verwendest, benötigt jede eine eigene Adresse. </p>

--- task ---

Bevor du diese anschließt, musst du die entsprechende [Montageanleitung](https://learn.adafruit.com/adafruit-led-backpack/0-8-8x8-matrix-assembly){:target="_blank"} befolgen. Die Montage der LED-Arrays erfordert einige Lötarbeiten. Hole dir daher die Erlaubnis eines Erwachsenen ein, bevor du Werkzeuge verwendest. Hier kannst du unserer Lötanleitung folgen.

<iframe width="560" height="315" src="https://www.youtube.com/embed/8Z-2wPWGnqE" title="YouTube-Videoplayer" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

--- /task ---

Die in diesem Projekt verwendeten Matrizen haben alle dieselbe Adresse, was bedeutet, dass eine von beiden eine neue Adresse benötigt, damit sie zusammen arbeiten können. Dazu ist noch etwas Löten erforderlich.

--- task ---

Schließe mit Ihrem Lötset die `A0` Verbindung von **nur einer** deiner Matrizen.

![Bilder der gelöteten und ungelöteten Platinen.](images/A0-soldering.jpg)

--- /task ---

--- task ---

Platziere die Augen in den quadratischen Fassungen auf deinem Robotergesicht. Verwende Gummibänder, um sie zu sichern, und stelle sicher, dass sich die Stifte oben befinden.

![Bild zeigt 8 x 8 Arrays, die im LEGO®-Gesicht montiert sind.](images/array_eyes.jpg)

--- /task ---

Nachdem der grundlegende Aufbau des Robotergesichts abgeschlossen ist, musst du den Raspberry Pi-Computer hinzufügen und deine Komponenten daran anschließen.
