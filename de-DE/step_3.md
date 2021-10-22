## Verwenden Sie Emoji für Ihr Robotergesicht

Ziel ist es, ein Robotergesicht zu bauen, das auf erkannte Objekte reagieren kann. Wenn Sie das in kleinere Schritte unterteilen, könnten Sie sagen, dass Ihr Robotergesicht:

1. Verwenden Sie die Raspberry Pi-Kamera, um nach Objekten zu suchen
2. Wenn ein Objekt erkannt wird, verwenden Sie dieses Objekt, um das Gesicht zu ändern
3. Ordne das erkannte Objekt einer Reaktion oder Emotion zu
4. Ändere das Aussehen des Gesichts, um eine Reaktion darzustellen
5. Kehren Sie zu Schritt 1 zurück, um nach dem nächsten Objekt zu suchen, auf das Sie reagieren können

Damit das Projekt funktioniert, braucht es eine Auswahl von Reaktionen, die es mit einfachen Gesichtsausdrücken anzeigen kann. Emojis sind ein großartiges Beispiel dafür.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">Ein Emoji ist ein Beispiel für eine <span style="color: #0faeb0">Abstraktion</span>, eine vereinfachte Darstellung eines echten Gesichts. Die ganze Komplexität wurde entfernt und auf die einfachen Schlüsselteile des Gesichts beschränkt.</p>

![Eine Reihe von Emojis.](images/emojis.png)

In diesem Projekt können Sie diese vier Emojis verwenden, um Augen darzustellen:

| <img src="resources/neutral.png" alt="8 x 8 Pixel Kunst eines neutralen Gesichts" width="100" /> | <img src="resources/wide.png" alt="8 x 8 Pixel Kunst eines großäugigen Gesichts" width="100" /> | <img src="resources/angry.png" alt="8 x 8 Pixel Kunst eines wütenden Gesichts" width="100" /> | <img src="resources/look_down.png" alt="8 x 8 Pixel Kunst eines nach unten schauenden Gesichts" width="100" /> |
| ----------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Neutral                                                                                                           | Weit                                                                                                             | Verärgert                                                                                                      | Schau runter                                                                                                                    |



Wenn Sie jedoch Ihre eigenen Emojis erstellen möchten, können Sie [Piskel](https://www.piskelapp.com) , um Ihre eigenen 8 x 8 Emojis zu erstellen. Verwenden Sie nur schwarze und weiße Pixel.


### Verbinde Objekte mit den Ausdrücken

Aus Ihren Experimenten im vorherigen Schritt haben Sie mindestens vier Objekte identifiziert, die Ihre Kamera und Ihr Modell für maschinelles Lernen zuverlässig erkennen können.

--- task ---

Wählen Sie aus, welche Objekte welche Reaktionen in Ihrem Roboter auslösen. Jedem Ausdruck sollte eine Reaktion zugeordnet sein.

Für unser Beispiel haben wir verwendet:

| Objekt   | Reaktion                                                                                                                       |
| -------- | ------------------------------------------------------------------------------------------------------------------------------ |
| Brokkoli | <img src="resources/neutral.png" alt="8 x 8 Pixel Kunst eines neutralen Gesichts" width="25" />               |
| Teekanne | <img src="resources/wide.png" alt="8 x 8 Pixel Kunst eines großäugigen Gesichts" width="25" />                |
| Schlange | <img src="resources/angry.png" alt="8 x 8 Pixel Kunst eines wütenden Gesichts" width="25" />                  |
| Hotdog   | <img src="resources/look_down.png" alt="8 x 8 Pixel Kunst eines nach unten schauenden Gesichts" width="25" /> |

--- /task ---

--- save ---
