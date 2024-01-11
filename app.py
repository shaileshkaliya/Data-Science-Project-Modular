from src.DS_Project.logger import logging
from src.DS_Project.exception import CustomException
from src.DS_Project.components.data_ingestion import DataIngestion
from src.DS_Project.components.data_transformation import DataTransformation
from src.DS_Project.components.model_tranier import ModelTrainer
import sys
import os 

if __name__=='__main__':
    logging.info("The execution has started")

    try:
        #data_ingestion_config=DataIngestionConfig()
        d = DataIngestion();
        train_data_path, test_data_path = d.initiate_data_ingestion();

        #data_transformation_config=DataTransformationConfig()
        data_transformation = DataTransformation();
        train_arr,test_arr,_=data_transformation.initiate_data_transormation(train_data_path,test_data_path)

        # Model Training
        model_trainer = ModelTrainer();
        print(model_trainer.initiate_model_trainer(train_arr,test_arr));
    except Exception as e:
        raise CustomException(e,sys);
