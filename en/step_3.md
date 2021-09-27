## Use emoji for your robot face

Before you delve straight into building and programming your robot face, consider how the project will work and think about what we'll need. 

The goal is to build a robotic face that can respond to objects that it recognises using machine learning. If we break that down into smaller steps we might say that our robot face will:

1. Use the Raspberry Pi camera to look for objects that match those in a pre-trained machine learning model.
2. If a object is detected with a degree of certainty, use that object to change the face.
3. Match the object detected to an appropriate reaction or emotion
4. Change to look of the face to represent the chosen reaction or emotion.
5. Return to step 1 to look for the next object to react to.

For the project to work it's going to need a selection of reactions and emotions that it can display using simple facial expressions... like emoji!

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">An emoji is an example of an <span style="color: #0faeb0">abstraction</span>, a simplified representation of a real face. All of the complexity has been removed and limited to the simple key parts of the face.</p>

![Range of emojis](images/emojis.png)

In this project, we will represent these five emojis:

| ![](images/happy.png) | ![](images/sad.png) | ![](images/love.png) | ![](images/sleep.png) | ![](images/laugh.png) |
| -------------------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- |
| Happy | Sad | Love | Sleep | Laugh | 

### Connecting objects to expressions

From your experiments in the previous step you will have identified at least five objects that your camera and machine learning model can reliably detect. 

--- task ---

Choose which objects will trigger which facial expressions in your robot. Each expression can have multiple objects associated with it but not the other way around.

For our example we are using: 

| Objects | Reaction |
| ------- | -------- |
| Brocoli, Chocolate | ![](images/happy.png)|
| Spider | ![](images/sad.png) |
| Cat | ![](images/love.png)
| Banana | ![](images/laugh.png) |
| Moon | ![](images/sleep.png) |

--- /task ---

