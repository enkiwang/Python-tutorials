# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 21:06:34 2018
looping for: enumerate, zip(), [ x for x in ... ], {key:value for key in [..]}
    1) one seq;2)multiple seq;
    3) create new list [f(var) for var in ..]
    4) create new dict {key:value}

@author: yongweiw
"""



# 1) enumerate() a single sequence, gives index + value

for indx, val in enumerate(['apple','orange','666']):
    print(indx, val)

#0 apple
#1 orange
#2 666


#2) zip(), to loop over two or more sequences
questions = ['name','student_num','age','score']
answers = ['John','123456','8','100']

for q,a in zip(questions, answers):
    print("what's your {0}? It is {1}.".format(q,a))



# 3) looping to create new list: [f(var) for var in range(..)]
new_seq = [x**2 for x in range(3)]
print(new_seq)

text = "word1anotherword23nextone456lastone333"
numbers = [x for x in text if x.isdigit()]
print(numbers)

# ['1', '2', '3', '4', '5', '6', '3', '3', '3']


# 4) looping to create new dict: {key: value for x in [...]}
import os
path_dir = '/path/to/folder'
items_dir = {x: os.path.join(path_dir, x) for x in ['apple_dir','orange_dir','flowers_dir']}

print(items_dir)

#{'apple_dir': '/path/to/folder/apple_dir',
# 'flowers_dir': '/path/to/folder/flowers_dir',
# 'orange_dir': '/path/to/folder/orange_dir'}