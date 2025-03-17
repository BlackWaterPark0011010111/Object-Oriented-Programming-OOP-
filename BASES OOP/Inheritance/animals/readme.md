Python OOP Concepts - Animal Reign
In this exercise we will check how inheritance in Python and the usage of the super() built-in method and self work.

Overview of animal.py:
The Animal class represents an ordinary animal. It contains the number_of_legs and the number_of_eyes of an animal, as well as some of its behavior through the methods breathe() and walk(). It also contains the method summary(), which just summarizes the information of the current animal instance.
No extra action should be taken here.
Overview of dog.py:
Since every dog has 4 legs and two eyes, the constructor method should make a call to the Animal constructor, passing the correspondent values to the constructor.
You should override the breathe() method. It should call the breathe() method of the Animal class and then print "Dogs love to breathe with their mouths open.".
You should override the walk() method. It should call the walk() method of the Animal class and then print "Dogs love to run.".
Overview of german_shepard.py:
You should override the walk() method. It should call the walk() method of the Dog class and then print "German Shepard`s show their beautiful fur while running.".
Overview of animal_reign.py:
Where the main method resides, therefore where your code should be executed. An animal (human), a dog and a german shepard instances are created.
No extra action should be taken here.