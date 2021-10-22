## Testen Sie das Modell für maschinelles Lernen

Ihr erster Schritt besteht darin, zu verstehen und zu testen, wie Sie ein Modell für maschinelles Lernen verwenden können, um Objekte zu erkennen. Für dieses Projekt erstellen und trainieren Sie kein eigenes Modell, sondern verwenden ein Beispielmodell, das eine Reihe von Objekten erkennen kann.

Bevor Sie beginnen, müssen Sie Ihren Raspberry Pi-Computer eingerichtet und eine Raspberry Pi-Kamera angeschlossen haben. In den folgenden Anleitungen finden Sie Anweisungen, wie Sie beides tun können:

--- task --- Verbinden Sie ein Raspberry Pi-Kameramodul mit Ihrem Raspberry Pi, indem Sie diesen Anweisungen folgen:

[Erste Schritte mit dem Kameramodul](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera){:target="_blank"}

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Computer haben keine natürliche Lernfähigkeit. Die meisten Dinge, die Computer tun, wurden <span style="color: #0faeb0">direkt von einem Menschen programmiert</span>. Dadurch eignen sie sich hervorragend für Aufgaben, die ein paar klar definierte Regeln haben, aber sie kämpfen mit menschenähnlicheren Aufgaben wie dem Erkennen verschiedener Objekte.

Durch maschinelles Lernen können einem Computer Tausende und Abertausende von Bildern angezeigt werden, von denen jedes beschriftet ist. Nach und nach kann das Programm die Eigenschaften einer Gruppe von Bildern lernen und ihnen dann das richtige Label geben.

Das Endergebnis dieses Prozesses wird als <span style="color: #0faeb0">Modell</span>. Nach dem Training können Modelle in der realen Welt verwendet werden, um Aufgaben auszuführen. 
</p>

### Testen eines Modells

--- task ---

 Laden Sie zunächst die Ressourcen für dieses Projekt auf Ihren Raspberry Pi [herunter, indem Sie hier](http://rpf.io/p/en/robot-face-go){:target="_blank"} klicken.

 --- /task ---

 --- task ---

 Entpacken Sie die Dateien und verschieben Sie dann das entpackte Verzeichnis in Ihr `/home/pi` Verzeichnis.

 --- /task ---

 Sie werden eine Reihe von Dateien finden, die für das Projekt nützlich sind, aber für diesen Schritt verwenden Sie:

 - `model.tflite` – Die Modelldatei für maschinelles Lernen
 - `labels.txt` - Etiketten für jedes Objekt das Modell erkennen kann
 - `classifer.py` – Ein Python-Programm zum Testen des Modells

--- task ---

Öffnen Sie **Thonny**, das sich unter dem **Programmiermenü** in Ihrem Raspberry Pi **Startmenü**.

 --- /task ---

--- task ---

Öffnen und **Führen Sie** das `classifier.py` Programm aus.

Ihr Raspberry Pi zeigt Folgendes an:
+ Was die Kamera "sieht"
+ Der Name des Hauptobjekts, das es erkennt

 ![Bild des laufenden Erkennungsprojekts.](images/classifier.png)

--- /task ---

--- task ---

 **Versuchen Sie** die Kamera mit verschiedenen Objekten zu präsentieren und untersuchen Sie, welche sie sicher erkennen kann.

 Experimentieren Sie dabei mit:
   - **Hintergrund**: Die Kamera erkennt möglicherweise Objekte anstelle des Objekts, das Sie vor die Kamera halten.
   - ****: Wo und wie Sie das Objekt halten, kann sich auf seine Erkennung auswirken. Experimentieren Sie mit der Entfernung von der Kamera und drehen Sie das Objekt in verschiedene Richtungen.
   - **Beleuchtung**: Die Beleuchtung in Ihrem Raum kann beeinflussen, wie gut ein Objekt erkannt wird. Versuchen Sie, mehr Lichter einzuschalten oder einige Lichter auszuschalten.
   - **Bilder**: Es kann hilfreich sein, die von der Kamera gedruckten Bilder von Objekten statt der Objekte selbst anzuzeigen.

--- /task ---

--- task ---

Finden Sie **mindestens** vier Objekte (oder Bilder), die Ihre Kamera zuverlässig erkennen kann – Sie benötigen sie für Ihr Modell für maschinelles Lernen.

--- /task ---

--- save ---
