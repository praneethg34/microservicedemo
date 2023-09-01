import os


env=os.environ

PGDB_USER=env.get("DB_USER","user1")
PGDB_PASS=env.get("DB_PASS","password1")
PGDB_HOSTPORT=env.get("DB_HOST","adp-pgdb-postgresql")
PGDB=env.get("db","adppoc")
MONGO_URL=env.get("MONGO_URL",'mongodb://admin:password123@mongodb-standalone:27017/')
