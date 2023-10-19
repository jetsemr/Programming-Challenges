# Author: Jet Semrick
# Date: 10-19-2023
# Problem: An animal shelter holds dogs and cats. Create a data structure that is FIFO.
# Source: 3.6 from pg. 99 Cracking the Coding Interview

import sys
sys.path.append('..')
# pylint: disable=import-error
import structures

class Animal:
  def __init__(self, animal, num):
    self.animal = animal
    self.num = num
 
class AnimalShelter:
  def __init__(self):
    self.dogs = structures.Queue()
    self.cats = structures.Queue()
    self.arrivalNum = 0
  
  def enqueue(self, value):
    self.arrivalNum += 1
    animal = Animal(value, self.arrivalNum)
    
    if value == 'dog':
      self.dogs.enqueue(animal)
    elif value == 'cat':
      self.cats.enqueue(animal)
    else:
      raise Exception("Not a cat or dog.")
  
  def dequeueAny(self):
    if not self.dogs.isEmpty() and not self.cats.isEmpty():
       if (self.dogs.peek().num < self.cats.peek().num):
          return self.dogs.dequeue()
       else:
          return self.cats.dequeue()
    elif (not self.dogs.isEmpty()):
       return self.dogs.dequeue()
    else:
       return self.cats.dequeue()
  
  def dequeueDog(self):
    return self.dogs.dequeue()
  def dequeueCat(self):
    return self.cats.dequeue()

# Test Cases

shelter = AnimalShelter()
shelter.enqueue('dog')
shelter.enqueue('cat')
a = shelter.dequeueAny()
print(a.animal, a.num)
shelter.enqueue('dog')
shelter.enqueue('dog')
shelter.enqueue('dog')
shelter.enqueue('dog')
shelter.enqueue('dog')
shelter.enqueue('dog')
shelter.enqueue('dog')
shelter.enqueue('dog')
a = shelter.dequeueAny()
print(a.animal, a.num)
a = shelter.dequeueDog()
print(a.animal, a.num)
shelter.enqueue('cat')
a = shelter.dequeueCat()
print(a.animal, a.num)

