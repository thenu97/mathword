#!/usr/bin/env python3.8

class Family:
    def __init__(self, grandparents, parents, children):
        self.gp = grandparents
        self.p = parents
        self.c = children
        
class motherside(Family):
    pass
x = ('Grandma: N/A', 'Mother: Nesamma', 'Children: Komathy')
print(x)

print('\n')

class fatherside(Family):
    pass
x = ('Grandpa: N/A', 'Father: Kailapullai', 'Children: Viknarajah')
print(x)
    
class ImmediateFamily:
    def __init__(self, Mother, Father, Me, Second, Third, Fourth, Fifth):
        self.M = Mother
        self.F = Father
        self.Me = Me
        self.S = Second
        self.Th = Third
        self.For = Fourth
        self.Fif = Fifth
    
immdiate_family = ImmediateFamily('Mother: Komathy', 'Father: Viknarajah', 'Me: Thenu', 'Sis: Piruntha', 'Sis: Piraveena', 'Bro: Piravinth', 'Sis: Lanuja')
print(immdiate_family.M)
print(immdiate_family.F)
print(immdiate_family.Me)
print(immdiate_family.S)
print(immdiate_family.Th)
print(immdiate_family.For)
print(immdiate_family.Fif)

