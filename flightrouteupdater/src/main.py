import os
import json
from confluent_kafka import Consumer, KafkaError
import config
import ast
import time
from pymongo import MongoClient




    

consumer = Consumer(config.KAFKA_CONFIG)

#Subscribe to topic
consumer.subscribe([config.KAFKA_TOPIC])

client=MongoClient(config.MONGO_URL)
db=client["flights_route"]  


while True:
    msg = consumer.poll(1)
    #msg=Msg(idx)
    
    
    if msg is None:
       
        continue

    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            continue
        else:
            print(msg.error())
            break
  
    try:
        
        msg_value = ast.literal_eval(msg.value().decode('utf-8'))
        print(msg_value)

        # Check if the message has keys to create or update a Flight object
        required_keys = {'flight_number', 'origin', 'destination', 'departure_time', 'arrival_time'}
        if required_keys.issubset(msg_value.keys()):
            flight_number=msg_value['flight_number']
            departure_time=msg_value['departure_time']
            collection=db[flight_number]
            update={"time": msg_value["last_updated_time"],"latitude": round(float(msg_value["xy"][0]),4),"longitude": round(float(msg_value["xy"][1]),4) }
            doc=collection.find_one({ departure_time: {"$exists": "true" }})
            if doc:
                collection.update_one({departure_time: {"$exists": "true" }},{"$push": {departure_time: update}})
            else:
                collection.insert_one({departure_time: [update]})



       

    except json.JSONDecodeError:
        print("Message could not be decoded into JSON format.")
 
        
      
    time.sleep(1)
       
consumer.close()