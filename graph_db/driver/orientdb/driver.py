from ... import types
from . import exceptions
import requests

class OrientDBDriver(types.BaseDriver):
    client = None
    _connected = False
    def __init__(self, autoConnect = True, settings={}):
        self._settings = settings
        user = self._settings['user']
        password = self._settings['password']
        self._auth = requests.auth.HTTPBasicAuth(user, password)
        self._settings['url'] = 'http://%s:%d' % (self._settings['host'], self._settings['port'])

        if autoConnect:
            self.connect()

    def connect(self):
        if self._connected:
            return
        url = '%(base_url)s/connect/%(db_name)s/sql/-' % ({
            'base_url': self._settings['url'],
            'db_name': self._settings['name']
        })
        try:
            response = requests.get(url, auth=self._auth)
            if response.status_code == 401:
                raise exceptions.OrientDBConnectionError("Invalid Credentials")

            url = '%(base_url)s/database/%(db_name)s/sql/-' % ({
                'base_url': self._settings['url'],
                'db_name': self._settings['name']
            })
            response = requests.get(url, auth=self._auth)
            if response.status_code == 401:
                raise exceptions.OrientDBConnectionError("Invalid Database 401 Connection")
            self._connected = True
        except requests.exceptions.RequestException as e:
            raise exceptions.OrientDBConnectionError("Invalid Database Connection (OrientDB may be down)")

    def query(self, sql, *args, **kwargs):
        if not self._connected:
            self.connect()
        depth = kwargs.get('depth', 0)
        url = '%(base_url)s/command/%(db_name)s/sql/-' % ({
            'base_url': self._settings['url'],
            'db_name': self._settings['name']
        })
        
        try:
            response = requests.post( url,
                auth = self._auth, 
                params = {
                    'format': 'rid,class,fetchPlan:*:%d' % depth
                },
                data = sql)
            return response.json().get('result')
        except requests.exceptions.RequestException as e:
            self._connected = False
            raise exceptions.OrientDBConnectionError("invalid connection (maybe down)")
        except ValueError as e:
            raise exceptions.OrientDBQueryError(response.text)
            
    def disconnect(self):
        try:
            response = requests.get(self._settings['url'] + '/disconnect', auth=self._auth)
        except requests.exceptions.RequestException as e:
            raise exceptions.OrientDBConnectionError("Couldn't Disconnect to OrientDB Server")
