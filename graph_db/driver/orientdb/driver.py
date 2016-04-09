from ... import types
from . import exceptions
import requests

class DBDriver(types.BaseDBDriver):
    def __init__(self, autoConnect = True, settings={}):
        self._connected = False
        self._dbSelected = False
        self._settings = settings
        self.debug = self._settings.get('debug', False)
        user = self._settings['user']
        password = self._settings['password']
        self._auth = requests.auth.HTTPBasicAuth(user, password)

        self._settings['url'] = 'http://%s:%s' % (self._settings['host'], str(self._settings['port']))

        if autoConnect:
            self.connect()
            self.selectDB()

    def __url(self, *args):
        segments = [self._settings['url']]
        segments.extend( args )
        return '/'.join( segments )

    def connect(self):
        if self._connected:
            return

        try:
            url = self.__url('connect', self._settings['name'])
            self._debugOut("GET %s" % url)
            response = requests.get(url, auth=self._auth)
            self._debugIn("[%s]" % response.status_code, response.text)
            if response.status_code == 401:
                raise exceptions.OrientDBConnectionError("Invalid Credentials")
        except requests.exceptions.RequestException as e:
            raise exceptions.OrientDBConnectionError("Invalid Database Connection (connect) (OrientDB may be down)")
        
        self._connected = True
        return self

    def selectDB(self):
        if not self._connected:
            self.connect()
        try:
            url = self.__url('database', self._settings['name'])
            self._debugOut("GET %s" % url)
            response = requests.get(url, auth=self._auth)
            self._debugIn("[%s]" % response.status_code, response.text)
            if response.status_code == 401:
                raise exceptions.OrientDBConnectionError("Invalid Database 401 Connection")
            self._dbSelected = True
        except requests.exceptions.RequestException as e:
            raise exceptions.OrientDBConnectionError("Invalid Database Connection (select-db) (OrientDB may be down)")

        return self

    def query(self, sql, *args, **kwargs):
        if not self._connected:
            self.connect()

        if not self._dbSelected:
            self.selectDB()

        depth = kwargs.get('depth', 0)

        url = self.__url('command', self._settings['name'], 'sql')

        self._debugOut("GET %s" % url)
        self._debugOut("POST %s\n--> %s" % (url, sql))

        try:
            response = requests.post( url,
                auth   = self._auth, 
                params = {
                    'format': 'rid,class,fetchPlan:*:%d' % depth
                },
                data = sql)
            self._debugIn(response.text)
            return response.json().get('result')
        except requests.exceptions.RequestException as e:
            self._connected = False
            raise exceptions.OrientDBConnectionError("invalid connection (maybe down)")
        except ValueError as e:
            raise exceptions.OrientDBQueryError(response.text)

    def disconnect(self):
        if not self._connected:
            return
        try:
            url = self._settings['url'] + '/disconnect'
            self._debugOut("GET %s" % url)
            response = requests.get(url, auth=self._auth)
        except requests.exceptions.RequestException as e:
            raise exceptions.OrientDBConnectionError("Couldn't Disconnect to OrientDB Server")
        self._connected = False
