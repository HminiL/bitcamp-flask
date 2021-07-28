import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from modu.template import ChangeTemperatureOnMyBirthday


class Population():

    data: [] = list()

    def read_data(self):
        data = csv.reader(open('data/202106_202106_연령별인구현황_월간.csv', encoding='utf-8'))
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

    def find_similar_dong(self):
        data = self.data
        name = input('인구 구조가 알고 은싶 지역의 이름(읍면동 단위)을 입력해주세요 : ')
        # home = (np.array(i[3:], dtype=int) for i in data if name in i[0])
        for i in data:
            if name in i[0]:
                home = np.array(i[3:], dtype=int) / int(i[2])

        plt.rc('font', family='C:/Windows/Fonts/H2GTRE.ttf')
        plt.title(name+'지역의 인구구조')
        plt.plot(home)
        plt.show()

        print(home)


if __name__ == '__main__':
    pop = Population()
    pop.read_data()
    # pop.show_flot(pop.pop_per_dong('역삼2동'))
    # pop.find_similar_dong()
