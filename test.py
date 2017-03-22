import numpy as np
import random

Lx=5;
Ly=5;
Lt=5

random.seed();

beta=2;

lattice=np.zeros((Lx,Ly,Lt,3));

def plusone(a, L):
    return (a+1)%L;

def minusone(a, L):
    return (a+L-1)%L;

# old_link = lattice[2,2,2,0];
# new_link = lattice[1,2,2,0];
#
# print type(old_link);
#
# old_action = np.cos(old_link+new_link);
# new_action = np.cos(new_link);
#
# print type(old_action)
#
# C = np.exp(-beta*old_action)/np.exp(-beta*old_action);
#
# print type(old_action)
#
# z = random.random();
#
# print type(z)
#
# print np.less(z,C)
#
# if z<C: print "Hello"

def xlink(x, y, t):
    old_link = lattice[x,y,t,0];

    print type(old_link);

    new_link = old_link + 0.1;

    # staples in the xy plane; i've dispensed with descriptive variable names now
    staple1 = lattice[plusone(x,Lx),y,t,1]-lattice[x,plusone(y,Ly),t,0]-lattice[x,y,t,1];
    staple2 = 0-lattice[plusone(x,Lx),minusone(y,Ly),t,1]-lattice[x,minusone(y,Ly),t,0]+lattice[x,minusone(y,Ly),t,1];

    print type(staple1)
    print type(staple2)

    # staples in the xt plane
    staple3 = lattice[plusone(x,Lx),y,t,2]-lattice[x,y,plusone(t,Lt),0]-lattice[x,y,t,2];
    staple4 = -lattice[plusone(x,Lx),y,minusone(t,Lt),2]-lattice[x,y,minusone(t,Lt),0]+lattice[x,y,minusone(t,Lt),2];

    print 4*old_link+staple1+staple2;

    old_action = np.cos(4*old_link+staple1+staple2+staple3+staple4);
    new_action = np.cos(4*new_link+staple1+staple2+staple3+staple4);

    # print old_action

    C = np.exp(-beta*new_action)/np.exp(-beta*old_action);

    # print type(C);

    z = random.random();

    # if np.less(z,C):
        # return new_link;
    # else:
    return old_link;

lattice[3,3,3,0]=1;

print xlink(3,3,3);
