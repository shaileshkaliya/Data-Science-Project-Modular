from src.DS_Project.logger import logging
from src.DS_Project.exception import CustomException
from src.DS_Project.components.data_ingestion import DataIngestion
import sys
import os 

if __name__=='__main__':
    d = DataIngestion();
    d.initiate_data_ingestion();