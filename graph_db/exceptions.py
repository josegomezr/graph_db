class GraphDBError(Exception):
    """
    Base Exception
    """
    pass

class GraphDBConectionError(GraphDBError):
    """
    Describes Connection errors.
    """
    pass

class GraphDBAuthError(GraphDBError):
    """
    Describes Authentication errors.
    """
    pass

class GraphDBQueryError(GraphDBError):
    """
    Describes Query Errors
    """
    pass