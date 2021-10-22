## Füge die Augen hinzu

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">Die im Beispiel verwendeten LED-Matrizen werden mit dem Raspberry Pi <span style="color: #0faeb0">I2C</span>. Geräte, die I2C verwenden, werden mit einer bestimmten Nummer verbunden, die als Adresse bezeichnet wird. Da Sie zwei Matrizen verwenden, benötigt jede eine eigene Adresse. </p>

--- task ---

Bevor Sie diese anschließen, müssen Sie die entsprechende [Montageanleitung](https://learn.adafruit.com/adafruit-led-backpack/0-8-8x8-matrix-assembly){:target="_blank"} befolgen. Die Montage der LED-Arrays erfordert einige Lötarbeiten. Holen Sie daher die Erlaubnis eines Erwachsenen ein, bevor Sie Werkzeuge verwenden. Hier können Sie unserer Lötanleitung folgen. <iframe width="560" height="315" src="https://www.youtube.com/embed/8Z-2wPWGnqE" title="YouTube-Videoplayer" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen mark="crwd-mark"></iframe>

--- /task ---

Die in diesem Projekt verwendeten Matrizen haben alle dieselbe Adresse, was bedeutet, dass eine von ihnen eine neue Adresse benötigt, damit zwei zusammenarbeiten können. Dazu ist noch etwas Löten erforderlich.

--- task ---

Schließen Sie mit Ihrem Lötset die `A0` Verbindung von **nur einer** Ihrer Matrizen.

![Bilder der gelöteten und ungelöteten Platinen.](images/A0-soldering.jpg)

--- /task ---

--- task ---

Platzieren Sie die Augen in den quadratischen Fassungen auf Ihrem Robotergesicht; Verwenden Sie Gummibänder, um sie zu sichern, und stellen Sie sicher, dass sich die Stifte oben befinden.

![Bild zeigt 8 x 8 Arrays, die im LEGO®-Gesicht montiert sind.](images/array_eyes.jpg)

--- /task ---

Nachdem der grundlegende Aufbau des Robotergesichts abgeschlossen ist, müssen Sie den Raspberry Pi-Computer hinzufügen und Ihre Komponenten daran anschließen.
