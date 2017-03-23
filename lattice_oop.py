
#########################################################################################
#
# U(1) Lattice Gauge Theory Simulator | James Graham
#
#########################################################################################

import lattice_site
import parameters

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

numpy.random.seed(0);

#########################################################################################
#
# Here we put a Site into each lattice entry and then call the set_neighbours() function
# along with map() to set all the neighbours in parallel
#
#########################################################################################

for x in xrange(Lx):
    for y in xrange(Ly):
        for t in xrange(Lt):
            lattice[x,y,t] = Site();

map(lattice_site.set_neighbours, lattice)
# for x in xrange(Lx):
#     for y in xrange(Ly):
#         for t in xrange(Lt):
#             lattice[x, y, t].x_next = lattice[(x+1)%Lx, y, t];
#             lattice[x, y, t].x_prev = lattice[(x+Lx-1)%Lx, y, t];
#
#             lattice[x, y, t].y_next = lattice[x, (y+1)%Ly, t];
#             lattice[x, y, t].y_prev = lattice[x, (y+Ly-1)%Ly, t];
#
#             lattice[x, y, t].t_next = lattice[x, y, (t+1)%Lt];
#             lattice[x, y, t].t_prev = lattice[x, y, (t+Lt-1)%Lt];
































#########################################################################################
#
# fin.
#
#########################################################################################
