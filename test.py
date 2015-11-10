import graph_db

dbsettings = {
    'host': 'localhost',
    'user': 'root',
    'password': 'veca3150',
    'name': 'diggi-v1',
    'port': 2480
}

driver = graph_db.Factory('orientdb', dbsettings)

amy = driver.Vertex.create('V')
victor = driver.Vertex.create('V')

amigo = driver.Edge.create('L', amy[0]['@rid'], victor[0]['@rid'])

print (amy, victor, amigo)

driver.Driver.disconnect()
