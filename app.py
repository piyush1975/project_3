from src.Corona.logger import logging
from src.Corona.exception import CustomException
import sys



if __name__ == "__main__":
    logging.info("The exicution has started")

    
    try:
        
        a=1/0
    except Exception as e:
        logging.info("Custome Exception")
        raise CustomException(e,sys)
    