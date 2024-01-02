from src.DS_Project.logger import logging
from src.DS_Project.exception import CustomException
import sys
import os
from dotenv import load_dotenv
import pymysql
import pandas as pd

load_dotenv()

host=os.getenv("host")
password=os.getenv("password")
user=os.getenv("user")
db=os.getenv("db")

def read_sql_data() :
    logging.info("Reading data from mySQL databse started")
    try:
        myDB = pymysql.connect(
            host=host,
            password=password,
            user=user,
            db=db
        )
        logging.info("Connection estabilished with mySQL databse")
        df = pd.read_sql_query("Select * from students", myDB);
        print(df.head())
        return df;

    except Exception as e:
        raise CustomException(e,sys);