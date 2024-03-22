

def inverse_matrix(matrix):
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if determinant == 0:
        raise ValueError("Matrix is not invertible")

    inverse = [[0, 0], [0, 0]]
    inverse[0][0] = matrix[1][1] / determinant
    inverse[0][1] = -matrix[0][1] / determinant
    inverse[1][0] = -matrix[1][0] / determinant
    inverse[1][1] = matrix[0][0] / determinant

    return inverse

# Example matrix
matrix = [
    [4, 7],
    [2, 6]
]

inverse = inverse_matrix(matrix)

print("Inverse matrix:")
for row in inverse:
    print(row)