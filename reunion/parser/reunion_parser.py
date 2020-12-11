import requests
from lxml import etree

class ReunionParser():

    def __init__(self):
        self.url = 'https://www.cmoney.tw/follow/channel/hot-stock'
        self.dict = {}

    def parse(self):
        pass

    def get_popularities(self):
        return self.dict

