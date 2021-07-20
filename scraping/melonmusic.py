from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import Request


class Melonmusic(object):

    def __init__(self, url):
        self.url = url


    def scrap(self):
        soup = BeautifulSoup(urlopen(Request(self.url, headers = {"User-Agent": "Mozilla/5.0"})), "lxml")
        artists = 0
        ls = soup.find_all(name='div', attrs={'class': 'ellipsis rank02'})
        ls2 = soup.find_all('div', {'class': 'ellipsis rank01'})
        for i,j in enumerate(ls):
            artists += 1
            print(str(artists) + "Rank" + j.find('a').text  + ls2[i].find('a').text)


def main():
    Melonmusic(f'https://www.melon.com/chart/index.htm?dayTime={"2021072016"}').scrap()


if __name__ == '__main__':
    main()