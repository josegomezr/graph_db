from ... import types

def _getConst(obj):
    if obj.get('in') and obj.get('out'):
        return EdgeResult
    else:
        return VertexResult

def Result(rset):
    if isinstance(rset, dict):
        const = _getConst(rset)
        return const(rset)
    elif isinstance(rset, list):
        const = _getConst(rset[0])
        return ResultSet(rset, const)

class VertexResult(types.Map):
    def __init__(self, result):
        super(self.__class__, self).__init__(result)

class EdgeResult(types.Map):
    def __init__(self, result):
        super(self.__class__, self).__init__(result)


class ResultSet(types.List):
    def __init__(self, resultset, const):
        super(ResultSet, self).__init__(resultset)

        for i, target in enumerate(self):
            self[i] = const(target)
            
