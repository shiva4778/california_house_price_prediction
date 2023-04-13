from flask import Flask
from housing.logger import logging
import sys
from housing.exception import HousingException
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    logging.info('Raising exception intentionally')
    try:
        a=1/0
    
    except Exception as e:
        housing=HousingException(e,sys)
        logging.info(housing.error_message)
        
        raise HousingException(e,sys)

    return 'ci cd pipeline'
if __name__=='__main__':
    app.run(debug=True)

