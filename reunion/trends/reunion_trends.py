import grpc

from reunion.parser import ReunionParser
from reunion.utils import get_grpc_hostname
from api.protos import database_pb2_grpc
from api.protos.database_pb2 import TrendWithDefaultDate

class ReunionTrends():

    def __init__(self):

        channel = grpc.insecure_channel(f'{get_grpc_hostname()}:6565')
        self.stub = database_pb2_grpc.DatabaseStub(channel)

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

        for key, value in self.dict.items():
            _dict = {
               'symbol': key,
               'popularity': value
            }
            try:
                rowcount = self.stub.insert_reunion_trend(
                    TrendWithDefaultDate(symbol=_dict['symbol'], popularity=_dict['popularity']))
                print(rowcount)
            except grpc.RpcError as e:
                status_code = e.code()
                print(e.details())
                print(status_code.name, status_code.value)
