from qutip import *
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

def alpha_sq(epsilon,delta):
    return ((epsilon)**2 )/((delta)**2 + 1/4)
N=10
epsilon = 1
delta = 0
K= 0
K_primes = np.array([0, 1, 5])
times = np.linspace(0, 20, 100)

rho_0 = fock_dm(N,0)
a = destroy(N)
a_dag = create(N)

fig, ax = plt.subplots(1,3, figsize=(14, 7), facecolor='w', edgecolor='k')  #create subplot
axs = 0

for K_prime in K_primes:

    deltas = np.arange(-10,10,0.1)
    photon_num = np.zeros(len(deltas))
    photon_num_analytic = np.zeros(len(deltas))
    g = np.zeros(len(deltas))

    i=0
    for delta in tqdm(deltas):
        H = (delta * a_dag * a + (K/2) * a_dag *a_dag * a * a + 1j * epsilon * (a_dag - a) + (K_prime/3) * (a_dag**3) * (a**3))
        result = mesolve(H,rho_0,times,[a],[a_dag*a,a_dag*a_dag*a*a])
        photon_num = result.expect[0]
        g[i] = (result.expect[1])[-1]/((result.expect[0])[-1])**2
        i+=1

    ax[axs].plot(deltas, g, ".-b", label='numeric')
    ax[axs].set_xlabel('$\Delta$',fontsize="16")
    ax[0].set_ylabel('$<a^{+}a^{+}aa>$',fontsize="16")
    ax[axs].set_title(f'K\' = {K_primes[axs]}')
    ax[axs].legend()

    axs+=1

plt.show()
plt.tight_layout()