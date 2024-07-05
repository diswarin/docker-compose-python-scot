import pandas as pd
from sqlalchemy import create_engine

Server = 'LENOVOKUM\WINCC'
Database ='CI_DB_1'
Driver ='ODBC Driver 17 for SQl Server'
Database_con = 'mssql://@{Server}/{Database}?{Driver}'


engine = create_engine(Database_con)
con=engine.connect()


#df =pd.read_sql('A1' ,con)

#print(df)
