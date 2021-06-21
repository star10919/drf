import json
import pandas as pd
from rest_framework.common.abstracts import PrinterBase, ReaderBase, ScraperBase
import googlemaps
from selenium import webdriver

class Printer(PrinterBase):

    def dframe(self, this):
        print('*' * 100)
        print(f'1. 대상의 type\n{type(this)} 이다.')
        print(f'2. 대상의 column\n{this.columns} 이다.')
        print(f'3. 대상의 상위 5개 행\n{this.head()} 이다.')
        print(f'4. 대상의 null 의 갯수\n {this.isnull().sum()}개')
        print('*' * 100)

class Reader(ReaderBase):
    def new_file(self, file) -> str:
        return file._context + file._fname

    def csv(self, file) -> object:
        return pd.read_csv(f'{self.new_file(file)}.csv', thousands=',')

    def xls(self, file, header, usecols) -> object:
        return pd.read_excel(f'{self.new_file(file)}.xls', header=header, usecols=usecols)

    def json(self, file) -> object:
        return json.load(open(f'{self.new_file(file)}.json', encoding='UTF-8'))

    def gmaps(self) -> object:
        return googlemaps.Client(key='AIzaSyApAeFdseWeUvcd-4fmRnhb2cpovrE0SJg')

    # AIzaSyApAeFdseWeUvcd-4fmRnhb2cpovrE0SJg

class Scraper(ScraperBase):
    def driver(self) -> object:
        return webdriver.Chrome('C:/Program Files/Google/Chrome/chromedriver')