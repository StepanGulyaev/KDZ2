from input import *
dimensions = 2
def make_grey_code_matrix(dimensions):
    grey_code_matrix = []
    for i in range(pow(2,dimensions)):
        grey_code = bin(i ^ i>>1)[2:].zfill(dimensions)
        row = []
        for i in range(dimensions):
            row.append(grey_code[i])
        grey_code_matrix.append(row)
    return grey_code_matrix

def make_mu_matrix(grey_code_matrix):
    mu_matrix = []
    for i in range(len(grey_code_matrix)):
        row=[]
        for j in range(len(grey_code_matrix[i])):
            row.append(None)
        mu_matrix.append(row)

    for i in range(len(grey_code_matrix)):
        if grey_code_matrix[i][0] == '0':
            mu_matrix[i][0] = mu1_min
        else:
            mu_matrix[i][0] = mu1_max

        if grey_code_matrix[i][1] == '0':
            mu_matrix[i][1] = mu2_min
        else:
            mu_matrix[i][1] = mu2_max

    return mu_matrix

def find_intersection_points(mu_matrix):
    B_matrix=[]
    for i in range(len(mu_matrix)-1):
        L_mu = (mu_matrix[i][0] + mu_matrix[i][1] - 1) * (mu_matrix[i+1][0] + mu_matrix[i+1][1] - 1)
        if(L_mu <= 0):
            if(mu_matrix[i][0] == mu_matrix[i+1][0]):
                x = mu_matrix[i][0]
                y = round(-x+1,5)
                B_matrix.append((x, y))
            elif(mu_matrix[i][1] == mu_matrix[i+1][1]):
                y = mu_matrix[i][1]
                x = round(-y+1,5)
                B_matrix.append((x, y))

    last_el_index = len(mu_matrix)-1
    L_mu = (mu_matrix[last_el_index][0] + mu_matrix[last_el_index][1] - 1) * (mu_matrix[0][0] + mu_matrix[0][1] - 1)
    if (L_mu <= 0):
        if (mu_matrix[last_el_index][0] == mu_matrix[0][0]):
            x = mu_matrix[last_el_index][0]
            y = round(-x + 1, 5)
            B_matrix.append((x, y))
        elif (mu_matrix[last_el_index][1] == mu_matrix[0][1]):
            y = mu_matrix[last_el_index][1]
            x = round(-y + 1, 5)
            B_matrix.append((x, y))

    B_matrix = list(dict.fromkeys(B_matrix))
    return(B_matrix)

def get_Omega_matrix(B_matrix):
    Omega_matrix = []
    y1=1
    x1 = -((B_matrix[0][1] * y1)/B_matrix[0][0])
    Omega_matrix.append((x1,y1))

    x2 = 1
    y2 = -((B_matrix[1][0] * x2)/B_matrix[1][1])
    Omega_matrix.append((x2,y2))
    return Omega_matrix




