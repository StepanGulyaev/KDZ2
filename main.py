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
    grey_code_matrix = make_grey_code_matrix(dimensions)
    mu_matrix = make_mu_matrix(grey_code_matrix)
    B_matrix = find_intersection_points(mu_matrix)
    print(grey_code_matrix)
    print(mu_matrix)
    print(B_matrix)
    #draw_graphs(project_data,pareto)







