from sqlalchemy import text

from plenario.database import redshift_engine


def create_network_table(network_name):
    op = text('CREATE TABLE {} ('
              '"nodeId" VARCHAR NOT NULL, '
              'datetime TIMESTAMP WITHOUT TIME ZONE NOT NULL, '
              '"feature" VARCHAR NOT NULL, '
              '"sensor" VARCHAR NOT NULL, '
              '"property1" DOUBLE PRECISION NOT NULL, '
              '"property2" DOUBLE PRECISION, '
              '"property3" DOUBLE PRECISION, '
              'PRIMARY KEY ("nodeId", datetime)) '
              'DISTKEY(datetime) SORTKEY(datetime);'.format(network_name))
    redshift_engine.execute(op)


def add_column(network_name, column_name, column_type):
    op = text('ALTER TABLE {} '
              'ADD COLUMN {} {} '
              'DEFAULT NULL'.format(network_name, column_name, column_type))
    redshift_engine.execute(op)


def insert_observation(network_name, nodeid, datetime, feature, sensor,
                       property1, property2='default', property3='default'):
    op = text('INSERT INTO {} '
              'VALUES ({}, {}, {}, {}, {}, {}, {});'
              .format(network_name, repr(nodeid), repr(datetime), repr(feature), repr(sensor),
                      property1, property2, property3))
    redshift_engine.execute(op)

