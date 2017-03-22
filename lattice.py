#########################################################################################
#
# U(1) Lattice Gauge Theory Simulator | James Graham
#
#########################################################################################

import numpy as np

Lx=10;
Ly=10;
Lt=10;

#########################################################################################
#
# Our method is to create a numpy array with the appropriate number of sites (array entries).
# Each entry consists of a tuple (x,y,t) indicating the value of the phase of the U(1) element
# pointing away from the site in, respectively, the x, y or t direction.
#
#########################################################################################

lattice = np.full((Lx,Ly,Lt),(0,0,0))

def plusone(int a, int L)
{
return (a+1)%L
}

def minusone(int a, int L)
{
return (a+L-1)%L
}
