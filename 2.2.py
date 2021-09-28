import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

mu=1/(70*365.0)
beta=520/365.0
gamma=1/7.0
TS=1.0
ND=60*365
S0=0.1
I0=1e-4
R0=1-S0-I0
INPUT = (S0, I0, R0)

def diff_eqs(INP,t):
    '''The main set of equations'''
    Y=np.zeros((3))
    V = INP
    Y[0] = mu - beta * V[0] * V[1] - mu * V[0]
    Y[1] = beta * V[0] * V[1] - gamma * V[1] - mu * V[1]
    Y[2] = gamma * V[1] - mu * V[2]
    return Y   # For odeint



t_start = 0.0; t_end = ND; t_inc = TS
t_range = np.arange(t_start, t_end+t_inc, t_inc)
RES = spi.odeint(diff_eqs,INPUT,t_range)

print(RES)

#Ploting
plt.subplot(311)
plt.plot(RES[:,0], '-g', label='Susceptibles')
plt.title('Program_2_2.py')
plt.xlabel('Time')
plt.ylabel('Susceptibles')
plt.subplot(312)
plt.plot(RES[:,1], '-r', label='Infectious')
plt.xlabel('Time')
plt.ylabel('Infectious')
plt.subplot(313)
plt.plot(RES[:,2], '-k', label='Recovereds')
plt.xlabel('Time')
plt.ylabel('Recovereds')
plt.show()