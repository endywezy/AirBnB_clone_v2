
from sqlalchemy import create_engine

DB_USER = 'hbnb_dev'
DB_PASSWORD = 'soccer'
DB_HOST = 'localhost'
DB_NAME = 'hbnb_dev_db'

engine = create_engine(f'mysql+mysqldb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}')

try:
    connection = engine.connect()
    print("Connection to the database was successful.")
    connection.close()
except Exception as e:
    print(f"An error occurred: {e}")            
