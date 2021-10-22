## Fügen Sie den Himbeer-Pi . hinzu

Für dieses Projekt möchten Sie idealerweise das Build Plate-Element verwenden, um Ihren Raspberry Pi und Build HAT zu montieren:

![Bild mit einer magentafarbenen LEGO® Bauplatte.](images/build_10.png)

--- task ---

Montieren Sie Ihren Raspberry Pi mit M2-Schrauben und Muttern auf der Bauplatte und stellen Sie sicher, dass sich der Pi auf der flachen Seite befindet:

 ![Raspberry Pi mit einer magentafarbenen LEGO® Bauplatte verschraubt.](images/build_11.jpg)

--- /task ---

Die Montage des Raspberry Pi auf diese Weise ermöglicht einen einfachen Zugriff auf die Anschlüsse sowie den SD-Kartensteckplatz.

### Montieren Sie die Kamera und bauen Sie HAT

Bevor Sie den Build HAT hinzufügen, müssen Sie zuerst das Flachbandkabel der Kamera am Raspberry Pi befestigen und durch das Loch im Build HAT fädeln. Wenn Sie die Kameraplatine noch nicht mit Ihrem Raspberry Pi verbunden haben, können Sie dies wie folgt tun: [Erste Schritte mit dem Kameramodul](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera){:target="_blank"}.

![Animation, die zeigt, wie das Raspberry Pi-Kameramodul mit dem Raspberry Pi verbunden wird.](images/connect-camera.gif)

--- task ---

Lassen Sie das Kameraband mit dem Raspberry Pi verbunden, aber entfernen Sie die Kameraplatine vom losen Ende des Bandes, indem Sie den kleinen schwarzen Clip nach oben drücken und das Band herausziehen:

![Bild zeigt die Rückseite der Kameraplatine mit geschlossenem Clip.](images/build_12.jpg)

![Bild zeigt die Rückseite der Kameraplatine mit geöffnetem Clip und entferntem Farbband.](images/build_13.jpg)

--- /task ---

--- task ---

Stecken Sie das Band durch die Unterseite des Build HAT und durch die Oberseite, um sicherzustellen, dass das Band nicht verdreht ist: ![Bild des Picamera-Bandes, das oben durch den Build HAT ragt.](images/build_14.jpg)

--- /task ---

--- task ---

Richten Sie den Build HAT mit dem Raspberry Pi aus und stellen Sie sicher, dass Sie das Label `This way up` Stellen Sie sicher, dass alle GPIO-Pins vom HAT bedeckt sind, und drücken Sie sie fest nach unten. (Das Beispiel verwendet einen [Stacking-Header](https://www.adafruit.com/product/2223){:target="_blank"}, wodurch die Pins länger werden.)

![Bild von GPIO-Pins, die durch die Oberseite des Build HAT ragen.](images/build_15.jpg)

--- /task ---

--- Aufgabe --- Bringen Sie die Kamera wieder am Ende des Flachbandkabels an und stellen Sie sicher, dass es nicht verdreht ist.

![Bild der am Flachbandkabel befestigten Picamera.](images/build_16.jpg)

--- /task ---

--- Aufgabe --- Verbinden Sie die Bauplatte mit einigen schwarzen Bolzen an der Rückseite Ihres Robotergesichts. ![Bild einer Maker Plate und eines Raspberry Pi, die an der Rückseite des Robotergesichts angeschlossen sind.](images/build_17.jpg)

Die Montage des Raspberry Pi auf diese Weise bietet den besten Zugang zu Anschlüssen und Pins und bedeutet, dass Ihre Barrel-Buchse einfach angeschlossen werden kann, um das Robotergesicht mit Strom zu versorgen.

--- /task ---

--- task ---

Schließen Sie Ihre kleinen LEGO® Technic™ Motoren an die Anschlüsse A und B an, um den Mund zu steuern.

![Bild von zwei kleinen LEGO® Technic™ Motoren, die mit den Anschlüssen A und B des Build HAT verbunden sind.](images/build_18.jpg)

--- /task ---

--- task ---

Schließen Sie Ihren großen LEGO® Technic™ Motor an Port C an, um die Augenbrauen zu kontrollieren.

![Bild, das einen großen LEGO® Technic™ Motor zeigt, der an Port C des Build HAT angeschlossen ist.](images/build_19.jpg)

--- /task ---

--- task ---

Kleben Sie mit dem Klebepad an der Unterseite ein Steckbrett oben auf den Rahmen, der den großen LEGO® Motor trägt.

![Bild, das ein Steckbrett zeigt, das oben am Robotergesichtsmechanismus befestigt ist.](images/build_20.jpg)

--- /task ---

--- task ---

Montieren Sie die Kameraplatine im Halter auf der Oberseite des Roboters, indem Sie das Band unter den Halter führen und die Kamera zwischen den Gummistoppern auf beiden Seiten verkeilen.

Sichern Sie die Kamera mit einem Gummiband mit den schwarzen Ösen auf beiden Seiten.

![Das Bild zeigt die Kameraplatine, die mit Gummibändern an Vorder- und Rückseite befestigt ist.](images/build_21.jpg)

--- /task ---

Um das Augenpaar mit dem Raspberry Pi GPIO zu verbinden, müssen sie zuerst mit einem Steckbrett und dann mit den GPIO-Pins vom Steckbrett verbunden werden.

--- task ---

Verwenden Sie acht männlich-weibliche Überbrückungsdrähte, um die vier Stifte von jedem Auge auf dem Steckbrett miteinander zu verbinden. Stellen Sie sicher, dass sich beide VCC-Pins in derselben Reihe des Steckbretts befinden, sich beide GND-Pins in derselben Reihe befinden und so weiter. Verbinden Sie dann die 3V3-, GND-, SDA- und SCL-Pins des Raspberry Pi, wie unten gezeigt.

![I2C-Diagramm.](images/eye_wiring.png)

--- /task ---

Ihr Robotergesicht ist jetzt gebaut, verbunden und kann programmiert werden!





