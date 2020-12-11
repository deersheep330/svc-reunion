

class ReunionParser():

    def __init__(self):
        self.url = 'https://www.cmoney.tw/follow/channel/hot-stock'
        self.list = []

    def parse(self):
        '''
        print(f'==> parse page: {self.url}')
        resp = requests.get(self.url)
        content = resp.text
        tree = etree.HTML(content)
        print(content)

        entries = tree.xpath("//*[contains(@id, 'ItemList')]//*[contains(@id, 'Item_')]//*[contains(@class, 'text')]//*[contains(@href, '/follow/channel/stock-')]")
        print(entries)
        '''
