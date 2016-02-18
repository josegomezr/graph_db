from ... import types

class Result(types.Result):
    def __init__(self, result):
        super(self.__class__, self).__init__(result)

class ResultSet(types.ResultSet):
    def __init__(self, resultset):
        super(ResultSet, self).__init__(resultset)
