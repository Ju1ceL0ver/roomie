import pandas as pd
from sqlalchemy import create_engine

# Укажи свой путь к базе данных
DATABASE_PATH = "sqlite:////Users/aleksejzagorskij/roomie/instance/roommates.db" 

engine = create_engine(DATABASE_PATH)
query = "SELECT * FROM user"
df = pd.read_sql(query, engine)
print(df)
df.to_csv('users_output.csv', index=False)