
#########################################################################################
#
# U(1) Lattice Gauge Theory Simulator | James Graham
#
#########################################################################################

import numpy as np;
import matplotlib as mp;
import random;
import math;

random.seed(1);

#########################################################################################
#
# Our method is to create a numpy array with the appropriate number of sites (array entries).
# The link is accessed through the fourth coordinate in the array, which is 0, 1 or 2,
# corresponding to links int the x, y, t directions.
#
# We will have update methods for the x, y and t links, which will be largely identical.
# Then we will iterate through the sites on the lattice until we have gone through once
# Then we do it again.
#
# First we define some global constants and the array
#
#########################################################################################

beta = 2.2;

Lx=10;
Ly=10;
Lt=10;

N_configs_per_sample = 50;
N_samples = 50;

N_equilibration_configs = 200;
N_configs = N_configs_per_sample*N_samples;

lattice = np.zeros((Lx, Ly, Lt,3));

n_links = 3*Lx*Ly*Lt;
n_transitions = n_links*(N_configs+N_equilibration_configs);
n_acceptances = 0;

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
jPC_plus = np.zeros((Lt, N_configs));
jPC_minus = np.zeros((Lt, N_configs));
wilson_loop = np.zeros((Lt, N_configs));

#########################################################################################
#
# Because numpy arrays can handle negative indices but not large positive ones, we
# rewrite our addition- and subtraction-by-one so we don't have to think too hard when
# updating our link matrices.
#
#########################################################################################

def plusone(a, L):
    return (a+1)%L;

def minusone(a, L):
    return (a+L-1)%L;

#########################################################################################
#
# Create a set of random phases within +-Pi/6 ~0.5. They need to come in +- pairs to ensure
# ergodicity. We also need sufficiently many to help with ergodicity.
#
#########################################################################################

V_size = 200;

mu, sigma = 0, 0.5;
samples = np.random.normal(mu, sigma, V_size/2);

V = np.append(samples, -samples);

#########################################################################################
#
# Create our set of x, y and t link update functions
#
#########################################################################################

def xlink(x, y, t):
    old_link = lattice[x,y,t,0];
    new_link = old_link + random.choice(V);

    # staples in the xy plane; i've dispensed with descriptive variable names now
    staple1 = lattice[plusone(x,Lx),y,t,1] - lattice[x,plusone(y,Ly),t,0] - lattice[x,y,t,1];
    staple2 = -lattice[plusone(x,Lx),minusone(y,Ly),t,1] - lattice[x,minusone(y,Ly),t,0] + lattice[x,minusone(y,Ly),t,1];

    # staples in the xt plane
    staple3 = lattice[plusone(x,Lx),y,t,2] - lattice[x,y,plusone(t,Lt),0] - lattice[x,y,t,2];
    staple4 = -lattice[plusone(x,Lx),y,minusone(t,Lt),2] - lattice[x,y,minusone(t,Lt),0] + lattice[x,y,minusone(t,Lt),2];

    old_action = np.cos(4 * old_link + staple1 + staple2 + staple3 + staple4);
    new_action = np.cos(4 * new_link + staple1 + staple2 + staple3 + staple4);

    C = np.exp(-beta * new_action) / np.exp(-beta * old_action);

    z = np.random.random();

    if z<C:
        # n_acceptances += 1
        return new_link;
    else:
        return old_link;

def ylink(x, y, t):
    old_link = lattice[x,y,t,1];
    new_link = old_link + random.choice(V);

    # staples in the xy plane
    staple1 = lattice[x,plusone(y,Ly),t,0] - lattice[plusone(x,Lx),y,t,1] - lattice[x,y,t,0];
    staple2 = -lattice[minusone(x,Lx),plusone(y,Ly),t,0] - lattice[minusone(x,Lx),y,t,1] + lattice[minusone(x,Lx),y,t,0];

    # staples in the yt plane
    staple3 = lattice[x,plusone(y,Ly),t,2] - lattice[x,y,plusone(t,Lt),1] - lattice[x,y,t,2];
    staple4 = -lattice[x,plusone(y,Ly),minusone(t,Lt),2] - lattice[x,y,minusone(t,Lt),1] + lattice[x,y,minusone(t,Lt),2];

    old_action = np.cos(4 * old_link + staple1 + staple2 + staple3 + staple4);
    new_action = np.cos(4 * new_link + staple1 + staple2 + staple3 + staple4);

    C = np.exp(-beta * new_action) / np.exp(-beta * old_action);

    z = random.random();

    if np.less(z,C):
        # n_acceptances += 1
        return new_link;
    else:
        return old_link;

def tlink(x, y, t):
    old_link = lattice[x,y,t,2];
    new_link = old_link + random.choice(V);

    # staples in the xt plane
    staple1 = lattice[x,y,plusone(t,Lt),0] - lattice[plusone(x,Lx),y,t,2] - lattice[x,y,t,0];
    staple2 = -lattice[minusone(x,Lx),y,plusone(t,Lt),0] - lattice[minusone(x,Lx),y,t,2] + lattice[minusone(x,Lx),y,t,0];

    # staples in the yt plane
    staple3 = lattice[x,y,plusone(t,Lt),1] - lattice[x,plusone(y,Ly),t,2] - lattice[x,y,t,1];
    staple4 = -lattice[x,minusone(y,Ly),plusone(t,Lt),1] - lattice[x,minusone(y,Ly),t,2] + lattice[x,minusone(y,Ly),t,1];

    old_action = np.cos(4 * old_link + staple1 + staple2 + staple3 + staple4);
    new_action = np.cos(4 * new_link + staple1 + staple2 + staple3 + staple4);

    C = np.exp(-beta * new_action) / np.exp(-beta * old_action);

    z = random.random();

    if np.less(z,C):
        # n_acceptances += 1;
        return new_link;
    else:
        return old_link;

##########################################################################################
#
# Creates our set of operator functions
#
#########################################################################################

def plaquette_operator(nparray):

    n_plaquettes = 3*Lx*Ly*Lt;
    plaquette_sum=0.0;

    for x in xrange(Lx):
        for y in xrange(Ly):
            for t in xrange(Lt):
                xt_phase = lattice[x,y,t,0] + lattice[plusone(x,Lx),y,t,2] - lattice[x,y,plusone(t,Lt),0] - lattice[x,y,t,2];
                xy_phase = lattice[x,y,t,0] + lattice[plusone(x,Lx),y,t,1] - lattice[x,plusone(y,Ly),t,0] - lattice[x,y,t,1];
                yt_phase = lattice[x,y,t,1] + lattice[x,plusone(y,Ly),t,2] - lattice[x,y,plusone(t,Lt),1] - lattice[x,y,t,2];

                plaquettes = np.cos(xt_phase) + np.cos(xy_phase) + np.cos(yt_phase);

                plaquette_sum += plaquettes;

    return plaquette_sum / n_plaquettes;

def m_plus(nparray, zero):
    return 0;

def m_minus(nparray, zero):
    return 0;

def flux(nparray, zero):
    return 0;

#########################################################################################
#
# Update our lattice appropriately many times to erase the memory of the zeros, then
# do the "science run" and put data into our data arrays
#
#########################################################################################

for i in xrange(N_equilibration_configs):
    for x in xrange(Lx):
        for y in xrange(Ly):
            for t in xrange(Lt):
                lattice[x,y,t,0] = xlink(x,y,t);
                lattice[x,y,t,1] = ylink(x,y,t);
                lattice[x,y,t,2] = tlink(x,y,t);

for j in xrange(N_configs):
    for x in xrange(Lx):
        for y in xrange(Ly):
            for t in xrange(Lt):
                lattice[x,y,t,0] = xlink(x,y,t);
                lattice[x,y,t,1] = ylink(x,y,t);
                lattice[x,y,t,2] = tlink(x,y,t);

    # print lattice[:,: ,0,0]

    avg_plaquette[j]=plaquette_operator(lattice);

print "mean plaquette = " + np.mean(avg_plaquette)

print "acceptance rate = " + float(n_acceptances)/n_transitions;

#########################################################################################
#
# Here we save some time by evaluating the m++, m-- and flux operators at n_t=0,
# then passing them into the functions that get the products of operators
#
#########################################################################################

    # plus_zero=0;
    # minus_zero=0;
    # flux_zero=0;
    #
    # for t in xrange(Lt):
    #     jPC_plus[t,j]=m_plus(lattice, plus_zero);
    #     jPC_minus[t,j]=m_minus(lattice, minus_zero);
    #     wilson_loop[t,j]=flux(lattice, flux_zero);
