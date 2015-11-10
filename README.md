# GraphDB

Almacenamiento para grafos.

Esto es un esfuerzo por crear una interfaz común para almacenar grafos dirigidos sin importar el motor de base de datos utilizado (Grafo, Documento, Clave-Valor).

El proyecto se encuentra en estado ALPHA y puede cambiar bruscamente.

## Caso de estudio
Consideremos el grafo siguiente:

![(Amy)-[Amigo]->(Victor)](https://raw.github.com/josegomezr/graphdb/master/img/grafo-prueba.png)

Que puede ser representado de la siguiente manera:

|    Vertex:    |      Amy      |
|--------------:|:--------------|
|**id:**        |`1`            |
|**dataset:**   |`{}`           |
|**out_C:**     |`[2]`          |
|**type:**      |`V`            |

|     Edge:     |     Amigo     |
|--------------:|:--------------|
|**id:**        |`3`            |
|**dataset:**   |`{}`           |
|**out_C:**     |`[2]`          |
|**type:**      |`L`            |

|    Vertex:    |     Victor    |
|--------------:|:--------------|
|**id:**        |`2`            |
|**dataset:**   |`{}`           |
|**in_C:**      |`[2]`          |
|**type:**      |`V`            |

Almacenarlo en una base de datos tipo Grafo (como OrientDB por ejemplo) es muy fácil.

```sql
# Esquema / Estructura
# la clase V existe por defecto en OrientDB
CREATE CLASS L EXTENDS E
# Datos 
CREATE VERTEX V # asumiendo que @rid resulta #9:0
CREATE VERTEX V # asumiendo que @rid resulta #9:1
CREATE EDGE L FROM #9:0 TO #9:1 #11:0
# consulta
SELECT * FROM #11:0 # con fetchPlan = *:1
```
```js
// resultado
[
  {
    "in": {
      "in_": [],
      "in_L": [
        "#11:0"
      ],
      "@fieldTypes": "in_=g,in_L=g",
      "@rid": "#9:1",
      "@version": 4,
      "@type": "d",
      "@class": "V"
    },
    "out": {
      "@rid": "#9:0",
      "out_L": [
        "#11:0"
      ],
      "@fieldTypes": "out_=g,out_L=g",
      "out_": [],
      "@version": 4,
      "@type": "d",
      "@class": "V"
    },
    "@version": 3,
    "@rid": "#11:0",
    "@class": "L",
    "@type": "d"
  }
]
```

Sin embargo, es muy poco probable conseguir comercialmente servidores con OrientDB instalado (como los servicios de Shared Hosting por ejemplo), que tal si cambiamos de motor a digamos MySQL.

```sql
# Esquema/Estructura
CREATE TABLE vertex_type(
	id_vertex_type INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256),
    parent INT NULL,
    PRIMARY KEY (id_vertex_type),
    FOREIGN KEY (parent) REFERENCES vertex_type(id_vertex_type)
);

CREATE TABLE edge_type(
	id_edge_type INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    parent INT NULL,
    PRIMARY KEY (id_edge_type),
    FOREIGN KEY (parent) REFERENCES edge_type(id_edge_type)
);

CREATE TABLE vertex(
	id_vertex INT NOT NULL AUTO_INCREMENT,
    dataset TEXT,
    type INT NOT NULL,
    PRIMARY KEY (id_vertex),
    FOREIGN KEY (type) REFERENCES vertex_type(id_vertex_type)
);

CREATE TABLE edge(
	id_edge INT NOT NULL AUTO_INCREMENT,
    dataset TEXT,
    type INT NOT NULL,
    origin INT NOT NULL,
    destiny INT NOT NULL,
    PRIMARY KEY (id_edge),
    FOREIGN KEY (type) REFERENCES edge_type(id_edge_type),
    FOREIGN KEY (origin) REFERENCES vertex(id_vertex),
    FOREIGN KEY (destiny) REFERENCES vertex(id_vertex)
);

# Datos
INSERT INTO vertex_type (id_vertex_type, name) VALUES (1, 'V');

INSERT INTO edge_type (id_edge_type, name) VALUES (1, 'L');

INSERT INTO vertex (id_vertex, type) VALUES (1, 1), (2, 1);

INSERT INTO edge (type, origin, destiny) VALUES (1, 1, 2);

# Consulta

SELECT edge.id_edge AS edge_id, edge_type.name AS edge_type, edge.origin AS edge_origin, edge.destiny AS edge_destiny, edge.dataset AS edge_dataset, oV.id_vertex AS origin_vertex_id, oV.dataset AS origin_vertex_dataset, oVT.name AS origin_vertex_type, dV.id_vertex AS origin_vertex_id, dV.dataset AS origin_vertex_dataset, dVT.name AS origin_vertex_type
FROM edge
LEFT JOIN edge_type ON ( type = edge_type.id_edge_type ) 
LEFT JOIN vertex AS oV ON ( origin = oV.id_vertex ) 
LEFT JOIN vertex AS dV ON ( destiny = dV.id_vertex ) 
LEFT JOIN vertex_type AS oVT ON ( oV.type = oVT.id_vertex_type ) 
LEFT JOIN vertex_type AS dVT ON ( dV.type = dVT.id_vertex_type ) 
WHERE origin = 1
```

Es notable lo absurdamente complejo que se volvió solo al cambiar el motor, y es solo un caso simple de estudio. El proposito este proyecto es poder almacenar y manejar un grafo dirigido en la mayor cantidad de bases de datos posibles.

## Metas
Hacer funcionar este fragmento de codigo.

```python
import graph_db
db_settings = {
	'host': 'xxx',
    'name': 'yy',
    'user': 'ww',
    'password': 'zz',
    'port': '999'
}
driver = graph_db.Factory('orientdb', db_settings)
amy = driver.Vertex.create()
victor = driver.Vertex.create()
amigo = driver.Edge.create(amy, victor)
```

## Fragmento que funciona
```python
import graph_db

dbsettings = {
    'host': 'localhost',
    'user': 'root',
    'password': 'veca3150',
    'name': 'diggi-v1',
    'port': 2480
}

orientFactory = graph_db.Factory('orientdb', dbsettings)
orientFactory.Driver.connect()

amy = orientFactory.Vertex.create('V')
victor = orientFactory.Vertex.create('V')

amigo = orientFactory.Edge.create('L', amy['result'][0]['@rid'], victor['result'][0]['@rid'])

print amy.get('result'), victor.get('result'), amigo.get('result')

orientFactory.Driver.disconnect()
```