import pandas as pd
from sqlalchemy import create_engine
import json

# Credentials to database connection
hostname="localhost"
dbname="digitalskola"
uname="root"
pwd="M0n3g45x"
 
# Opening JSON file
f = open('data_covid.json')
data = json.load(f)
data = data["data"]["content"]

print(data[0])

# Create dataframe
df = pd.DataFrame(data)

# Create SQLAlchemy engine to connect to MySQL Database
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
				.format(host=hostname, db=dbname, user=uname, pw=pwd))

# Convert dataframe to sql table                                   
df.to_sql('reza_raw_covid', engine, index=False)
