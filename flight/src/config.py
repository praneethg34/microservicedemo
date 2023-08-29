import os
import pandas as pd


df = pd.read_csv('uscities.csv')
df["citistate"]=df["city"].str.lower()+df["state_id"].str.lower()
env=os.environ
FLIGHT_NUMBER=env.get("FLIGHT_NUMBER","1111")
START_CITY=env.get("FROM_CITY","orlando")
START_STATE=env.get("FROM_STATE","fl")
END_CITY=env.get("TO_CITY","new york")
END_STATE=env.get("TO_STATE","ny")
KAFKA_CONFIG={"bootstrap.servers": env.get("KAFKA_BOOTSTRAP_SERVERS")}
KAFKA_TOPIC="flight_update"