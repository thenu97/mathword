#!/usr/bin/env python3.8




string = "apples, pears # and bananas\ngrapes\nbananas !apples"

list1 = string.split()

ele = list1.index('#')
ele2 = list1.index('#') + 2
for i in range(ele, ele2 + 1):
    list1.remove(list1[i])


print(list1)