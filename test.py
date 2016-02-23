import graph_db
import unittest


class OrientDBTestCase(unittest.TestCase):
    """Orient Test Case"""

    def test_it_should_connect(self):
        """It should connect with no problems"""
        dbsettings = {
            'host': 'localhost',
            'user': 'root',
            'password': 'veca3150',
            'name': 'diggi-v1',
            'port': 2480
        }
        driver = graph_db.Factory('orientdb', dbsettings)
        driver.Driver.connect()
        assert driver.Driver._connected == True
        driver.Driver.disconnect()
    
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
        self.assertRaises(graph_db.types.GraphDBException, driver.Driver.connect)
        assert driver.Driver._connected == False
        driver.Driver.disconnect()

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
        driver1.Driver.connect()
        driver2 = graph_db.Factory('orientdb', dbsettings)
        driver2.Driver.connect()
        assert driver1 == driver2
        assert driver1.Driver == driver2.Driver
        driver1.Driver.disconnect()
        driver2.Driver.disconnect()

if __name__ == '__main__':
    unittest.main()

'''

amy = driver.Vertex.create('V')

victor = driver.Vertex.create('V')

amigo = driver.Edge.create('L', amy, victor)

print (amy, victor, amigo)

driver.Driver.disconnect()
'''