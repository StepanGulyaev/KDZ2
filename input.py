from project import Project
from prettytable import PrettyTable
import random

N = 100
u1_border_min = 0
u2_border_min = 0
u1_border_max = 79
u2_border_max = 79
r = 100 #r is a radius in which one randomly generated project can't contain another one.
        #It was made with purpose to make graph clearer and for more even distribution of values

mu1_min = 0.3
mu1_max = 0.4
mu2_min = 0.4
mu2_max = 0.7

def distribution_for_random(all_j,j):
    for i in range(len(all_j)):
        if ((all_j[i][0] - j[0])**2 + (all_j[i][1] - j[1])**2 < r**2):
           return True
    return False

def gen_random_projects():
    all_j = []
    projects = []
    i = 1
    input_table = PrettyTable()
    input_table.field_names = ["№","u1", "u2","j1","j2"]
    while len(all_j) != N:
        u1 = round(random.uniform(u1_border_min,u1_border_max),3)
        u2 = round(random.uniform(u2_border_min,u1_border_max),3)
        j1 = round(0.2 * (u1 - 70) ** 2 + 0.8 * (u2 - 20) ** 2,3)
        j2 = round(0.2 * (u1 - 10) ** 2 + 0.8 * (u2 - 70) ** 2,3)
        j = (j1,j2)
        if not distribution_for_random(all_j,j):
            all_j.append(j)
            project = Project(j1,j2,i)
            projects.append(project)
            input_table.add_row([i,u1,u2,j1,j2])
            i += 1
    print(input_table)
    return projects


