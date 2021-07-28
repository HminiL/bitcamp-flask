import pandas as pd
import matplotlib.pyplot as plt



def read_data():
    data = pd.read_csv('data/202106_202106_연령별인구현황_월간.csv', encoding='utf-8', index_col=0, thousands=',')
    pd.DataFrame.to_csv('data/202106_202106_연령별인구현황_월간_without.csv', sep=',', na_rep='Nan')
    print(data)

if __name__ == '__main__':
    read_data()