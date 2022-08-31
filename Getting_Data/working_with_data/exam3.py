from matplotlib import pyplot as plt

def shape(A):
    nums_rows = len(A)
    nums_cols = len(A[0]) if A else 0
    return nums_rows, nums_cols

def get_columns(data, j):
    return [a_i[j] for a_i in data]

data = [
    [2, 3, 5, 5],
    [4, 8, 7, 5],
    [7, 9, 4, 2],
    [1, 6, 7, 3]
]

_, num_columns = shape(data)

fig, ax = plt.subplots(num_columns, num_columns)

for i in range(num_columns):
    for j in range(num_columns):

        if i != j:
            ax[i][j].scatter(get_columns(data, i), get_columns(data, j))

        else:
            ax[i][j].annotate("series " + str(i), (0.5, 0.5), xycoords="axes fraction", ha="center", va="center")
        
        if i < num_columns - 1:
            ax[i][j].xaxis.set_visible(False)
        if j > 0:
            ax[i][j].yaxis.set_visible(False)

ax[-1][-1].set_xlim(ax[0][-1].get_xlim())
ax[0][0].set_xlim(ax[0][1].get_ylim())

plt.show()