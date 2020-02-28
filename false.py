#!/usr/bin/env python3.8





array = [1, 2, 0, 0, 0, 3, 4, 5, False, False, True]




def move_zeros(array):
    i = 0
    for i in array:
        if i is False:
            array.remove(0)
            array.append(0)
            continue
        
            
            
    return array
    
    

    
    

print(move_zeros(array))