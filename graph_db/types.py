        
class BaseDBDriver():
    """
    This will stub the most basic methods that a GraphDB driver must have.
    """
    _connected = False
    _settings = {}
    def __init__(self, dbapi):
        self.dbapi = dbapi
    def _debug(self, *args):
        if self.debug:
            print ("[GraphDB #%x]:" % id(self), *args)

    def _debugOut(self, *args):
        self._debug("OUT --> ", *args)

    def _debugIn(self, *args):
        self._debug("IN  <-- ", *args)

    def connect(self):
        """
        Performs connection to the database service.

        connect() -> self
        """
        raise NotImplementedError('Not Implemented Yet')
    def query(self, sql):
        """
        Performs a query to the database.

        query( sql ) -> dict
        """
        raise NotImplementedError('Not Implemented Yet')
    def disconnect(self):
        """
        Performs disconnection and garbage collection for the driver.
        connect() -> self
        """
        raise NotImplementedError('Not Implemented Yet')

class BaseEdgeDriver(object):
    """
    Base driver for managing Edges.
    
    This will provide CRUD & search operations to be extended by 
    drivers.
    """
    def __init__(self, driver):
        self.driver = driver

    def create(self, eType, origin, destiny, data = {}):
        """
        create(eType, origin, destiny [, data]) -> dict

        Creates an edge from *origin* to *destiny*
        """
        raise NotImplementedError('Not Implemented Yet')
    
    def update(self, eType, criteria = {}, data = {}):
        """
        update(eType [, criteria [, data]]) -> dict

        Update edges mathing a given criteria
        """
        raise NotImplementedError('Not Implemented Yet')
    
    def delete(self, eType, criteria = {}):
        """
        delete(eType [, criteria]) -> dict

        Delete edges mathing a given criteria
        """
        raise NotImplementedError('Not Implemented Yet')

    def find(self, eType, criteria = {}):
        """
        find(eType [, criteria]) -> list

        Find an edge for a given criteria.
        """
        raise NotImplementedError('Not Implemented Yet')

class BaseVertexDriver(object):
    """
    Base driver for managing Vertexes.
    
    This will provide CRUD & search operations to be extended by 
    drivers.
    """
    def __init__(self, driver):
        self.driver = driver

    def create(self, vType, data = {}):
        """
        create(vType, [, data]) -> dict

        Create a Vertex
        """
        raise NotImplementedError('Not Implemented Yet')
    
    def update(self, vType, criteria = {}, data = {}):
        """
        update(vType, criteria, data) -> dict

        Update a Vertex given a criteria
        """
        raise NotImplementedError('Not Implemented Yet')
    
    def delete(self, vType, criteria = {}):
        """
        delete(vType, criteria) -> dict

        Delete a Vertex given a criteria
        """

        raise NotImplementedError('Not Implemented Yet')

    def find(self, vType, criteria = None):
        """
        find(vType [, criteria]) -> list

        Look for vertexes matching criteria.
        """

        raise NotImplementedError('Not Implemented Yet')
