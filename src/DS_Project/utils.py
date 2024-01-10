from src.DS_Project.logger import logging
from src.DS_Project.exception import CustomException
import sys
import os
from dotenv import load_dotenv
import pymysql
import pandas as pd
import pickle

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

def save_obj(file_path, obj):
    try:
        file_dir = os.path.dirname(file_path)
        os.makedirs(file_dir, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e,sys);