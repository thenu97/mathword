#!/usr/bin/env python3.8
from random import choice 
import string
password_generator = True
while password_generator == True:
    characters = string.punctuation + string.ascii_letters + string.digits
    pass_len = int(input("How long do you want your password to be?: "))
    password = "".join(choice(characters) for x in range(0, pass_len))
    print(password)
    pass_again = input("Generate another password (Y/N): ")
    if pass_again.lower() == 'Y':
        continue
    else:
        password_generator = False
exit()

