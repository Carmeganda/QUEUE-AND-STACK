#QUEUETYPES
from collections import deque
from heapq import heappop, heappush
from dataclasses import dataclass
from itertools import count


# Building a Queue Data Type
class Iterable:
    def __len__(self):
      return len(self._elements)

    def __iter__(self):
      while len(self) > 0:
        yield self.dequeue()

class Queue(Iterable):
    def __init__(self, *elements):
      self._elements = deque(elements)

    def enqueue(self, element):
      self._elements.append(element)

    def dequeue(self):
      return self._elements.popleft()

# Building a Stack Data Type
class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()

# Building a Priority Queue Data Type
class PriorityQueue(Iterable):
    def __init__(self):
        self._elements = []
        self._counter = count()
    
    def enqueue_with_priority(self, priority, value):
        element = (-priority, next(self._counter), value)
        heappush(self._elements, element)

    def dequeue(self):
        return heappop(self._elements)[-1]

# Handling Corner Cases in Your Priority Queue

#HEAP

from heapq import heappush, heappop

fruits = []

# pushing elements to fruits list 
from heapq import heappush

fruits = []
heappush(fruits, "orange")
heappush(fruits, "apple")
heappush(fruits, "banana")
heappush(fruits, "guava")
print(fruits)

# removing the first element in fruits list
from heapq import heappop

heappop(fruits)
'apple'
heappop(fruits)
'banana'
heappush(fruits,"mango")
print(fruits)

# tuple comparison
person1 = ("John", "Brown", 42)
person2 = ("John", "Doe", 42)
person3 = ("John", "Doe", 24)

print(person1 < person2)
print(person2 < person3)

#STACK
lifo = []

lifo.append("1st")
lifo.append("2nd")
lifo.append("3rd")

lifo = Stack("1st", "2nd", "3rd")
for element in lifo:
 print(element)


#SECONDELEMENTS

fifo = Queue("1st", "2nd", "3rd")
print(len(fifo))


# dequeueing elements because  of iter method
for element in fifo:
  print(element)

print(len(fifo)) # output: 0

class PriorityQueue:
    def __init__(self):
        self._elements = []

    def enqueue_with_priority(self, priority, value):
        heappush(self._elements, (priority, value))

    def dequeue(self):
        return heappop(self._elements)

CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1

messages = PriorityQueue()
messages.enqueue_with_priority(IMPORTANT, "Windshield wipers turned on")
messages.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
messages.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
messages.enqueue_with_priority(IMPORTANT, "Hazard lights turned on")

class PriorityQueue:
    def __init__(self):
        self._elements = []

    def enqueue_with_priority(self, priority, value):
        heappush(self._elements, (-priority, value))

    def dequeue(self):
        return heappop(self._elements)[-1]

print(messages.dequeue())
