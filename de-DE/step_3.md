## Verwende Emoji für dein Robotergesicht

Ziel ist es, ein Robotergesicht zu bauen, das auf erkannte Objekte reagieren kann. Wenn du das in kleinere Schritte unterteilst, könntest du sagen, dass dein Robotergesicht:

1. Die Raspberry Pi-Kamera verwendet, um nach Objekten zu suchen
2. Den Gesichtsausdruck ändern, wenn ein Objekt erkannt wird
3. Das erkannte Objekt einer Reaktion oder Emotion zuordnen
4. Das Aussehen des Gesichts ändern, um eine Reaktion darzustellen
5. Zu Schritt 1 zurückkehren, um nach dem nächsten Objekt zu suchen, auf das es reagieren kann

Damit das Projekt funktioniert, braucht es eine Auswahl von Reaktionen, die es mit einfachen Gesichtsausdrücken anzeigen kann. Emojis sind ein großartiges Beispiel dafür.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">Ein Emoji ist ein Beispiel für eine <span style="color: #0faeb0">Abstraktion</span>, eine vereinfachte Darstellung eines echten Gesichts. Die ganze Komplexität wurde entfernt und auf die einfachen Schlüsselteile des Gesichts beschränkt.</p>

![Eine Reihe von Emojis.](images/emojis.png)

In diesem Projekt kannst du diese vier Emojis verwenden, um Augen darzustellen:

| <img src="resources/neutral.png" alt="8 x 8 Pixel Kunst eines neutralen Gesichts" width="100" /> | <img src="resources/wide.png" alt="8 x 8 Pixel Kunst eines Gesichts mit großen Augen" width="100" /> | <img src="resources/angry.png" alt="8 x 8 Pixel Kunst eines wütenden Gesichts" width="100" /> | <img src="resources/look_down.png" alt="8 x 8 Pixel Kunst eines nach unten schauenden Gesichts" width="100" /> |
| ----------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Neutral                                                                                                           | Groß                                                                                                                  | Verärgert                                                                                                      | Hinunterschauen                                                                                                                 |



Wenn du jedoch deine eigenen Emojis erstellen möchtest, kannst du [Piskel](https://www.piskelapp.com) verwenden, um 8 x 8 Emojis zu erstellen. Verwende nur schwarze und weiße Pixel.


### Verbinde Objekte mit den Ausdrücken

Aus deinen Experimenten im vorherigen Schritt hast du mindestens vier Objekte identifiziert, die deine Kamera und Ihr Modell für maschinelles Lernen zuverlässig erkennen können.

--- task ---

Wähle aus, welche Objekte welche Reaktionen in deinem Roboter auslösen. Jedem Ausdruck sollte eine Reaktion zugeordnet sein.

Für unser Beispiel haben wir verwendet:

| Objekt   | Reaktion                                                                                                                       |
| -------- | ------------------------------------------------------------------------------------------------------------------------------ |
| Brokkoli | <img src="resources/neutral.png" alt="8 x 8 Pixel Kunst eines neutralen Gesichts" width="25" />               |
| Teekanne | <img src="resources/wide.png" alt="8 x 8 Pixel Kunst eines Gesichts mit großen Augen" width="25" />           |
| Schlange | <img src="resources/angry.png" alt="8 x 8 Pixel Kunst eines wütenden Gesichts" width="25" />                  |
| Hotdog   | <img src="resources/look_down.png" alt="8 x 8 Pixel Kunst eines nach unten schauenden Gesichts" width="25" /> |

--- /task ---

--- save ---
