# Project design

Before you delve straight into building and programming your robot face let's consider how the project will work and think about what we'll need. The goal is to build a robotic face that can respond to objects that it recognises using machine learning. If we break that down into smaller steps we might say that our robot face will:

1. Use the Raspberry Pi camera to look for objects that match those in a pre-trained machine learning model.
2. If a object is detected with a degree of certainty, use that object to change the face.
3. Match the object detected to an appropriate reaction or emotion
4. Change to look of the face to represent the chosen reaction or emotion.
5. Return to step 1 to look for the next object to react to.

# Getting expressive

For the project to work it's going to need a selection of reactions and emotions that it can display using simple facial expression.

Some expressions are going to be quite hard to display as they are quite subtle. For example how would you distinguish between **happy** and **smug**?

To keep it relatively simple we could look a range of simple emojis and select 5 to reproduce with our robot face.

*An emoji is an example of an **abstraction**, a siplified representation of a real face. All of the complexity has been removed and limited to the simple key parts of the face.*

![Range of emojis](images/emojis.png)

These are just a sample of the wide range of emojis available, some of which will be harder to represent that others. Most of the emojis rely on using the eyes and mouth to represent their expression with a few using additional props, colour or hands to enhance their meaning. If we were to choose 5 face to try and represent we might select:

| ![](imges/placeholder.png) | ![](imges/placeholder.png) | ![](imges/placeholder.png) | ![](imges/placeholder.png) | ![](imges/placeholder.png) |
| -------------------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- |
| Name | Name | Name | Name | Name | 



# Choosing objects

From your experiments in the previous step you will have hopefully identified some objects that your camera and machine learning model can reliably detect