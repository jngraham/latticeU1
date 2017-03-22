#########################################################################################
#
# U(1) Lattice Gauge Theory Simulator | James Graham
#
#########################################################################################

import numpy as np
import matplotlib as mp

#########################################################################################
#
# Our method is to create a numpy array with the appropriate number of sites (array entries).
# Each entry consists of a tuple (x,y,t) indicating the value of the phase of the U(1) element
# pointing away from the site in, respectively, the x, y or t direction.
#
# We will have update methods for the x, y and t links, which will be largely identical.
# Then we will iterate through the sites on the lattice until we have gone through once
# Then we do it again.
#
# First we define some global length variables and the array
#
#########################################################################################

Lx=10;
Ly=10;
Lt=10;

N_configs_per_sample = 1;
N_samples = 1;

N_equilibration_configs = 1;
N_configs = N_configs_per_sample*N_samples;

lattice = np.full((Lx, Ly, Lt), (0, 0, 0));

#########################################################################################
#
# Define arrays in which to store our data. The average plaquette gives us one value per field configuration
# whereas the glueball masses and the string tension come from are functions of n_t.
#
# Recall each energy comes from \langle \Phi^\dagger(n_t)\Phi(0)\rangle \propto e^{-a E n_t}
# So we calculat the \Phi^\dagger(n_t)\Phi(0) for every n_t in the lattice using the definitions
# given on the problem sheet and populate our arrays appropriately.
#
# It will take fitting lines to log-lin graphs to extract the energies. I may do that
# in here or with Mathematica.
#
#########################################################################################

avg_plaquette = np.zeros(N_configs);
jPC_plus = np.zeros(Lt, N_configs);
jPC_minus = np.zeros(Lt, N_configs);
wilson_loop = np.zeros(Lt, N_configs);

#########################################################################################
#
# Create a set of random phases within +-Pi/6 ~0.5. They need to come in +- pairs to ensure
# ergodicity. We also need sufficiently many to help with ergodicity.
#
#########################################################################################

V_size = 200;

mu, sigma = 0, 0.5;
samples = np.random.normal(mu, sigma, V_size%2);

V = np.append(samples, -samples);

#########################################################################################
#
# Create our set of x, y and t link update functions
#
#########################################################################################

def xlink(int x, int y, int t)
{
return 0;
}

def ylink(int x, int y, int t)
{
return 0;
}
def tlink(int x, int y, int t)
{
return 0;
}
#########################################################################################
#
# Redefine how we add and subtract one to indices so I don't have to worry about the edges
# of the lattice because I am lazy
#
#########################################################################################

def plusone(int a, int L)
{
return (a+1)%L;
}

def minusone(int a, int L)
{
return (a+L-1)%L;
}
