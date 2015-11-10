import graph_db

dbsettings = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456',
    'name': 'testdb',
    'port': 2480
}

driver = graph_db.Factory('orientdb', dbsettings)

amy = driver.Vertex.create('V')
victor = driver.Vertex.create('V')

amigo = driver.Edge.create('L', amy[0]['@rid'], victor[0]['@rid'])

print (amy, victor, amigo)

driver.Driver.disconnect()
