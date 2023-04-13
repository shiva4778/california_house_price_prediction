from setuptools import setup
from typing import List,Dict




#Declaring variable for setup function
PROJECT_NAME="housing-predictor"
versions='3.9.12'
author='Shivanshu'
descriptions="Complete industrial level machine learning project"
PACKAGES=['housing']
REQUIREMENTS_FILE_NAME='requirements.txt'
def get_requirements_list()->List[str]:
    """
    This function is going to return the list of library present in requirements.txt
    
    
    """
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines() 


setup(
    name=PROJECT_NAME,
      version=versions,
      author=author,
      description=descriptions,
      packages=PACKAGES,
      install_requires=get_requirements_list()
      )





