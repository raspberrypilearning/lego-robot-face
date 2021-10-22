## Usa emoji para tu cara de robot

El objetivo es construir una cara robótica que pueda responder a los objetos que reconoce. Si divide eso en pasos más pequeños, podría decir que su cara de robot:

1. Usa la cámara Raspberry Pi para buscar objetos
2. Si se detecta un objeto, use ese objeto para cambiar la cara
3. Haga coincidir el objeto detectado con una reacción o emoción
4. Cambia el aspecto de la cara para representar una reacción.
5. Regrese al paso 1 para buscar el siguiente objeto al que reaccionar.

Para que el proyecto funcione, necesitará una selección de reacciones que pueda mostrar usando expresiones faciales simples. Los emojis son un gran ejemplo de esto.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">Un emoji es un ejemplo de una abstracción <span style="color: #0faeb0"></span>, una representación simplificada de una cara real. Toda la complejidad se ha eliminado y se ha limitado a las partes clave simples de la cara.</p>

![Una variedad de emojis.](images/emojis.png)

En este proyecto, puedes usar estos cuatro emojis para representar ojos:

| <img src="resources/neutral.png" alt="Arte de 8 por 8 píxeles de una cara neutral" width="100" /> | <img src="resources/wide.png" alt="Arte de 8 por 8 píxeles de una cara con los ojos muy abiertos" width="100" /> | <img src="resources/angry.png" alt="Arte de 8 por 8 píxeles de una cara enojada" width="100" /> | <img src="resources/look_down.png" alt="Arte de 8 por 8 píxeles de una cara mirando hacia abajo" width="100" /> |
| ------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Neutral                                                                                                            | Amplio                                                                                                                            | Enfadado                                                                                                         | Mira abajo                                                                                                                       |



Sin embargo, si desea crear sus propios emojis, puede usar [piskel](https://www.piskelapp.com) para crear su propio emoji de 8 x 8. Utilice únicamente píxeles en blanco y negro.


### Conecta objetos a las expresiones

De sus experimentos en el paso anterior, habrá identificado al menos cuatro objetos que su cámara y modelo de aprendizaje automático pueden detectar de manera confiable.

--- task ---

Elija qué objetos desencadenarán qué reacciones en su robot. Cada expresión debe tener una reacción asociada.

Para nuestro ejemplo, usamos:

| Objeto    | Reacción                                                                                                                         |
| --------- | -------------------------------------------------------------------------------------------------------------------------------- |
| brócoli   | <img src="resources/neutral.png" alt="Arte de 8 por 8 píxeles de una cara neutral" width="25" />                |
| tetera    | <img src="resources/wide.png" alt="Arte de 8 por 8 píxeles de una cara con los ojos muy abiertos" width="25" /> |
| serpiente | <img src="resources/angry.png" alt="Arte de 8 por 8 píxeles de una cara enojada" width="25" />                  |
| Pancho    | <img src="resources/look_down.png" alt="Arte de 8 por 8 píxeles de una cara mirando hacia abajo" width="25" />  |

--- /task ---

--- save ---
