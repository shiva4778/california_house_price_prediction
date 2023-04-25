from housing.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig, \
ModelTrainerConfig , ModelEvaluationConfig,ModelPusherConfig,TrainingPipelineConfig
from housing.util.util import read_yaml_file
from housing.constant import *
from housing.exception import HousingException
import os
import sys
from housing.logger import logging

class Configuration:
    
    def __init__(self,config_file_path=CONFIG_FILE_PATH,
                 current_time_stamp:str=CURRENT_TIME_STAMP)->None:
        self.config_info=read_yaml_file(file_path=config_file_path)
        self.get_training_pipeline_config=self.get_training_pipeline_config()
        self.time_stamp=current_time_stamp

         

        
    def get_data_ingestion_config(self)->DataIngestionConfig:
        try:
            artifact_dir=self.training_pipeline_config.artifact_dir
            data_ingestion_artifact_dir=os.path.join(artifact_dir,DATA_INGESTION_ARTIFACT_DIR,self.time_stamp)
            data_ingestion_info=self.config_info[DATA_INGESTION_CONFIG_KEY]
            dataset_download_url=data_ingestion_info[DATA_INGESTION_ARTIFACT_DIR]
            dataset_download_dir=os.path.join(data_ingestion_artifact_dir,data_ingestion_info[DATA_INGESTION_DOWNLOAD_URL_KEY])
            
            tgz_download_dir=os.path.join(data_ingestion_artifact_dir,data_ingestion_info[DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY])
    
            
            
            raw_data_dir=os.path.join(data_ingestion_artifact_dir,data_ingestion_info[DATA_INGESTION_RAW_DATA_DIR_KEY])
            ingested_data_dir=os.path.join(data_ingestion_artifact_dir,data_ingestion_info[DATA_INGESTION_INGESTED_DIR_NAME_KEY])
            ingested_train_dir=os.path.join(ingested_data_dir,data_ingestion_info[DATA_INGESTION_TRAIN_DIR_KEY])
            ingested_test_dir=os.path.join(ingested_data_dir,data_ingestion_info[DATA_INGESTION_TEST_DIR_KEY])

            data_ingestion_config=DataIngestionConfig(dataset_download_url=dataset_download_url,
            tgz_download_dir=tgz_download_dir,
            raw_data_dir=raw_data_dir,
            ingested_train_dir=ingested_train_dir,
            ingested_test_dir=ingested_test_dir)

            logging.info(f"Data Ingestion Config :{data_ingestion_config}")
            return data_ingestion_config
            
        except Exception as e:
            raise(e,sys)
    
    def get_data_validation_config(self)->DataValidationConfig:

        try:
            artifact_dir=self.get_training_pipeline_config.artifact_dir
            data_validation_artifact_dir=os.path.join(artifact_dir,DATA_VALIDATION_ARTIFACT_DIR)
            data_validation_info=self.config_info[DATA_VALIDATION_CONFIG_KEY]
            schema_dir=os.path.join(data_validation_artifact_dir,data_validation_info[DATA_VALIDATION_SCHEMA_DIR_KEY])
            schema_file_name=os.path.join(schema_dir,data_validation_info[DATA_VALIDATION_SCHEMA_FILE_NAME_KEY])
            report_file_name=os.path.join(schema_dir,data_validation_info[DATA_VALIDATION_REMOTE_FILE_NAME_KEY])
            report_page_file_name=os.path.join(schema_dir,data_validation_info[DATA_VALIDATION_REPORT_PAGE_FILE_NAME_KEY])

            data_validation_config=DataIngestionConfig(schema_dir=schema_dir)
            logging.info(f"Data Validation Config:{data_validation_config}")
            return data_validation_config

        except Exception as e:
            raise(e,sys)
    def get_data_transformation_config(self)->DataTransformationConfig:
        try:
            artifact_dir=self.get_training_pipeline_config.artifact_dir
            data_transformation_artifact_dir=os.path.join(artifact_dir,DATA_TRANSFORMATION_ARTIFACT_DIR)
            data_transformation_info=self.config_info[DATA_TRANSFORMATION_CONFIG_KEY]
            data_transformation_add_bedroom_per_room=os.path.join(data_transformation_artifact_dir,data_transformation_info[DATA_TRANSFORMATION_ADD_BEDROOM_PER_ROOM_KEY])
            data_transformation_transformed_dir=os.path.join(data_transformation_artifact_dir,data_transformation_info[DATA_TRANSFORMATION_TRANSFORMED_DIR_KEY])
            data_transformation_transformed_train_dir=os.path.join(data_transformation_transformed_dir,data_transformation_info[DATA_INGESTION_TRAIN_DIR_KEY])
            data_transformation_test_dir=os.path.join(data_transformation_transformed_dir,data_transformation_info[DATA_TRANSFORMATION_TRANSFORMED_TEST_DIR_KEY])
            data_transformation_preprocessing_dir=os.path.join(data_transformation_artifact_dir,data_transformation_info[DATA_TRANSFORMATION_PREPROCESSING_DIR_KEY])
           
            data_transformation_preprocessed_object_file_name=os.path.join(data_transformation_preprocessing_dir,data_transformation_info[DATA_TRANSSFORMATION_PREPROCESSED_OBJECT_FILE_NAME_KEY])
           
            data_transformation_config=DataTransformationConfig(add_bedroom_per_room=data_transformation_add_bedroom_per_room,transformed_test_dir=data_transformation_test_dir,transformed_train_dir=data_transformation_transformed_train_dir,preprocessed_object_file_path=data_transformation_preprocessing_dir)
            logging.info(f"Data Transformation Config :{data_transformation_config}")

            return data_transformation_config

        except Exception as e:
            raise(e,sys)
    def get_model_evaluation_config(self):
        try:
            artifact_dir=self.get_training_pipeline_config.artifact_dir
            model_evaluation_artifact_dir=os.path.join(artifact_dir,MODEL_TRAINER_DIR)
            trained_model_info=self.config_info[MODEL_TRAINER_CONFIG_KEY]
            trained_model_dir=os.path.join(model_evaluation_artifact_dir,trained_model_info[TRAINED_MODEL_DIR_KEY])
            model_file_name=os.path.join(trained_model_dir,trained_model_info[MODEL_FILE_NAME_KEY])
            model_base_accuarcy=os.path.join(trained_model_dir,trained_model_dir[MODEL_BASE_ACCURACY_KEY])

            model_config_dir_key=os.path.join(trained_model_dir,trained_model_info[MODEL_CONFIG_DIR_KEY])

            model_config_file_name=os.path.join(model_config_dir_key,trained_model_info[MODEL_CONFIG_FILE_NAME])
            model_trainer_config=ModelTrainerConfig(trained_model_file_path=model_file_name,base_accuracy=model_base_accuarcy)
            logging.info(f'Model evaluation config:{trained_model_dir}')
            return model_trainer_config


            
        except Exception as e:
            raise(e,sys)
    def get_model_pusher_config(self):
        try:
            artifact_dir=self.get_training_pipeline_config.artifact_dir
            model_pusher_config_dir=os.path.join(artifact_dir,MODEL_PUSHER_CONFIG_DIR_KEY)
            model_pusher_info=self.config_info[MODEL_PUSHER_CONFIG_KEY]
            model_pusher_export_dir=os.path.join(model_pusher_config_dir,model_pusher_info[MODEL_PUSHER_EXPORT_DIR_KEY])
            model_pusher_config=ModelPusherConfig(export_dir_path=model_pusher_export_dir)
            logging.info(f'Model pusher Config:{model_pusher_config}')
            return model_pusher_config
        except Exception as e:
            raise(e,sys)
    def get_training_pipeline_config(self)->TrainingPipelineConfig:
        try:
            training_pipeline_config=self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir=os.path.join(ROOT_DIR,training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY])
            training_pipeline_config=TrainingPipelineConfig(artifact_dir=artifact_dir)
            return training_pipeline_config
        except Exception as e:
            raise HousingException(e,sys) from e
        

    