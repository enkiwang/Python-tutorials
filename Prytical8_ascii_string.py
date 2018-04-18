# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 16:40:27 2018
two tasks: 
    1)convert characters to ASCII numbers: number = ord(char)
    2)convert ASCII numbers to characters: char = chr(number)
    AND combine with usage e.g. [chr(num) for num in numbers], .join() etc
@author: Yongwei
"""

import numpy as np

"********************* character to ASCII number: number=ord(char) *********************"
# Get the ASCII number of a character
chars = ['A', 'a', 's', 't']
numbers = [ord(char) for char in chars]
print(numbers)  # [65, 97, 115, 116]


"********************* ASCII number to character: char=chr(number) *********************"
# Get the character given by an ASCII number
#1) test using numbers
chars1 = [chr(number) for number in numbers]
print(chars1)     # ['A', 'a', 's', 't'] 
    
# 2)test using newly created lists    
numbers_ = np.arange(65, 68)  # step =1
chars_ = [chr(number) for number in numbers_]
print(chars_)  # ['A', 'B', 'C']

"********************* *********************"
string_ = "Hello World!"
string2Val = [ord(char) for char in string_] # [72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100, 33]
print(string2Val)

"********************* ASCII list to string ''.join()*********************"


string_list = [104, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100, 33, 33, 33]
string = ''.join(chr(num) for num in string_list)
print(string)   # hello, world!!!