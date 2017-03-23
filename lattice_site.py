
#########################################################################################
#
# U(1) Lattice Gauge Theory Lattice Site | James Graham
#
#########################################################################################

from parameters import *

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

        x = self.x_coord;
        y = self.y_coord;
        t = self.t_coord;

        self.x_next = lattice[(x+1)%Lx, y, t];
        self.x_prev = lattice[(x+Lx-1)%Lx, y, t]

        self.y_next = lattice[x, (y+1)%Ly, t];
        self.y_prev = lattice[x, (y+Ly-1)%Ly, t];

        self.t_next = lattice[x, y, (t+1)%Lt];
        self.t_prev = lattice[x, y, (t+Lt-1)%Lt];

        return None;

    def update_xlink(self):

        staple1 = self.x_next.y_link - self.y_next.x_link - self.y_link;
        staple2 = - self.x_next.y_prev.y_link - self.y_prev.x_link + self.y_prev.y_link;
        staple3 = self.x_next.t_link - self.t_next.x_link - self.t_link;
        staple4 = - self.x_next.t_prev.t_link - self.t_prev.x_link + self.t_prev.t_link;

        old_link = self.x_link;
        new_link = old_link + np.random.choice(V);

        old_action = np.cos(old_link + staple1) + np.cos(old_link + staple2) + np.cos(old_link + staple3) + np.cos(old_link + staple4);
        new_action = np.cos(new_link + staple1) + np.cos(new_link + staple2) + np.cos(new_link + staple3) + np.cos(new_link + staple4);

        C = np.exp(-beta * new_action)/np.exp(-beta * old_action);

        z = np.random.random();

        if z<C:
            self.x_link = new_link;

        return None;

    def update_ylink(self):

        staple1 = self.y_next.x_link - self.x_next.y_link - self.x_link;
        staple2 = - self.y_next.x_prev.x_link - self.x_prev.y_link + self.x_prev.x_link;
        staple3 = self.y_next.t_link - self.t_next.y_link - self.t_link;
        staple4 = - self.y_next.t_prev.t_link - self.t_prev.y_link + self.t_prev.t_link;

        old_link = self.y_link;
        new_link = old_link + np.random.choice(V);

        old_action = np.cos(old_link + staple1) + np.cos(old_link + staple2) + np.cos(old_link + staple3) + np.cos(old_link + staple4);
        new_action = np.cos(new_link + staple1) + np.cos(new_link + staple2) + np.cos(new_link + staple3) + np.cos(new_link + staple4);

        C = np.exp(-beta * new_action)/np.exp(-beta * old_action);

        z = np.random.random();

        if z<C:
            self.y_link = new_link;

        return None;

    def update_tlink(self):

        staple1 = self.t_next.x_link - self.x_next.t_link - self.x_link;
        staple2 = - self.t_next.x_prev.x_link - self.x_prev.t_link + self.x_prev.x_link;
        staple3 = self.t_next.y_link - self.y_next.t_link - self.y_link;
        staple4 = - self.t_next.y_prev.y_link - self.y_prev.t_link + self.y_prev.y_link;

        old_link = self.t_link;
        new_link = old_link + np.random.choice(V);

        old_action = np.cos(old_link + staple1) + np.cos(old_link + staple2) + np.cos(old_link + staple3) + np.cos(old_link + staple4);
        new_action = np.cos(new_link + staple1) + np.cos(new_link + staple2) + np.cos(new_link + staple3) + np.cos(new_link + staple4);

        C = np.exp(-beta * new_action)/np.exp(-beta * old_action);

        z = np.random.random();

        if z<C:
            self.t_link = new_link;

        return None;






























#########################################################################################
#
# fin.
#
#########################################################################################
