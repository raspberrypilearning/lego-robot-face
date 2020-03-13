## Recognising Objects

Your first step will be understand and test how we can use a machine learning model to recognise objects. Before you begin you'll need to have setup your Raspberry Pi Computer and connected A Raspberry Pi Camera. You can find instructions on how to do both in the following guides:

 - [Setting up your Pi](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up)
 - [Getting started with the Camera Module](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera)


### Machine Learning



 Unlike most animals, computers do not have a natural ability to learn. Most behaviours that computers display have been directly programmed by a human. These make them great for tasks involving a few clearly defined rules, but struggle with more human like tasks such as recognising objects. Here the number and complexity of the rules that would be need make such a task impracticle if not impossible. For machines to be able to recognise objects we need to help them to learn usually using re-inforcement learning, similar to how humans learn from a young age.

 For example each time a toddler encounters an animal and proudly shouts "dog!", the times they are correct they may receive praise and when incorrect receive none. The praise acts to reinforce their idea of what a dog is, whilst it's absense makes the animal seen less likely to be labelled "dog!" again. The more animals the toddler sees the better it becomes at recognising dogs and not dogs, this same approach can replicated for computers through a process called training.

 During trainig a computer is show thousands and thousands of image, for each it makes it's best guess as to what the object is. It's guess is then either confirmed as correct or rejected as false, a correct guess it rewarded and the probability of that guess occuring again is increased. Each new guess helps re-inforce correct guesses and make the computer guess the correct names much more likely.

 The end result of this process in callled a **model** and once sufficietly trained can be used in the real world to perform a task. One important consideration is that the model is only as good as the variety and quatity of inputs it was trained on. If a model is only tested on a small sample of inputs it will have few opportunities to be refined and therefore likely be less good it's job. Likewise if a model had only every seen examples of siamese cats then it would also struggle to recognise other varieties of cat that look quite different.

### Testing a model

 For this project you won't be creating and training your own model but using an example model that can recognise a range of objects.

 To get started first download the model files and recogniser program from rpf.io/robot-face-go. A quick way to do this is by opening a terminal and typing:

 `wget rpf.io/p/en/robot-face-go`

 As we're going to use **Mu** for editing our code let's unzip the download to the mu-code folder.

 `unzip robot-face.zip ~/mu-code/`

 You'll find a range of files that will be useful for the project but for this step we're going to use:

 - `fileA` - The machine learning model file.
 - `fileB` - Text labels for each object the model can recognise
 - `fileC` - A python program to test the model


