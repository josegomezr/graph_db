from ... import types

class Result(types.Result):
    def edgeIn(self, label='E'):
        if self._type != 'vertex':
            raise Exception('no edge from edge')
        if label == 'E':
            label = ''
        edge = self['in_'+label]
        return self.__edge(edge)

    def edgeOut(self, label='E'):
        if self._type != 'vertex':
            raise Exception('no edge from edge')
        if label == 'E':
            label = ''
        edge = self['out_'+label]
        return self.__edge(edge)

class ResultSet(types.ResultSet):
    pass
