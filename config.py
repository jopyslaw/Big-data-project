from dotenv import load_dotenv
from os import environ

load_dotenv()

# Scheme: "postgres+psycopg2://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>"

USERNAME = environ.get('DB_USER_NAME')
PASSWORD = environ.get('DB_USER_PASSWORD')

