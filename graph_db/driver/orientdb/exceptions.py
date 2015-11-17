from ... import types

class OrientDBException(types.GraphDBException):
    pass

class OrientDBConnectionError(types.GraphDBException):
    pass

class OrientDBQueryError(types.GraphDBException):
    pass
