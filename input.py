from project import Project
import random
N = 100
u1_border_min = 0
u2_border_min = 0
u1_border_max = 79
u2_border_max = 79
r = 100 #r is a radius in which one randomly generated project can't contain another one.
        #It was made with purpose to make graph clearer and for more even distribution of values

def distribution_for_random(all_j,j):
    for i in range(len(all_j)):
        if ((all_j[i][0] - j[0])**2 + (all_j[i][1] - j[1])**2 < r**2):
           return True
    return False

def u_exist(all_u,u):
    for i in range(len(all_u)):
        if(all_u[i][0] == u[0] and all_u[i][1] == u[1]):
           return True
    return False

def gen_random_projects():
    all_j = []
    projects = []
    i = 1
    while len(all_j) != N:
        u1 = random.uniform(u1_border_min,u1_border_max)
        u2 = random.uniform(u2_border_min,u1_border_max)
        j1 = 0.2 * (u1 - 70) ** 2 + 0.8 * (u2 - 20) ** 2
        j2 = 0.2 * (u1 - 10) ** 2 + 0.8 * (u2 - 70) ** 2
        j = (j1,j2)
        if not  distribution_for_random(all_j,j):
            all_j.append(j)
            project = Project(j1,j2,i)
            projects.append(project)
            i += 1
    return projects


