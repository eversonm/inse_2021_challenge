import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

SQLALCHEMY_DATABASE_URI = (
    "postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}".format(
        user=os.environ.get("INSE_DB_USER"),
        passwd=os.environ.get("INSE_DB_PASSWORD"),
        host=os.environ.get("INSE_DB_HOST"),
        port=os.environ.get("INSE_DB_PORT"),
        db=os.environ.get("INSE_DB_NAME"),
    )
)
