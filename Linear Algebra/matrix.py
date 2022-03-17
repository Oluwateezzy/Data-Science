def shape(A):
    nums_rows = len(A)
    nums_cols = len(A[0]) if A else 0
    return nums_rows, nums_cols

def get_row(A, i):
    return A[i]

def get_column(A, i):
    return [A_i[i] for A_i in A]

def make_matrix(num_rows, num_cols, entry_fn):
    return [[entry_fn(i, j) for j in range(num_cols)]
                            for i in range(num_rows)]

def make_new_matrix(rows, cols):
    return 0

created_matrix = make_matrix(10, 10, make_new_matrix)
friendships = [(0, 1), (0, 2), (1, 2), (1,3), (2, 3), (3, 4),
                (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)
]

for i, j in friendships:
    created_matrix[i][j] = 1

def check_if_connected(row, col):
    return "connected" if created_matrix[row][col] == 1 else "not connected"

fof = [i for i, is_friend in enumerate(created_matrix[0]) if is_friend]

print(created_matrix)
print(fof)

def is_diagonal(i, j):
    return 0 if i == j else 1