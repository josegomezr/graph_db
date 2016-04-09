from ... import exceptions

class MongoDBException(exceptions.GraphDBError):
    pass

class MongoDBConnectionError(MongoDBException, exceptions.GraphDBConectionError):
    pass

class MongoDBQueryError(exceptions.GraphDBQueryError):
    pass