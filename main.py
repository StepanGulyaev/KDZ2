from tables import *
from slater import *
from graphics import draw_graphs

if __name__ == '__main__':
    project_data = gen_random_projects()
    print("Таблица исключения:")
    draw_exclude_table(project_data)
    print("Множество Парето:")
    pareto = make_pareto(project_data)
    show_pareto(pareto)
    B_matrix = find_intersection_points(dimensions)
    Omega_matrix = get_Omega_matrix(B_matrix)
    draw_slater_exclude_table(project_data,Omega_matrix)
    print(B_matrix)
    print(Omega_matrix)
    draw_graphs(project_data,pareto,B_matrix,Omega_matrix)







