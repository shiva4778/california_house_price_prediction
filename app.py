from flask import Flask
from housing.logger import logging
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    logging.info('this is my first logging')
    return 'ci cd pipeline'
if __name__=='__main__':
    app.run(debug=True)

