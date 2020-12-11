from ..parser import ReunionParser

class ReunionTrends():

    def __init__(self):
        self.parser = ReunionParser()
        self.parser.parse()

    def get_popularities(self):
        return self.dict

    def save_to_db(self):
        pass