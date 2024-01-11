from src.DS_Project.logger import logging
from src.DS_Project.exception import CustomException
import sys
import os
from dotenv import load_dotenv
import pymysql
import pandas as pd
import pickle
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score

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

def evaluate_models(X_train, y_train, X_test, y_test, models, params):
    try:
        report = {}
        for i in range(len(list(models))):
            model = list(models.values())[i]
            param = params[list(models.keys())[i]]

            gs = GridSearchCV(model, param, cv=3);
            gs.fit(X_train, y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)

            y_test_pred = model.predict(X_test)
            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score
        return report;
    except Exception as e:
        raise CustomException(e,sys);