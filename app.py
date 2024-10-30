from flask import Flask
from housing.logger import logging
from housing.exception import HousingExecption
import sys

app = Flask(__name__)

@app.route('/')
def hello_world():

    try:
        raise Exception("We are testing exception")
    except Exception as e:
        housing = HousingExecption(e,sys) 
        logging.info(housing.error_message)
        logging.info("We are testings logging")
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
