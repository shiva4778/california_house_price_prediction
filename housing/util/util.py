import yaml
from housing.exception import HousingException
import os
import sys


def read_yaml_file(file_path:str)->dict:
    '''
    Used to read yaml file
    
    '''
    try:
        with open(file_path,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(e,sys) from e
    

