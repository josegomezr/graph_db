from __future__ import print_function
from setuptools import setup, find_packages
import os
import graph_db

here = os.path.abspath(os.path.dirname(__file__))

long_description = '''GraphDB almacenamiento para grafos en cualquier gestor de base de datos.'''

setup(
    name='graph_db',
    version=graph_db.__version__,
    url='http://github.com/josegomezr/graph_db',
    license='Apache Software License',
    author='José Daniel Gómez Rodríguez',
    install_requires=[
        'requests == 2.7.0',
        'pqb >= 0.0.1',
    ],
    author_email='1josegomezr@gmail.com',
    description='GraphDB almacenamiento para grafos en cualquier gestor de base de datos.',
    long_description=long_description,
    packages=['graph_db'],
    include_package_data=True,
    platforms='any',
    keywords='graph database grafos',

    # test_suite='graph_db.test.all',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'Natural Language :: Spanish',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ]
)
