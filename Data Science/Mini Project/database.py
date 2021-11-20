from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
Base = declarative_base()
class Passwords(Base):
    __tablename__ = "passwords"
    username = Column(String, primary_key = True)
    password = Column(String)

if __name__== "__main__":
    engine = create_engine("sqlite:///mydatabase.sqlite3")
    Base.metadata.create_all(engine)