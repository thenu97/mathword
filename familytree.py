#!/usr/bin/env python3.8

class Person():
    def __init__(self, name, title, children=None):
        self.name = name
        self.title = title
        if children is None:
            self.children = []
        else:
            self.children = children
    
    def desc(self):
        out = []
        for kid in self.children:
            out.append(kid)
            out.extend(kid.desc())
        return out

p1 = Person("p1", "test")
p2 = Person("p2", "test", children = [p1])
p3 = Person("p3", "test")
p4 = Person("p4", "test", children = [p2, p3])
p5 = Person("p5", "boss", children = [p4])
print [person.title for person in p5.desc()]
print [person.name for person in p5.desc()]