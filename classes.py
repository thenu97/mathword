#!/usr/bin/env python3.8


class User: 
    pass # does absolutely nothing
user1 = User()  #calling a method, user1 = object = instance of a class
user1.first_name = "Dave" #first_name = variable, data attached to object = field
user1.second_name = "Bowman"

user2 = User()
user2.first_name ="thenuja"
user2.second_name="jones"

user3 = User()
user3.first_name ="tim"
user3.second_name="peter"



print(user1.first_name, user1.second_name)
print(user2.first_name, user2.second_name)
print(user3.first_name, user3.second_name)

class User2: 
    #pass # does absolutely nothing
    def __init__(self,f_name,l_name):
        self.f_name = f_name
        self.l_name = l_name
    
