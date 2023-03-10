import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from tables import *

matplotlib.use('TkAgg')

def draw_field(field):
    major_ticks = np.arange(-500, 5000, 500)
    minor_ticks = np.arange(-500, 5000, 250)

    field.set_xticks(major_ticks)
    field.set_xticks(minor_ticks, minor=True)
    field.set_yticks(major_ticks)
    field.set_yticks(minor_ticks, minor=True)
    field.tick_params(axis='both', which='major', labelsize=10)
    field.tick_params(axis='both', which='minor', labelsize=10)
    # And a corresponding grid
    field.grid(which='both')

    field.set_title('sus',)
    field.set_aspect(1)
    field.set_xlim((-500, 5000))
    field.set_ylim((-500, 5000))
    plt.axhline(0, color='orange')
    plt.axvline(0, color='orange')
    plt.xlabel(r'$j1$')
    plt.ylabel(r'$j2$')
    plt.grid(True)


def draw_pareto_projects(project_data,pareto):
    plt.figure(figsize=(10, 10))
    field = plt.gca()
    draw_field(field)
    dot_size = 5
    for i in range(len(project_data)):
        if project_data[i] not in pareto:
            field.plot(project_data[i].f1,project_data[i].f2,'k.',markersize=dot_size)
        else:
            field.plot(project_data[i].f1, project_data[i].f2,'r.',markersize=dot_size)
    plt.show()

def draw_cluster_projects(project_data):
    plt.figure(figsize=(10, 10))
    field = plt.gca()
    draw_field(field)
    dot_size = 5
    for i in range(len(project_data)):
        if project_data[i].cluster == 1:
            field.plot(project_data[i].f1,project_data[i].f2,'r.',markersize=dot_size)
        elif project_data[i].cluster == 2:
            field.plot(project_data[i].f1, project_data[i].f2,'g.',markersize=dot_size)
        elif project_data[i].cluster == 3:
            field.plot(project_data[i].f1, project_data[i].f2, 'b.',markersize=dot_size)
    plt.show()




