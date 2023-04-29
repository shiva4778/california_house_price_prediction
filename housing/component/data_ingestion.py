from housing.exception import HousingException
from housing.logger import logging
from housing.entity.config_entity import DataIngestionConfig
from housing.entity.artifact_entity import DataIngestionArtifact
import sys
import tarfile
from six.moves import urllib
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit





class DataIngestion:

    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            data_ingestion_config=DataIngestionConfig()
            
            logging.info(f"{'='*20} Data Ingestion log started.{'='*20}")
    

        except Exception as e:

            HousingException(e,sys)

    def download_housing_data(self,):
        try:
            #Extracting remote url to download datset
            download_url=self.data_ingestion_config.dataset_download_url

            #folder location to download file

            tgz_download_dir=self.data_ingestion_config.tgz_download_url
            os.makedirs(tgz_download_dir,exist_ok=True)

            #folder location to download file
            housing_file_name=os.path.basename(download_url)
            tgz_download_dir=self.data_ingestion_config.tgz_download_url
            tgz_file_path=os.path.join(tgz_download_dir,housing_file_name)
            urllib.requests.urlretrieve(download_url,tgz_file_path)
            logging.info(f"Downloading file from:[{download_url}] into :[{tgz_file_path}]")
            return tgz_file_path
        except Exception as e:
            raise HousingException(e,sys) from e

    def extract_tgz_file(self,tgz_file_path:str):
        try:
            raw_data_dir=self.data_ingestion_config.raw_data_dir
            os.makedirs(raw_data_dir,exist_ok=True)
            logging.info(f"Extracting tgz file :[{tgz_file_path}] into dir:[{raw_data_dir}]")
            with tarfile.open(tgz_file_path) as housing_tgz_file_obj:
                housing_tgz_file_obj.extractall(path=raw_data_dir)
        except Exception as e:
            raise HousingException(e,sys) from e

    def split_data_as_train_test(self)-> DataIngestionArtifact:
        try:
            raw_data_dir=self.data_ingestion_config.raw_data_dir

            file_name=os.listdir(raw_data_dir)[0]
            
            housing_file_path=os.path.join(raw_data_dir,file_name)
            logging.info(f'Reading file path:[{housing_file_path}]')

            housing_data_frame=pd.read_csv(housing_file_path)

            housing_data_frame['income_cat']=pd.cut(housing_data_frame['median_income']
                        bins=[0,1.5,3,4.5,6,np.inf],labels=[1,2,3,4,5])

            logging.info(f'Splitting data into train and test')
            strat_train_set=None
            strat_test_set=None

            split=StratifiedShuffleSplit(n_split=1,test_size=0.2,random_state=42)

            for train_index,test_index in split.split(housing_data_frame,housing_data_frame['income_cat']):
                strat_train_set=housing_data_frame.loc[train_index].drop(['income_cat'],axis=1)
                strat_test_set=housing_data_frame.loc[train_index].drop(['income_cat'],axis=1)
            
            train_file_path=os.path.join(self.data_ingestion_config.ingested_train_dir,file_name)# We can us df.to_csv() function
            test_file_path=os.path.join(self.data_ingestion_config.ingested_test_dir,file_name)

            if strat_train_set is not None:
                os.makedirs(self.data_ingestion_config.ingested_test_dir,exist_ok=True)
                
                logging.info(f"Exporting training dataset to file:[{train_file_path}]")
                strat_test_set.to_csv(train_file_path,index=False)

            if strat_test_set is not None:
                os.makedirs(self.data_ingestion_config.ingested_test_dir,exist_ok=True)
                logging.info(f"Exporting test dataset to file:[{test_file_path}]")
                strat_test_set.to_csv(test_file_path,index=False)

            data_ingestion_artifact=DataIngestionArtifact(train_file_path=train_file_path,test_file_path=test_file_path)
            

            logging.info(f"Data Ingestion artifact :[{data_ingestion_artifact}]")


        except Exception as e:
            raise HousingException(e,sys)

    def initiate_data_ingestion(self)->DataIngestionArtifact:
        try:
            tgz_file_path=self.download_url
            self.extract_tgz_file(tgz_file_path=tgz_file_path)


        except Exception as e:
            raise HousingException(e,sys) from e
        
    def __del__(self):
        logging.info(f"{'='*20} Data Ingestion log completed{'='*20} \n\n")





