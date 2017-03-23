
#########################################################################################
#
# U(1) Lattice Gauge Theory Lattice Site | James Graham
#
#########################################################################################

import parameters

import numpy as np

#########################################################################################
#
# What does each site need to know?
#
# The phases of each link matrix (complex exponential) going in a positive direction from
# from the site
#
# The nearest neighbour in positive and negative direction. I will initialize these to None
# since we don't know the neighbours until we put the sites on the lattice. We need to have
# neighbour variables because the site won't have access to the lattice when it uses our
# update and field functions, which we define below.
#
# I am being dirty and not making any variables private.
#
#########################################################################################

class Site:

    def __init__(self, x, y, t):

        self.x_coord = x;
        self.y_coord = y;
        self.t_coord = t;

        self.x_link = 0.0;
        self.y_link = 0.0;
        self.t_link = 0.0;

        self.x_next = None;
        self.x_prev = None;
        self.y_next = None;
        self.y_prev = None;
        self.t_next = None;
        self.t_prev = None;

    def set_neighbours(self):

        self.x_next = lattice[(self.x+1)%Lx, y, t];
        self.x_prev = lattice[(self.y+Lx-1)%Lx, y, t]

        self.y_next = lattice[x, (self.y+1)%Ly, t];
        self.y_prev = lattice[x, (self.y+Ly-1)%Ly, t];

        self.t_next = lattice[x, y, (self.t+1)%Lt];
        self.t_prev = lattice[x, y, (self.t+Lt-1)%Lt];

        return None;






























#########################################################################################
#
# fin.
#
#########################################################################################
