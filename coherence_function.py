from qutip import *
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

def alpha_sq(epsilon,delta):
    return ((epsilon)**2 )/((delta)**2 + 1/4)


def g(deltas, K):

    g = np.zeros(len(deltas))
    i=0
    for delta in tqdm(deltas):
        H = (delta * a_dag * a + (K/2) * a_dag *a_dag * a * a + 1j * epsilon * (a_dag - a))
        result = mesolve(H,rho_0,times,[a],[a_dag*a, a_dag*a_dag*a*a])
        g[i] = (result.expect[1])[-1]/(((result.expect[0])[-1])*np.conj(result.expect[0])[-1])
        i+=1
    return np.real(g)

N=15
epsilon = 1
times = np.linspace(0, 20, 100)
deltas = np.arange(-10,25,0.15)

rho_0 = fock_dm(N,0)
a = destroy(N)
a_dag = create(N)

fig, ax = plt.subplots(1,1, figsize=(14, 7), facecolor='w', edgecolor='k')  #create subplot


ax.plot(deltas, g(deltas, 0), ".-b", label='K=0')
ax.plot(deltas, g(deltas, -1), ".-r", label='K=-1')
ax.plot(deltas, g(deltas, -2.5), ".-g", label='K=-2.5')
ax.plot(deltas, g(deltas, -5), ".-k", label='K=-5')
ax.set_xlabel('$\Delta_p$', fontsize="22")
ax.set_ylabel('$g^2(0)$', fontsize="22")
ax.tick_params(axis="x", labelsize=20)
ax.tick_params(axis="y", labelsize=20)
plt.legend(fontsize="22")
plt.show()
plt.tight_layout()