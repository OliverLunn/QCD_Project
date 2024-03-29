from qutip import *
import numpy as np
import matplotlib.pyplot as plt

def matrix(n_states, result,t_steps):

    density_matrix = np.zeros((n_states, n_states,t_steps),dtype=complex)
    for n in range(N):
        for m in range(N):
            density_matrix[n,m,:] = (expect(result.states, projection(n_states, n, m)))
    return density_matrix
        
            
N = 20
K = 0
K_prime = 0
epsilon = 1
times = np.linspace(0, 20, 200)
delta = 0
trace = []

rho_0 = fock_dm(N,0)
a = destroy(N)
a_dag = create(N)

fig,ax = plt.subplots(1)
H = (delta * a_dag * a + (K/2) * a_dag *a_dag * a * a + 1j * epsilon * (a_dag - a) + (K_prime/3)*a_dag*a_dag*a_dag*a*a*a)
result = mesolve(H, rho_0, times,[a])
t_steps = len(times)
density_m = matrix(N, result,t_steps)

for i in range(len(times)):
    trace.append(np.real(np.trace(density_m[:,:,i]@np.conj(density_m[:,:,i]))))


plt.plot(times, trace, "xb")
plt.ylabel("$Tr[\\rho^2]$",fontsize="35")
plt.xlabel("$\kappa t$", fontsize="35")
plt.tick_params('both',labelsize='20')
plt.ylim((-0.1, 1.1))
plt.tight_layout()
plt.show()


