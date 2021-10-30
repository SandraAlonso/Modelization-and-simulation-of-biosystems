import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# parameter values
R0 = 4
t_incubation = 10.0
t_infective = 6.0
vacune = 0.005

# initial number of infected and recovered individuals
i_initial = 1/20000
e_initial = 0.00
r_initial = 0.00
s_initial = 1 - e_initial - i_initial - r_initial

alpha = 1/t_incubation
gamma = 1/t_infective
beta = R0*gamma


# SEIR model differential equations.
def deriv(x, t, alpha, beta, gamma, vacune):
    s, e, i, r = x
    if(t<55):
        vacune=0.0
    else:
        vacune=0.05
    dsdt = -beta * s * i -s*vacune
    dedt =  beta * s * i - alpha * e
    didt = alpha * e - gamma * i
    drdt =  (gamma * i)*0.02 + s*vacune

    return [dsdt, dedt, didt, drdt]

t = np.linspace(0, 160, 160)
x_initial = s_initial, e_initial, i_initial, r_initial
soln = odeint(deriv, x_initial, t, args=(alpha, beta, gamma, vacune))
s, e, i, r = soln.T
print(r)




def plotdata(t, s, i, e):
    # plot the data
    fig = plt.figure(figsize=(12,6))
    ax = [fig.add_subplot(221, axisbelow=True), 
          fig.add_subplot(223),
          fig.add_subplot(122)]

    ax[0].plot(t, s, lw=1, label='Susceptible')
    ax[0].plot(t, i, lw=1, label='Infected')
    ax[0].plot(t, r, lw=1, label='Recovered')
    ax[0].set_title('Susceptible and Recovered Populations')
    ax[0].set_xlabel('Time /days')
    ax[0].set_ylabel('Fraction')
    ax[0].plot([55, 55], [0, 1], '--', lw=2, label='vaccine is created')


    ax[1].plot(t, i, lw=1, label='Infective')
    ax[1].set_title('Infectious Population')
    if e is not None: ax[1].plot(t, e, lw=1, label='Exposed')
    ax[1].set_ylim(0, 0.3)
    ax[1].set_xlabel('Time /days')
    ax[1].set_ylabel('Fraction')

    ax[2].plot(s, i, lw=1, label='s, i trajectory')
    ax[2].plot([1/R0, 1/R0], [0, 1], '--', lw=3, label='di/dt = 0')
    ax[2].plot(s[0], i[0], '.', ms=20, label='Initial Condition')
    ax[2].plot(s[-1], i[-1], '.', ms=20, label='Final Condition')
    ax[2].set_title('State Trajectory')
    ax[2].set_aspect('equal')
    ax[2].set_ylim(0, 1.05)
    ax[2].set_xlim(0, 1.05)
    ax[2].set_xlabel('Susceptible')
    ax[2].set_ylabel('Infectious')

    for a in ax: 
        a.grid(True)
        a.legend()

    plt.tight_layout()

    plt.show()



plotdata(t, s, i, e)