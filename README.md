# GraphDB

Almacenamiento para grafos.

Esto es un esfuerzo por crear una interfaz común para almacenar grafos dirigidos sin importar el motor de base de datos utilizado (Grafo, Documento, Clave-Valor).

El proyecto se encuentra en estado ALPHA y puede cambiar bruscamente.

## Ejemplo

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
