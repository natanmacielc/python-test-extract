import os
from data_reader import DataReader, DatabaseConnector, DataFrame
from excel_creator import ExcelCreator

if __name__ == "__main__":
    def main():
        db_type = os.environ.get('DB_TYPE')
        db_user = os.environ.get('DB_USER')
        db_password = os.environ.get('DB_PASSWORD')
        db_host = os.environ.get('DB_HOST')
        db_port = os.environ.get('DB_PORT')
        db_name = os.environ.get('DB_NAME')

        db_connector: DatabaseConnector = DatabaseConnector(db_type, db_user, db_password, db_host, db_port, db_name)
        data_reader: DataReader = DataReader(db_connector)
        data: DataFrame = data_reader.read_from_table('PERSONS')
        ExcelCreator.create_excel(data)

        print(f'A planilha foi crida contendo {data.size} itens')
    main()
