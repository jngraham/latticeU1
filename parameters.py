
#########################################################################################
#
# U(1) Lattice Gauge Theory Parameters | James Graham
#
# Here we have all the parameters we need to create the lattice, that we load into both
# lattice_oop.py and lattice_site.py
#
#########################################################################################

beta = 2.2;

Lx=10;
Ly=10;
Lt=10;

N_configs_per_sample = 5;
N_samples = 5;

N_equilibration_configs = 20;
N_configs = N_configs_per_sample*N_samples;

lattice = np.empty((Lx, Ly, Lt));
