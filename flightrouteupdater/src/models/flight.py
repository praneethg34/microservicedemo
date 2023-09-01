import os
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import config
import datetime

Base = declarative_base()



env = os.environ.get('env', 'test')
if env == 'production':
    engine = create_engine(f'postgresql://{config.PGDB_USER}:{config.PGDB_PASS}@{config.PGDB_HOSTPORT}/{config.PGDB}')
else:
    engine = create_engine('sqlite:///flights_test.db')

class Flight(Base):
    __tablename__ = 'flights'

   
    flight_number = Column(String(50), nullable=False,primary_key=True)
    origin = Column(String(50), nullable=False)
    destination = Column(String(50), nullable=False)
    departure_time = Column(String, nullable=False)
    arrival_time = Column(String, nullable=False)
    current_estimate=Column(String(50), nullable=True)
    current_location = Column(String(50), nullable=True)
    last_updated_time = Column(String, nullable=True)

# Read environment variable to decide which database to use



def setup_tables():
    Base.metadata.create_all(engine)

# Create a session to interact with the database
def get_session():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def add_merge_flight_details(flight,session):
    session.merge(flight)
    session.commit()


