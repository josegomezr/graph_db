class BaseDriver():
    _connected = False
    _settings = {}
    def __init__(self, autoConnect = True, settings={}):
        self._settings.update(settings)
        if autoConnect:
            self.connect()
    def connect(self):
        raise NotImplementedError('Not Implemented Yet')
    def query(self, sql):
        raise NotImplementedError('Not Implemented Yet')
    def disconnect(self):
        raise NotImplementedError('Not Implemented Yet')

class DummyDriver(BaseDriver):
    def connect(self):
        pass
    def query(self, sql):
        pass
    def disconnect(self):
        pass

class Map(dict):
    """
    Example:
    m = Map({'first_name': 'Eduardo'}, last_name='Pool', age=24, sports=['Soccer'])
    """
    def __init__(self, *args, **kwargs):
        super(Map, self).__init__(*args, **kwargs)
        for arg in args:
            if not(isinstance(arg, dict)):
                continue
            for k, v in arg.items():
                self[k] = v
        if not(kwargs):
            return
        for k, v in kwargs.items():
            self[k] = v

    def __getattr__(self, attr):
        return self.get(attr)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        super(Map, self).__setitem__(key, value)
        self.__dict__.update({key: value})

    def __delattr__(self, item):
        self.__delitem__(item)

    def __delitem__(self, key):
        super(Map, self).__delitem__(key)
        del self.__dict__[key]