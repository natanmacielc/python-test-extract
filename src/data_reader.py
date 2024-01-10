from database_connector import DatabaseConnector
from pandas import DataFrame


class DataReader:
    def __init__(self, db_connector: DatabaseConnector):
        self.db_connector = db_connector

    def read_from_table(self, table: str) -> DataFrame:
        return self.db_connector.execute_query("select * from " + table)
