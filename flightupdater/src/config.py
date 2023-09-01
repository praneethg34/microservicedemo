import os

env=os.environ
KAFKA_CONFIG={"bootstrap.servers": env.get("KAFKA_BOOTSTRAP_SERVERS"),"group.id": "flight_updates"}
KAFKA_TOPIC="flight_update"
PGDB_USER=env.get("DB_USER","user1")
PGDB_PASS=env.get("DB_PASS","password1")
PGDB_HOSTPORT=env.get("DB_HOST","adp-pgdb-postgresql")
PGDB=env.get("db","adppoc")
