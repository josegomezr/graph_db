from ... import exceptions

class OrientDBException(exceptions.GraphDBError):
    pass

class OrientDBConnectionError(OrientDBException, exceptions.GraphDBConectionError):
    pass

class OrientDBQueryError(exceptions.GraphDBQueryError):
    def __init__(self, message, *args):
        exeptionPath = 'com.orientechnologies.orient.core.exception'
        start = message.find(exeptionPath)
        end = message.find('\n', start)

        FirstError = message[start+len(exeptionPath)+1:end]
        FirstExceptionName, FirstExceptionDescription = FirstError.split(': ', 1)

        start = message.find(exeptionPath, end)
        end = message.find('\n', start)
        SecondError = message[start+len(exeptionPath)+1:]
        SecondExceptionName, SecondExceptionDescription = SecondError.split(': ', 1)
        message = "%s: %s //// %s: %s" % (FirstExceptionName, FirstExceptionDescription, SecondExceptionName, SecondExceptionDescription)
        super(OrientDBQueryError, self).__init__(message, *args)