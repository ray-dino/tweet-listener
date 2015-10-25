import os
from cassandra.cqlengine.management import sync_table
from cassandra.cqlengine.connection import set_session
from models import Tweet
from cassandra.cluster import Cluster
from cassandra.query import dict_factory


CASSANDRA_ADDRESS = [os.environ.get('CASSANDRA_ADDRESS', '127.0.0.1')]
CASSANDRA_KEYSPACE = os.environ.get('CASSANDRA_KEYSPACE')

if __name__ == '__main__':
    if raw_input('Are you sure you want to sync the database? [Y/N]')=='Y':
        cluster = Cluster(CASSANDRA_ADDRESS)
        session = cluster.connect(CASSANDRA_KEYSPACE)
        session.row_factory = dict_factory
        set_session(session)
        sync_table(Tweet)
