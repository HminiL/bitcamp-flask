import matplotlib.pyplot as plt

from modu.template.basic_hist import highest_temperature


def show_box_highest_temperature(month: str):
    plt.boxplot(highest_temperature(month))
    plt.show()


if __name__ == '__main__':
    show_box_highest_temperature('01')