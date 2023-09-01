import os
import pandas as pd


df = pd.read_csv('uscities.csv')
df["citistate"]=df["city"].str.lower()+df["state_id"].str.lower()
env=os.environ
KAFKA_CONFIG={"bootstrap.servers": env.get("KAFKA_BOOTSTRAP_SERVERS"),"group.id": "flight_route_updates"}
KAFKA_TOPIC="flight_update"
PGDB_USER=env.get("DB_USER","user1")
PGDB_PASS=env.get("DB_PASS","password1")
PGDB_HOSTPORT=env.get("DB_HOST","adp-pgdb-postgresql")
PGDB=env.get("db","adppoc")
MONGO_URL=env.get("MONGO_URL",'mongodb://admin:password123@mongodb-standalone:27017/')
