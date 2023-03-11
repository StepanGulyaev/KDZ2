import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from tables import *

matplotlib.use('TkAgg')

def draw_Fx(Fx,project_data,pareto):

    major_ticks = np.arange(-500, 5500, 500)
    minor_ticks = np.arange(-500, 5000, 250)

    Fx.set_xticks(major_ticks)
    Fx.set_xticks(minor_ticks, minor=True)
    Fx.set_yticks(major_ticks)
    Fx.set_yticks(minor_ticks, minor=True)
    Fx.tick_params(axis='both', which='major', labelsize=10)
    Fx.tick_params(axis='both', which='minor', labelsize=10)
    # And a corresponding grid
    Fx.grid(which='both')

    Fx.set_title('Fx',)
    Fx.set_aspect(1)
    Fx.set_xlim((-500, 5000))
    Fx.set_ylim((-500, 5000))
    plt.axhline(0, color='orange')
    plt.axvline(0, color='orange')
    plt.xlabel(r'$j1$')
    plt.ylabel(r'$j2$')

    dot_size = 5
    for i in range(len(project_data)):
        if project_data[i] not in pareto:
            Fx.plot(project_data[i].f1,project_data[i].f2,'k.',markersize=dot_size)
        else:
            Fx.plot(project_data[i].f1, project_data[i].f2,'r.',markersize=dot_size)
    plt.grid(True)

def draw_mu(mu):
    major_ticks = np.arange(-1, 1.1, 0.1)
    minor_ticks = np.arange(-1, 1.1, 0.050)

    mu.set_xticks(major_ticks)
    mu.set_xticks(minor_ticks, minor=True)
    mu.set_yticks(major_ticks)
    mu.set_yticks(minor_ticks, minor=True)

    mu.tick_params(axis='both', which='major', labelsize=10)

    mu.set_title('Mu')
    mu.set_aspect(1)
    mu.set_xlim((-1,1))
    mu.set_ylim((-1,1))
    plt.axhline(0, color='orange')
    plt.axvline(0, color='orange')

    #mu -- lines

    x = np.linspace(mu1_min,mu1_min,20)
    y = np.linspace(0,1,20)
    mu.plot(x, y,linestyle='--',linewidth=2,color='black')

    x = np.linspace(mu1_max,mu1_max,20)
    y = np.linspace(0,1,20)
    mu.plot(x, y,linestyle='--',linewidth=2,color='black')

    y = np.linspace(mu2_min,mu2_min,20)
    x = np.linspace(0,1,20)
    mu.plot(x, y,linestyle='--',linewidth=2,color='black')

    y = np.linspace(mu2_max,mu2_max,20)
    x = np.linspace(0,1,20)
    mu.plot(x, y,linestyle='--',linewidth=2,color='black')

    # mu square lines

    x = np.linspace(mu1_min,mu1_min,20)
    y = np.linspace(mu2_min,mu2_max,20)
    mu.plot(x, y,linestyle='-',linewidth=2,color='red')

    x = np.linspace(mu1_max,mu1_max,20)
    y = np.linspace(mu2_min,mu2_max,20)
    mu.plot(x, y,linestyle='-',linewidth=2,color='red')

    y = np.linspace(mu2_min,mu2_min,20)
    x = np.linspace(mu1_min,mu1_max,20)
    mu.plot(x, y,linestyle='-',linewidth=2,color='red')

    y = np.linspace(mu2_max,mu2_max,20)
    x = np.linspace(mu1_min,mu1_max,20)
    mu.plot(x, y,linestyle='-',linewidth=2,color='red')

    #diagonal

    x = np.linspace(0, 1, 20)
    y = -x + 1
    mu.plot(x, y, linestyle='-', linewidth=2, color='black')

    plt.xlabel(r'$mu1$')
    plt.ylabel(r'$mu2$')
    plt.grid(True)


def draw_graphs(project_data,pareto):
    windows_size = (9,9)
    plt.figure(figsize=windows_size)
    mu = plt.gca()
    draw_mu(mu)
    plt.figure(figsize=windows_size)
    Fx = plt.gca()
    draw_Fx(Fx,project_data,pareto)
    plt.show()






