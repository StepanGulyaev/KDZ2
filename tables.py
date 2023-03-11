from input import *
from prettytable import PrettyTable



def all_projects_have_status(project_data):
    for i in range(N):
        if 'x' not in project_data[i].flag_list and \
                '✓' not in project_data[i].flag_list:
            return False
    return True


def get_index_of_first_with_no_status(project_data):
    for i in range(N):
        if 'x' not in project_data[i].flag_list and \
                '✓' not in project_data[i].flag_list:
            return i


def draw_exclude_table(project_data):
    exclude_table = PrettyTable()
    exclude_table.field_names = ["№","f1", "f2"]
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

def show_pareto(pareto):
    pareto_table = PrettyTable()
    pareto_table.field_names = ["№", "f1", "f2"]
    for i in range(len(pareto)):
        pareto_table.add_row([pareto[i].number,pareto[i].f1, pareto[i].f2])
    print(pareto_table)








