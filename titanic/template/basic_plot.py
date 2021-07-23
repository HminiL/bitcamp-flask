import matplotlib.pyplot as plt

from commom.menu import print_menu

"""
list 값은 y축 이고, x축은 0부터 1까지 자동으로 증가한다. 
"""
def plot_show():
    plt.title("plotting")
    plt.plot([10, 20, 30, 40], color='yellow')
    plt.show()

"""
첫 번째 리스트가 x축, 두 번째 리스트가 y축
"""
def plot_two_list_show():
    plt.plot([1, 2, 3, 4], [12, 46, 25, 15],linestyle = '--')
    plt.show()


def plot_legend():
    plt.title("legend")
    plt.plot([10, 20, 30, 40], color='skyblue', label='asc', linestyle=':')
    plt.plot([40, 30, 20, 10], label='desc', color='pink')
    plt.legend()
    plt.show()


def plot_color():
    plt.title("color")
    plt.plot([10, 20, 30, 40], color = 'red', label='red')
    plt.plot([40, 30, 20, 10], 'pink', label='pink')
    plt.legend()
    plt.show()


def plot_marker():
    plt.title("marker")     #제목설정
    plt.plot([10, 20, 30, 40], 'r.', label='circle')        # 빨간색 원형 마커 그래프
    plt.plot([40, 30, 20, 10], 'g^', label='triangle up')   # 초록색 삼각형 마커 그래프
    plt.legend()        # 범례표시
    plt.show()


if __name__ == '__main__':
    while 1:
        menu = print_menu(['exit','plot_show', 'plot_two_list_show', 'plot_legend', 'plot_color', 'plot_marker'])
        if menu == 0:
            break
        elif menu == 1:
            plot_show()
        elif menu == 2:
            plot_two_list_show()
        elif menu == 3:
            plot_legend()
        elif menu == 4:
            plot_color()
        elif menu == 5:
            plot_marker()
