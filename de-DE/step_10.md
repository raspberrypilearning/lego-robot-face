## Gesichter ändern

Jetzt ist es an der Zeit, all deine verschiedenen Funktionen zusammenzubringen, um das gesamte Gesicht zu verändern.

--- task ---

Zunächst musst du ein dictionary erstellen, um die verschiedenen Gesichtsausdrücke zu speichern, die du verwenden möchtest. Es enthält Werte für die Mundmotoren, den Augenbrauenmotor und die Augen.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 22
line_highlights:
---

gesichter = { "neutral":{"mund":0, "auge_rechts":neutral, "auge_links":neutral, "augenbrauen":0}, "gluecklich":{"mund":45, "auge_rechts": breit, "auge_links":wide, "augenbrauen":150}, "boese":{"mund":-20, "auge_rechts":wütend, "auge_links":wütend, "augenbrauen":-150}, " traurig":{"mund":-45, "auge_rechts":look_down, "auge_links":look_down, "augenbrauen":-40} } --- /code ---

--- /task ---

--- task ---

Erstelle nun eine Funktion, die Mund, Augenbrauen und Augen steuert.

--- code ---
---
language: python filename: robot_face.py line_numbers: true line_number_start: 50
line_highlights:
---
def gesicht_machen (gesicht): wechsle_augen(gesicht["auge_rechts"],gesicht["auge_links"]) mund_bewegen(gesicht["mund"]) augenbrauen_bewegen(gesicht["augenbrauen"]) --- /code - --

--- /task ---

--- task ---

Führe deinen Code aus und verwende dann die **Shell**, um deine neue Funktion zu testen.

--- code ---
---
language: python filename: line_numbers: true line_number_start:
line_highlights:
---
> > > gesicht_machen(gesichter['angry']) gesicht_machen(gesichter['happy']) gesicht_machen(gesichter['neutral']) gesicht_machen(gesichter['sad']) --- /code ---

--- /task ---

--- save ---
