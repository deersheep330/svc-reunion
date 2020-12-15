from ..db import create_engine, start_session, insert, get_db_hostname
from ..models import ReunionTrend
from ..parser import ReunionParser

class ReunionTrends():

    def __init__(self):
        self.parser = ReunionParser()
        self.parser.parse()

        self.dict = {}
        n = len(self.parser.list) * 10
        for symbol in self.parser.list:
            self.dict[symbol] = n
            n -= 10

    def get_popularities(self):
        return self.dict

    def save_to_db(self):
        engine = create_engine('mysql+pymysql', 'root', 'admin', get_db_hostname(), '3306', 'mydb')
        session = start_session(engine)

        for key, value in self.dict.items():
            _dict = {
               'symbol': key,
               'popularity': value
            }
            try:
                insert(session, ReunionTrend, _dict)
            except Exception as e:
                print(f'insert entry error: {e}')
        session.commit()
        session.close()