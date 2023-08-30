import os
import json
from confluent_kafka import Consumer, KafkaError
import config
import ast
from models.flight import Flight,get_session,setup_tables
import time


consumer = Consumer(config.KAFKA_CONFIG)

#Subscribe to topic
consumer.subscribe([config.KAFKA_TOPIC])
setup_tables()


while True:
    msg = consumer.poll(1)
    
    
    if msg is None:
       
        continue

    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            continue
        else:
            print(msg.error())
            break
    session=get_session()
    try:
        
        msg_value = ast.literal_eval(msg.value().decode('utf-8'))
        print(msg_value)

        # Check if the message has keys to create or update a Flight object
        required_keys = {'flight_number', 'origin', 'destination', 'departure_time', 'arrival_time'}
        if required_keys.issubset(msg_value.keys()):
            flight = session.query(Flight).filter_by(flight_number=msg_value['flight_number']).first()

            if flight is None:
                # Create new Flight object
                coords=msg_value["xy"]
                del msg_value["xy"]
                flight = Flight(**msg_value)
                flight.current_location=str(coords)
                session.add(flight)
            else:
                # Update existing Flight object
                coords=msg_value["xy"]
                del msg_value["xy"]
                msg_value["current_location"]=str(coords)
                for key, value in msg_value.items():

                    setattr(flight, key, value)
                session.merge(flight)    

            session.commit()

    except json.JSONDecodeError:
        print("Message could not be decoded into JSON format.")
        session.rollback()
        
    
    finally:
        if session:
            session.close()
    time.sleep(1)        
        
consumer.close()