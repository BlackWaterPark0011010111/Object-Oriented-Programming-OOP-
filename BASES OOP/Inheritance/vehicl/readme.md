Python OOP Concepts - Transport vehicles
In this exercise we will check how inheritance in Python and the usage of the super() built-in method and self work in connection with multiple inheritance.

The problem
You are working for the Berlin city traffic planning office. The system the office is using has been used for many years and it used to monitor all kinds of transport related things. The system classifies all types of vehicles present in the city by means of a large number of classes and subclasses. The class for each vehicle is ultimately derived from the super class Vehicle. Each subclass is adding methods and variables that are relevant just for that type of vehicle.

This has worked for a long time, but yesterday the mayor announced that the city will be rolling out a new type of public transportation: bicycle taxis. These need to be classified both under "public transport vehicles" and under "bikes" which hitherto had been two separate and incompatible categories in the system. Bikes had been assumed to always be without a motor and public transport vehicles had been assumed to always have a motor.

You are being called in as an expert to make a change to the system that should affect the system as little as possible but still manages to add bike taxis, both with and without motors, to the system. You only get to work on those classes that are relevant for your work, but you know that there are many more sub classes (for cars, ships, airplanes, buses, the metro, etc.) that all rely on the rest of the system to continue to work as it does.

Overview of vehicle.py:
The Vehicle class represents any kind of transport vehicle.
It has attributes specifying the speed, the maximum_mileage and whether or not it is motorized.
It has a protected attribute __scrap_metal that keeps track of whether the vehicle can still drive or whether it is scrap metal.
It prints "Ready to go!" after being initialized and this message should only be printed once for each vehicle.
It has a method drive(km: int) -> bool. This method checks whether the vehicle is not yet scrap metal and if that is not the case, it prints how many kilometers the vehicle is driving. It subtracts the number of km from the maximum_mileage. If the maximum_mileage ends up under 0, it sets the __scrap_metal attribute to True. It will return True if the vehicle is able to drive the requested amount and otherwise False.
No extra action should be taken here.
Overview of public_transport.py
The PublicTransport class subclasses Vehicle. Public transport is normally motorized, so it calls the Vehicle constructor setting motorized to True it forwards all other values. It adds a protected attribute __current_passengers and adds public methods enter_passengers(num: int), exit_passengers(num: int) and get_current_passengers() -> int to obtain the current number of passengers.
Modify the constructor method of PublicTransport so that it only specifies motorized if it has not yet been specified.
Overview of bike.py
The Bike class subclasses Vehicle. Bikes are normally not motorized, so it calls the Vehicle constructor setting motorized to False and speed to 20. It adds a private attribute _mileage_until_next_repair that is initiated at 200. It adds a method called repair() that resets the _mileage_until_next_repair to 200. It's maximum_mileage is 600.
It overrides the drive(km: int) method, checking whether _mileage_until_next_repair is above 0, and if this is the case, it subtracting the km from the _mileage_until_next_repair and calls the drive(km: int) method of the parent class.
Modify the constructor method of Bike so that it only sets the speed if no speed has been specified yet and only specifies motorized if it has not yet been specified.
Overview of bike_taxi.py
You need to modify the BikeTaxi class so that it subclasses both PublicTransport and Bike. It should be created to so that it has all the methods and attributes of both parent classes. Bike taxis exist both with and without a motor, so the constructor method needs to accept an argument specifying whether or not it is motorized by initiating it as BikeTaxi(motorized: bool).
A motorized bike taxi can carry 4 passengers and a non-motorized bike taxi can carry 2 passengers.
A motorized bike has a speed of 30 and a non-motorized bike taxi has a speed of 18.
It should override the enter_passengers(num: int) method, checking that there are never more than the allowed number of passengers onboard at a time and printing the error "Cannot load more passengers at this time." if there are too many. If the number of passengers is acceptable, it should call the enter_passengers(num: int) method of the PublicTransport class.
Overview of app.py:
This is where the main method resides, therefore this is where your code should be executed. A motorized and a non-motorized bike taxi are initiated. Both bike taxis are then driven around town until they turn into scrap metal.