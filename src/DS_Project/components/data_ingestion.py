import os
import sys
from src.DS_Project.logger import logging
from src.DS_Project.exception import CustomException
import pandas as pd
from src.DS_Project.utils import read_sql_data
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestConfig:
    train_data_path:str = os.path.join('artifacts','train.csv');
    test_data_path:str = os.path.join('artifacts','test.csv');
    raw_data_path:str = os.path.join('artifacts','rawData.csv');

class DataIngestion:
    def __init__(self):
        self.ingestionConfig = DataIngestConfig();

    def initiate_data_ingestion(self):
        try:
            df = read_sql_data();
            logging.info("Reading completed from databse")

            os.makedirs(os.path.dirname(self.ingestionConfig.train_data_path),exist_ok=True)

            df.to_csv(self.ingestionConfig.raw_data_path, index=False, header=True)
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestionConfig.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestionConfig.test_data_path,index=False,header=True)

            logging.info("Data Ingestion completed !")

        except Exception as e:
            logging.info(CustomException(e, sys))