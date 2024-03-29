import numpy as np
import matplotlib.pyplot as plt
from qutip import *

def matrix(n_states, result, t_steps):

    density_matrix = np.zeros((n_states, n_states,t_steps),dtype=complex)
    for n in range(N):
        for m in range(N):
            density_matrix[n,m,:] = (expect(result.states, projection(n_states, n, m)))
    return density_matrix

N = 15
K = -1
K_prime = 0
epsilon = 1
delta = 0

times = np.linspace(0, 20, 100)

rho_0 = fock_dm(N,0)
a = destroy(N)
a_dag = create(N)

H = (delta * a_dag * a + (K/2) * a_dag *a_dag * a * a + 1j * epsilon * (a_dag - a))
result = mesolve(H,rho_0,times,[a])

t_steps = len(times)
density_m = matrix(N,result,t_steps)

fig, ax = plt.subplots(1)

for n in range(N):
    ax.bar(n,density_m[n,n,t_steps-1],width=1,color='#72a5f7')
    

ax.set_xlabel('n')
ax.set_ylabel('P(|n>)')
plt.show()
