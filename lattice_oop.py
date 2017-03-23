
#########################################################################################
#
# U(1) Lattice Gauge Theory Simulator | James Graham
#
#########################################################################################

from lattice_site import *
from parameters import *

from datetime import datetime

starttime = datetime.now()

#########################################################################################
#
# The code I wrote yesterday is glacially slow and I'd rather not spend 3 weeks waiting
# for it to run! Since the Metropolis algorithm is O(n) I'm going to make it faster using
# parallel processing, but I'm not good enough at computer stuff at this juncture to
# specify all the threads myself, so I will take advantage of python's map() function.
#
# To call map() I need a function and an array (or list or whatever) and the function has
# to act on the elements of the array, be they integers or numpy.float64s or *spoilers*
# lattice sites. The function won't be able to access global variables (constants) like the
# size of the lattice so I need to turn to OOP so that each site knows its coordinates and
# what its successor is.
#
# See lattice_site.py for more info about the objects
#
# I have a file of parameters such as the size of the lattice and so on. And the lattice.
# Even though that's gross. It's empty. Because I want my site objects to be able to access
# the lattice. For this to work, each site needs to know its coordinates.
#
#########################################################################################

import numpy as np
import matplotlib as mp

np.random.seed(0);

#########################################################################################
#
# Here we put a Site into each lattice entry and then call the set_neighbours() function
# along with map() to set all the neighbours in parallel
#
#########################################################################################

for x in xrange(Lx):
    for y in xrange(Ly):
        for t in xrange(Lt):
            lattice[x,y,t] = Site(x,y,t);


for i in xrange(Lx):
    for j in xrange(Ly):
        map(lambda item: item.set_neighbours(), lattice[i,j,:]);

#########################################################################################
#
# I was going to be clever and do this in a chequerboard fashion to parallelize over
# something like
# X X X X X X
#  X X X X X X
# X X X X X X
#  X X X X X X
# X X X X X X
#  X X X X X X
#
# but since I can only make map() work with one-dimensional arrays, i'm kinda stuck
#
#########################################################################################

for k in xrange(N_equilibration_configs):
    for i in xrange(Lx):
        for j in xrange(Ly):
            map(lambda item: item.update_tlink(), lattice[i,j,:]);

    for i in xrange(Lx):
        for j in xrange(Lt):
            map(lambda item: item.update_ylink(), lattice[i,:,j]);

    for i in xrange(Ly):
        for j in xrange(Lt):
            map(lambda item: item.update_xlink(), lattice[:,i,j]);

print datetime.now() - starttime























#########################################################################################
#
# fin.
#
#########################################################################################
