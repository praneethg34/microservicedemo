import os
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import config
import datetime
from pymongo import MongoClient

Base = declarative_base()

client=MongoClient(config.MONGO_URL,connectTimeoutMS=5000)
db=client["flights_route"]  



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


def get_all_flights():
    output=[]
    session=get_session()
    try:
        flights=session.query(Flight).all()
        for flight in flights:
            flight_dict={}
            flight_dict["flight_number" ]=flight.flight_number
            flight_dict["origin"]=flight.origin
            flight_dict["destination"]=flight.destination
            flight_dict["departure_time"]=flight.departure_time
            flight_dict["arrival_time"]=flight.arrival_time
            flight_dict["current_estimate"]=flight.current_estimate
            flight_dict["last_updated_time"]= flight.last_updated_time
            output.append(flight_dict)
        return output    
    except Exception as err:
        print(err)
        return False
    finally:
        session.close()

def get_flight(flight_number):
    session=get_session()
    try:
        flights=session.query(Flight).filter(Flight.flight_number==flight_number).all()
        
        return flights  
    except Exception as err:
        print(err)
        return False
    finally:
        session.close()



    
def get_flight_route(flight_number,departure_time):
    collection=db[flight_number]
    routedoc=collection.find_one({ departure_time: {"$exists": "true" }})
    if routedoc:
        
        return routedoc[departure_time]
    else:
        return {}