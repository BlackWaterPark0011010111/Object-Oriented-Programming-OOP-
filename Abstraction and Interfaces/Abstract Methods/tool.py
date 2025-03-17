#File: src/tool.py

#First, I need to implement the Laptop class and override the work() method
#to avoid the NotImplementedError. I think I should just print something.

class Tool:
    def work(self):
        raise NotImplementedError("Abstract Method not implemented")

#Implementing the Laptop class
class Laptop(Tool):  #I need to inherit from Tool
    def work(self):
        print("Laptop is running")  # Simple print statement as per the note

#Testing:
#laptop = Laptop()
#laptop.work()  # Should print "Laptop is running" and not raise an error

