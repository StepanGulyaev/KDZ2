from tables import *
from slater import *
from graphics import draw_graphs

if __name__ == '__main__':
    print("Список проектов:")
    project_data = gen_random_projects()
    print("Таблица исключения по Парето:")
    draw_exclude_table(project_data)
    print("Множество Парето:")
    pareto = make_pareto(project_data)
    show_pareto(pareto)
    B_matrix = find_intersection_points(dimensions)
    Omega_matrix = get_Omega_matrix(B_matrix)
    print("Таблица исключения по Слейтеру:")
    draw_slater_exclude_table(project_data,Omega_matrix)
    slater = make_slater(project_data)
    print("Множество Слейтера:")
    show_slater(slater)
    draw_graphs(project_data,pareto,B_matrix,Omega_matrix,slater)







