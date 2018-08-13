#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 12:09:37 2018
inheritance: init child + super() (init parent inherited)
polymorphic
@author: yongwei
"""

# ####inheritance
class Parent(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("This is parent")
        
class Child(Parent):  #to inherit from parent
    def __init__(self,name,age,sex):  #Child's initialization
        super(Child,self).__init__(name,age) #Parent initialization
        self.sex = sex
        print("This is child")
        
p = Parent('Jack',20)
# This is parent

c = Child('Jack',20,'male') 
#This is parent
#This is child

# ## advantage1) inherit all methods from parents
class Animal(object):
    def run(self):
        print("Animal can run..")

class Dog(Animal):
    pass
class Cat(Animal):
    pass

dog = Dog()
dog.run() #Animal can run..

cat = Cat()
cat.run() #Animal can run..

# ## advantage2) overlap or add children's unique methods 
class Panda(Animal):
    def run(self):
        print("Panda can run..") #overlapping
    def eat(self):
        print("Panda can eat") # new method
    
panda = Panda()
panda.run()
panda.eat()


# ####polymorphic
# 1)consider class as a type of data type, type checked with isinstance() 
a = list() # list type
b = Animal() #Animal type
c = Panda()  # Panda type

print(isinstance(a,list))   #True
print(isinstance(b,Animal)) #True
print(isinstance(b,Panda))  #False
print(isinstance(c,Animal)) #True
print(isinstance(c,Panda))  #True

# 2)polymorhic: reuse interfaces of different instances 
def run_(animal_instance):
    animal_instance.run()

run_(Animal()) #Animal can run..
run_(Dog())    #Animal can run..
run_(Cat())    #Animal can run..
run_(Panda())  #Panda can run..


