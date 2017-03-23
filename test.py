import numpy as np
import random

class Foo:

    def __init__(self):
        self.bar = 0;

    def add(self):
        self.bar += 1;

L=3;

thing = np.empty((L,L), dtype = object);

for i in range(L):
    for j in range(L):
        thing[i,j] = Foo();

# print type(thing);

# map(lambda example: example.add(), thing);

for i in range(L):
    map(lambda example: example.add(), thing[:,i]);

for i in range(L):
    for j in range(L):
        print thing[i,j].bar;
