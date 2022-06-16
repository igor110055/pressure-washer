import traceback
from datetime import datetime

from config import ENV
from utils import LOGGER

from src.orderbook_ws import open_orderbook

MARKET = 'BTC/USD'

def run():
    """ 
    Starting point for ETL
    ...
    """
    LOGGER.info('starting etl')
    LOGGER.info('step 1: opening orderbook')
    open_orderbook(market=MARKET)
    LOGGER.info('step 2: closing orderbook')
    LOGGER.info('completed etl')


if __name__ == '__main__':
    try: 
        run()
    except Exception as runtime_exception:
        raise runtime_exception