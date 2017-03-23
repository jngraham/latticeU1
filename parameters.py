
#########################################################################################
#
# U(1) Lattice Gauge Theory Parameters | James Graham
#
# Here we have all the parameters and things we need
#
#########################################################################################

import numpy as np

#########################################################################################
#
# Here there be parameters
#
#########################################################################################
beta = 2.2;

Lx=10;
Ly=10;
Lt=10;

N_configs_per_sample = 5;
N_samples = 5;

N_equilibration_configs = 200;
N_configs = N_configs_per_sample*N_samples;

lattice = np.empty((Lx, Ly, Lt), dtype = object);

V_size = 200;

mu, sigma = 0, 0.5;
samples = np.random.normal(mu, sigma, V_size/2);

V = np.append(samples, -samples);

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
# fin.
#
#########################################################################################
