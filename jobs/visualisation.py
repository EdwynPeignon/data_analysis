import matplotlib.pyplot as plt
from jobs import static


# Generate pie and save fig
def generate_pie(data, label, title, explode=None, show=False):
    plt.clf()
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.title(title)
    ax.pie(data, labeldistance=5, autopct='%.0f%%', startangle=90, explode=explode)
    ax.axis('equal')
    plt.legend(label, loc=1)
    plt.savefig('{}{}.png'.format(static.PATH_OUTPUTS, title.replace(' ', '_')))
    if show:
        plt.show()


def generate_multiple_pies(list_data, list_label, size_matrix, column_name, explode=None):
    fig, axs = plt.subplots(size_matrix[0], size_matrix[1])
    if len(list_data) != len(list_label):
        print("Labels and data don't have the same number.")
        exit()
    elif len(list_data) > (size_matrix[0] * size_matrix[1]):
        print("Number of data higher than your matrix.")
        exit()
    print(list_label)
    x, y = 0, 0
    print(list_label, len(list_data))
    zip_for = zip(list_data, list_label) if explode is None else zip(list_data, list_label, explode)
    for increment in zip_for:
        print(x, y)
        if len(increment) == 2:
            axs[x, y].pie(increment[0], labels=increment[1], autopct='%1.1f%%', shadow=True)
        else:
            axs[x, y].pie(increment[0], labels=increment[1], autopct='%.0f%%', shadow=True, explode=increment[2])
        print(y % 2)
        if y % (size_matrix[1] - 1) == 0 and y != 0:
            x += 1
            y = 0
        else:
            y += 1
    plt.savefig('{}percentage_connected_all_{}.png'.format(static.PATH_OUTPUTS, column_name))


def plot_bargraph_with_groupings(df, groupby, title, xlabel, ylabel, show=False):
    plt.clf()
    fig, ax = plt.subplots(figsize=(20, 15))
    ax = df[groupby].value_counts().plot(kind='bar', title=title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.savefig('{}{}.png'.format(static.PATH_OUTPUTS, title.replace(' ', '_')))
    if show:
        plt.show()
