from housing.exception import HousingException
from housing.logger import logging
import sys
from housing.entity.config_entity import DataIngestionConfig
from housing.constant import *
from housing.config.configuration import Configuration

k=Configuration.get_data_ingestion_config()

a=DataIngestionConfig()
print(a)
        
        
if __name__=='__main__':
    pass
