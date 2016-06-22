import unittest
import graph_db
from unittest.mock import MagicMock, patch

class OrientDBTestCase(unittest.TestCase):
    """Orient Test Case"""

    def setUp(self):
        dbsettings = {
            'host': 'localhost',
            'user': 'root',
            'password': 'veca3150',
            'name': 'diggi-v1',
            'port': '2480'
        }
        self.driver = graph_db.Factory('orientdb', dbsettings)
    
    def test_it_should_connect(self):
        pass

# dbsettings = {
#     'host': 'localhost',
#     'user': 'test',
#     'password': 'test',
#     'name': 'test',
#     'port': 27019,
#     'debug': True
# }

# driver = graph_db.Factory('mongodb', dbsettings)

# a = driver.Vertex.find({
# 	'uuid' : 'c65d57d6-4d0a-4ed4-8e37-0386a45f9389'
# })[0]

# b = driver.Vertex.find({
# 	'uuid' : 'fe0100f8-c504-4566-86e8-bc88887c6029'
# })[0]

# amigo = driver.Edge.create(a, b, {'bar': 'baz'})

# print (amigo)

# driver.disconnect()

'''
import unittest

class OrientDBTestCase(unittest.TestCase):
    """Orient Test Case"""

    def setUp(self):
        dbsettings = {
            'host': 'localhost',
            'user': 'root',
            'password': 'veca3150',
            'name': 'diggi-v1',
            'port': '2480'
        }
        self.driver = driver = graph_db.Factory('orientdb', dbsettings)
        
    def test_it_should_connect(self):
        """It should connect with no problems"""
        
        driver = graph_db.Factory('orientdb', dbsettings)
        driver.DB.connect()
        assert driver.DB._connected == True
        driver.DB.disconnect()

    def test_it_should_not_connect(self):
        """It should not connect, and raise an exeption"""
        dbsettings = {
            'host': 'lo1calhost',
            'user': 'root',
            'password': 'veca3150',
            'name': 'diggi-v1',
            'port': 2480
        }
        driver = graph_db.Factory('orientdb', dbsettings)
        self.assertRaises(graph_db.types.GraphDBException, driver.DB.connect)
        assert driver.DB._connected == False
        driver.DB.disconnect()

    def test_it_should_recycle_connection(self):
        """It should recycle the connection if the host, driver and port are the same."""
        dbsettings = {
            'host': 'localhost',
            'user': 'root',
            'password': 'veca3150',
            'name': 'diggi-v1',
            'port': 2480
        }
        driver1 = graph_db.Factory('orientdb', dbsettings)
        driver1.DB.connect()
        driver2 = graph_db.Factory('orientdb', dbsettings)
        driver2.DB.connect()
        assert driver1 == driver2
        assert driver1.DB == driver2.DB
        driver1.DB.disconnect()
        driver2.DB.disconnect()
    def test_it_should_connect(self):
        """It should throw an error on bad query"""
        dbsettings = {
            'host': 'localhost',
            'user': 'root',
            'password': 'veca3150',
            'name': 'diggi-v1',
            'port': 2480
        }
        driver = graph_db.Factory('orientdb', dbsettings)
        driver.DB.connect()
        assert driver.DB._connected == True
        self.assertRaises(graph_db.types.GraphDBException, driver.Vertex.find, 'val')
        driver.DB.disconnect()


if __name__ == '__main__':
    unittest.main()

#

amy = driver.Vertex.create('V')

victor = driver.Vertex.create('V')

amigo = driver.Edge.create('L', amy, victor)

print (amy, victor, amigo)

driver.DB.disconnect()
'''