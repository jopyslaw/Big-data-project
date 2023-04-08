from dotenv import load_dotenv
from os import environ

load_dotenv()

# Scheme: "postgres+psycopg2://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>"

USERNAME = environ.get('DB_USER_NAME')
PASSWORD = environ.get('DB_USER_PASSWORD')

DATABASE_URI = f'postgresql+psycopg2://{USERNAME}:{PASSWORD}@195.150.230.208:5432/2022_jop_konrad'