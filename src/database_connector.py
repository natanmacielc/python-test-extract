import sqlalchemy as sql
import pandas as pd


class DatabaseConnector:
    def __init__(self, db_type: str, db_user: str, db_password: str, db_host: str, db_port: str, db_name: str):
        self.engine = sql.create_engine(f'{db_type}://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

    def execute_query(self, query) -> pd.DataFrame:
        return pd.read_sql(query, con=self.engine)
