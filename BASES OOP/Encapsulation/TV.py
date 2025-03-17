"""Python OOP Concepts - TV Party
It's time to make a TV party! You invited your friends over on a Saturday night to watch some movies on Netflix. The popcorn is ready, so let's set the TV to work!

The TV class is already created for you and will have regular TV operations such as Turn On, Turn Off, Volume Up, Volume Down, Channel Up, Channel Down, Set Channel and Set Volume.

These operations are defined in the TV class, and therefore, are common operations to any TV. But knowing what a TV does doesn't mean you have a TV, and that's why you need to have an instance object of the TV class.

Overview of tv.py:
Initialize the channel variable and set it to 1;
Initialize the volume_level variable and set it to 1;
Set the turned_on variable to False so that the TV is in the default off position;
turn_on() method should turn the TV on;
turn_off() method should turn the TV off;
channel_up() should increment the channel by 1. Note that the TV must be on;
channel_down() should decrement the channel by 1. Note that the TV must be on;
set_channel() method to set the TV to a specific channel. Note that the TV must be on;
volume_up() should increment the volume by 1. Note that the TV must be on;
volume_down() should decrement the volume by 1. Note that the TV must be on;
The channel's range should be between 1 and 100. The methods channel_up(), channel_down() and set_channel() should take this range into account;
The volume's range should be between 1 and 10. The methods volume_up() and volume_down() should take this range into account.
Overview of tv_party.py:
Create an instance object of the TV class;
Part 1:
Turn the TV on;
Set the channel to 3;
Set the volume to 7;
Set the TV off for food break;
Part 2:
Turn the TV on;
Set the channel to 95;
Set the volume to 5;"""


class TV:
    def __init__(self):
        # atributes initialization
        self.channel = 1
        self.volume_level = 1
        self.turned_on = False

    def turn_on(self):
        self.turned_on = True

    
    def turn_off(self):
        self.turned_on = False

    def channel_up(self):
        if self.turned_on: 
            if self.channel < 100: 
                self.channel += 1

    def channel_down(self):
        if self.turned_on:  
            if self.channel > 1:  
                self.channel -= 1

    def set_channel(self, channel):
        if self.turned_on:  
            if 1 <= channel <= 100: 
                self.channel = channel
    def volume_up(self):
        if self.turned_on: 
            if self.volume_level < 10: 
                self.volume_level += 1

    def volume_down(self):
        if self.turned_on: 
            if self.volume_level > 1:  
                self.volume_level -= 1



tv = TV()# creating object TV


tv.turn_on()      
tv.set_channel(3) 
tv.volume_up()    
tv.volume_up()    
tv.volume_up()    
tv.volume_up()    
tv.volume_up()    
tv.volume_up()    
tv.volume_up()    
tv.volume_up()    
tv.turn_off()     


tv.turn_on() 
tv.set_channel(95) 
tv.volume_down()  
tv.volume_down()  
tv.volume_down()  
tv.volume_down()  
tv.volume_down()  
