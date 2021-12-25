import os

db_host = os.getenv('DB_HOST', default='localhost')
db_name = os.getenv('DB_NAME', default='dashbaord')
db_password = os.getenv('DB_PASSWORD')
db_port = os.getenv('DB_PORT', default='5342')
db_user = os.getenv('DB_USERNAME', default='dashboard')

SQLALCHEMY_DATABASE_URI = f'postgres://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
