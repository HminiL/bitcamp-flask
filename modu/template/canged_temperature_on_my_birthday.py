import csv

class ChangeTemperatureOnMyBirthday():
    pass

    def processing(self):
        self.read_data()
        self.save_data_to_list()
        self.visualize_data()
        self.extract_date_data()

    def read_data(self):
        data = csv.reader(open('./data/seoul.csv'))
        print([i for i in data])

    def save_data_to_list(self):
        pass

    def visualize_data(self):
        pass

    def extract_date_data(self):
        pass


if __name__ == '__main__':
    this = ChangeTemperatureOnMyBirthday()
    this.read_data()

