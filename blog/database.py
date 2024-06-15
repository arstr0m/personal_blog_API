from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
from sqlalchemy import create_engine

username = "postgres"
password = "j@Hd#pW4"
host = "localhost"
port = "5432"
database = "personal_blogging"
encoded_password = quote_plus(password)
SQLALCHEMY_DATABASE_URL = f"postgresql://{username}:{encoded_password}@{host}:{port}/{database}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

try:
    with engine.connect() as connection:
        print("Conexión exitosa!")
except Exception as e:
    print(f"Error al conectar: {e}")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()