from slater import *
from prettytable import PrettyTable



def all_projects_have_status(project_data):
    for i in range(N):
        if 'x' not in project_data[i].flag_list and \
                '✓' not in project_data[i].flag_list:
            return False
    return True

def all_projects_have_slater_status(project_data):
    for i in range(N):
        if 'x' not in project_data[i].slater_flag_list and \
                '✓' not in project_data[i].slater_flag_list:
            return False
    return True


def get_index_of_first_with_no_status(project_data):
    for i in range(N):
        if 'x' not in project_data[i].flag_list and \
                '✓' not in project_data[i].flag_list:
            return i

def get_index_of_first_with_no_slater_status(project_data):
    for i in range(N):
        if 'x' not in project_data[i].slater_flag_list and \
                '✓' not in project_data[i].slater_flag_list:
            return i

def draw_exclude_table(project_data):
    exclude_table = PrettyTable()
    exclude_table.field_names = ["№","j1", "j2"]
    for i in range(len(project_data)):
        exclude_table.add_row([i+1,project_data[i].f1, project_data[i].f2])

    iteration = 1
    while not all_projects_have_status(project_data):
        flags = []
        i_no_status = get_index_of_first_with_no_status(project_data)
        for i in range(N):
            if project_data[i_no_status].f1 == project_data[i].f1 and \
                    project_data[i_no_status].f2 == project_data[i].f2:
                project_data[i].flag_list.append('✓')
                flags.append('✓')
            elif project_data[i_no_status].f1 <= project_data[i].f1 and \
                    project_data[i_no_status].f2 <= project_data[i].f2:
                if project_data[i].is_excluded():
                    project_data[i].flag_list.append(' ')
                    flags.append(' ')
                else:
                    project_data[i].flag_list.append('x')
                    flags.append('x')
            else:
                project_data[i].flag_list.append(' ')
                flags.append(' ')
        exclude_table.add_column(str(iteration), flags)
        iteration += 1
    flags = []
    for i in range(N):
        if project_data[i].is_excluded():
            flags.append(' ')
        else:
            flags.append('▧')
    exclude_table.add_column(str(iteration), flags)
    print(exclude_table)


def make_pareto(project_data):
    pareto = []
    for project in project_data:
        if not (project.is_excluded()):
            pareto.append(project)
    return pareto

def make_slater(project_data):
    slater = []
    for project in project_data:
        if not (project.is_slater_excluded()):
            slater.append(project)
    return slater


def show_pareto(pareto):
    pareto_table = PrettyTable()
    pareto_table.field_names = ["№", "j1", "j2"]
    for i in range(len(pareto)):
        pareto_table.add_row([pareto[i].number,pareto[i].f1, pareto[i].f2])
    print(pareto_table)

def show_slater(slater):
    slater_table = PrettyTable()
    slater_table.field_names = ["№", "j1", "j2"]
    for i in range(len(slater)):
        slater_table.add_row([slater[i].number,slater[i].f1, slater[i].f2])
    print(slater_table)


def is_p1_dominate_p2(p1,p2,Omega_matrix):
    k1 = Omega_matrix[0][1] / Omega_matrix[0][0]
    k2 = Omega_matrix[1][1] / Omega_matrix[1][0]
    c1 = p1.f2 - k1 * p1.f1
    c2 = p1.f2 - k2 * p1.f1
    if p1.f1 == p2.f1 and p1.f2 == p2.f2:
        return 0
    elif( p2.f2 >= k1 * p2.f1 + c1 and p2.f2 >= k2 * p2.f1 + c2):
        return 1
    else:
        return 2

def draw_slater_exclude_table(project_data,Omega_matrix):
    exclude_slater_table = PrettyTable()
    exclude_slater_table.field_names = ["№","j1", "j2"]
    for i in range(len(project_data)):
        exclude_slater_table.add_row([i+1,project_data[i].f1, project_data[i].f2])

    iteration = 1
    while not all_projects_have_slater_status(project_data):
        flags = []
        i_no_status = get_index_of_first_with_no_slater_status(project_data)
        for i in range(N):
            if is_p1_dominate_p2(project_data[i_no_status],project_data[i],Omega_matrix) == 0:
                project_data[i].slater_flag_list.append('✓')
                flags.append('✓')
            elif is_p1_dominate_p2(project_data[i_no_status],project_data[i],Omega_matrix) == 1:
                if project_data[i].is_slater_excluded():
                    project_data[i].slater_flag_list.append(' ')
                    flags.append(' ')
                else:
                    project_data[i].slater_flag_list.append('x')
                    flags.append('x')
            else:
                project_data[i].slater_flag_list.append(' ')
                flags.append(' ')
        exclude_slater_table.add_column(str(iteration), flags)
        iteration += 1
    flags = []
    for i in range(N):
        if project_data[i].is_slater_excluded():
            flags.append(' ')
        else:
            flags.append('▧')
    exclude_slater_table.add_column(str(iteration), flags)
    print(exclude_slater_table)









