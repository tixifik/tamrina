import numpy as np

def read_matrix_from_file(file_path):
    with open(file_path, 'rt') as file:
        n, m = map(int, file.readline().split())
        data = file.read().split()
        arr = np.array(data, dtype=int)
        return arr.reshape(n, m, m)

def compute_matrix_products(matrix_list):
    product_list = []
    for i in range(len(matrix_list)):
        for j in range(i + 1, len(matrix_list)):
            product = np.dot(matrix_list[i], matrix_list[j])
            product_list.append([product, [matrix_list[i], matrix_list[j]]])
    return product_list

def find_maximum_determinant(matrix_products):
    determinants = [np.linalg.det(x[1][0]) for x in matrix_products]
    max_det = max(determinants)
    max_det_index = determinants.index(max_det)
    return matrix_products[max_det_index][1]

def main():
    matrix = read_matrix_from_file('input1.txt')
    matrix_products = compute_matrix_products(matrix)

    selected_matrix_pair = find_maximum_determinant(matrix_products)
    mat1, mat2 = selected_matrix_pair

    det_mat1 = np.linalg.det(mat1)
    det_mat2 = np.linalg.det(mat2)

    if det_mat1 > det_mat2:
        mat3 = np.dot(mat1, mat2)
    elif det_mat2 > det_mat1:
        mat3 = np.dot(mat2, mat1)
    else:
        index_mat1 = np.where((matrix == mat1).all(axis=(1, 2)))[0][0]
        index_mat2 = np.where((matrix == mat2).all(axis=(1, 2)))[0][0]
        mat3 = np.dot(mat2, mat1) if index_mat1 > index_mat2 else np.dot(mat1, mat2)

    mat4 = np.linalg.inv(mat3)

    np.set_printoptions(precision=3, suppress=True)
    for row in mat4:
        print(" ".join(f"{t:.3f}" for t in row))

if __name__ == "__main__":
    main()




    