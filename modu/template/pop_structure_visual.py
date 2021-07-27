import csv

import matplotlib.pyplot as plt
from modu.template import ChangeTemperatureOnMyBirthday


class Population():

    data: [] = list()

    def read_data(self):
        data = csv.reader(open('data/202106_202106_연령별인구현황_월간.csv', 'rt', encoding='UTF-8'))
        next(data)
        self.data = data
        # print([i for i in data])

    def pop_per_dong(self, dong: str) ->[] :
        # [주의] csv reader 는 1회 이상 사용하면 GC(가비지컬렉터)가 제거한다.
        arr = []
        [arr.append(int(i)) for j in self.data if dong in j[0] for i in j[3:]]
        print(arr)
        return arr

    def show_flot(self, arr: []):
        plt.style.use('ggplot')
        plt.plot(arr)
        plt.show()


if __name__ == '__main__':
    pop = Population()
    pop.read_data()
    pop.show_flot(pop.pop_per_dong('역삼2동'))
