
# coding: utf-8

# In[2]:

#classes: Building, Elevator, Customer
#Equpit bulding with elevator, allow user to customise the number of floors (check for integer)
#Each customer starts on a random floor w/ random destination, only uses elevator once | simulation finished when all at destination

from random import randrange

class Elevator(object):
    def __init__(self):
        self.num_of_floors = building.num_of_floors
        self.cust_in_elevator = []
        self.current_floor = 1
        self.direction = "up"
        
    def move(self):
        if self.current_floor == 1:
            self.current_floor += 1
            self.direction = "up"
        elif self.current_floor == self.num_of_floors:
            self.current_floor -= 1
            self.direction = "down"
        elif self.direction == "up":
            self.current_floor += 1
            self.direction = "up"
        elif self.direction == "down":
            self.current_floor -= 1
            self.direction = "down"
    
    def customer_enters(self, customer):
        building.customer_list.remove(customer)
        self.cust_in_elevator.append(customer)
        
    def customer_leaves(self, customer):
        self.cust_in_elevator.remove(customer)
        building.customer_reached_destination.append(customer)
        
class Building(object):
    def __init__(self, num_of_floors):
        self.num_of_floors = num_of_floors
        self.customer_list = []
        self.customer_reached_destination = []
        
class Customer(object):
    def __init__(self):
        self.destination = randrange(1, building.num_of_floors + 1)
        self.current_floor = randrange(1, building.num_of_floors + 1)
        if self.current_floor == self.destination:
            while self.current_floor == self.destination:
                self.current_floor = randrange(1, building.num_of_floors + 1)
                
number_of_floors = int(input("Number of floors in the building: "))
number_of_customers = int(input("Number of customers in the building: "))
cust_number = number_of_customers
num_of_cust = number_of_customers

building = Building(number_of_floors)
while (num_of_cust != 0):
    building.customer_list.append(Customer())
    num_of_cust -= 1
elevator = Elevator()

reached_dest = 0
elevator_moves = 0
while (len(building.customer_reached_destination) != number_of_customers):
    elevator.move()
    for customer in building.customer_list:
        if elevator.current_floor == customer.current_floor:
            elevator.customer_enters(customer)
    for customer in elevator.cust_in_elevator:
        if elevator.current_floor == customer.destination:
            elevator.customer_leaves(customer)

    #========================================================================================================================
    
    #Remove # to see how many moves of the elevator it takes for all customers to reach their destinations
    
    elevator_moves += 1
    #print ("Number of moves:", elevator_moves)
    
    #Remove # to see the floors the elevator reaches
    
    #print ("The current floor:", elevator.current_floor)
    
    #========================================================================================================================
    
    if reached_dest == len(building.customer_reached_destination):
        pass
    elif reached_dest != len(building.customer_reached_destination):
        print ("%s customers have reached their destination!" % (len(building.customer_reached_destination)))
    reached_dest = len(building.customer_reached_destination)
        
print ("All %s customers have reached their destinations!" % (len(building.customer_reached_destination)))
print ("Number of moves:", elevator_moves)
input()

#Careful of running lots of customers w/ lots of floors (it seems to crash...)
#5 floors 3 customers works fine (as a rule of thumb) -- onwards it gets dodgy... Don't know why...

#Fixed it, customers were not being removed from the building list when they got off the elevator...
#Resulted in customers getting back in the elevator only to immediatley get off as they were on their current floor...


# In[ ]:



