# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 16:38:02 2018
generator type: using next() to iterate one by one. 
@author: yongweiw
"""

def myGenerator_word():
    yield 'Generator'
    yield 'similar'
    yield 'to'
    yield 'iterator'
    yield 'one'
    yield 'word'
    yield 'at'
    yield 'a'
    yield 'time'
    
my_gen_word = myGenerator_word()

print(next(my_gen_word))


def myGenerator_num(n):
    yield n
    yield n + 1
    yield n ** 2
    
my_gen_num = myGenerator_num(10)
print(next(my_gen_num))


# assuming a net class loaded with net.state_dict(torch.load(PATH))
for param in net.parameters():
    print(next(param))
    param.requires_grad = False   