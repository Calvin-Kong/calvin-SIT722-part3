from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://project3_pvh7_user:veCnTtiYGXxiouZdq1gjrgmcOfvtE15R@dpg-crihg0jv2p9s738i6keg-a.oregon-postgres.render.com/project3_pvh7" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
