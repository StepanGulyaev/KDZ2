import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from tables import *

matplotlib.use('TkAgg')

def draw_Fx(Fx,project_data,pareto,slater,Omega_matrix):

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
        if project_data[i] in slater:
            Fx.plot(project_data[i].f1,project_data[i].f2,'r.',markersize=dot_size)
        elif project_data[i] in pareto and project_data[i] not in slater:
            Fx.plot(project_data[i].f1, project_data[i].f2,'c.',markersize=dot_size)
        else:
            Fx.plot(project_data[i].f1, project_data[i].f2, 'k.', markersize=dot_size)

    #add slater cone
    for i in range(len(slater)):
        k1 = Omega_matrix[0][1] / Omega_matrix[0][0]
        k2 = Omega_matrix[1][1] / Omega_matrix[1][0]
        c1 = slater[i].f2 - k1 * slater[i].f1
        c2 = slater[i].f2 - k2 * slater[i].f1
        j1_1 = np.linspace(0, slater[i].f1, 20)
        j1_2 = np.linspace(slater[i].f1, 5000, 20)
        Fx.plot(j1_1,k2*j1_1+c2,linestyle='-', linewidth=0.5, color='red')
        Fx.plot(j1_2,k1*j1_2+c1,linestyle='-', linewidth=0.5, color='red')


    plt.grid(True)

def draw_mu(mu,B_matrix,Omega_matrix):
    major_ticks = np.arange(-1, 1.1, 0.1)
    minor_ticks = np.arange(-1, 1.1, 0.050)

    mu.set_xticks(major_ticks)
    mu.set_xticks(minor_ticks, minor=True)
    mu.set_yticks(major_ticks)
    mu.set_yticks(minor_ticks, minor=True)

    mu.tick_params(axis='both', which='major', labelsize=10)

    plt.grid(True)

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
    mu.plot(x, y,linestyle='-',linewidth=2,color='black')

    x = np.linspace(mu1_max,mu1_max,20)
    y = np.linspace(mu2_min,mu2_max,20)
    mu.plot(x, y,linestyle='-',linewidth=2,color='black')

    y = np.linspace(mu2_min,mu2_min,20)
    x = np.linspace(mu1_min,mu1_max,20)
    mu.plot(x, y,linestyle='-',linewidth=2,color='black')

    y = np.linspace(mu2_max,mu2_max,20)
    x = np.linspace(mu1_min,mu1_max,20)
    mu.plot(x, y,linestyle='-',linewidth=2,color='black')

    #diagonal

    x = np.linspace(0, 1, 20)
    y = -x + 1
    mu.plot(x, y, linestyle='-', linewidth=2, color='black')

    #intersection_points
    dot_size = 8
    for i in range(len(B_matrix)):
        mu.plot(B_matrix[i][0], B_matrix[i][1], 'r.', markersize=dot_size)

    #vectors_B
    for i in range(len(B_matrix)):
        plt.quiver(0, 0, B_matrix[i][0],B_matrix[i][1], color='b', units='xy',
                   scale=1,label = f"b{i+1} ({B_matrix[i][0]},{B_matrix[i][1]})")

    #vectors_Omega
    for i in range(len(Omega_matrix)):
        plt.quiver(0, 0, Omega_matrix[i][0],Omega_matrix[i][1], color='r', units='xy',
                   scale=1,label = f"o{i+1} ({round(Omega_matrix[i][0],3)},{round(Omega_matrix[i][1],3)})")

    #annotations
    mu.annotate("mu1L", xy=(mu1_min - 0.05,0 - 0.05),fontsize = 8)
    mu.annotate("mu1H", xy=(mu1_max - 0.05, 0 - 0.05),fontsize = 8)
    mu.annotate("mu2L", xy=(-0.1,mu2_min),fontsize = 8)
    mu.annotate("mu2H", xy=(-0.1,mu2_max),fontsize = 8)


    plt.xlabel(r'$mu1,J1$')
    plt.ylabel(r'$mu2,J2$')

    mu.legend(loc=2)




def draw_graphs(project_data,pareto,B_matrix,Omega_matrix,slater):
    windows_size = (9,9)
    plt.figure(figsize=windows_size)
    mu = plt.gca()
    draw_mu(mu,B_matrix,Omega_matrix)
    plt.figure(figsize=windows_size)
    Fx = plt.gca()
    draw_Fx(Fx,project_data,pareto,slater,Omega_matrix)
    plt.show()






