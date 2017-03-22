#########################################################################################
#
# For the U(1) lattice gauge theory problem
#
#########################################################################################

import numpy as np

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
    return 0;

def ylink(x, y, t):
    return 0;

def tlink(x, y, t):
    return 0;
