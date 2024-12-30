import os
import sys
from src.Corona.exception import CustomException
from src.Corona.logger import logging
import pandas as pd
import pymysql


from dotenv import load_dotenv
load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv("db")


def read_sql_data():
    logging.info("mysql started")
    try:
        mydb = pymysql.Connect(
            
            host=host,
            user=user,
            password=password,
            db=db
        )
        
        logging.info("Completed connection establish of mydb",mydb)
        df= pd.read_sql_query('select * from students',mydb)
        print(df.head())
        return df
    except Exception as ex:
        raise CustomException(ex)
    