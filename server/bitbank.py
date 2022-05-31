import logging
import python_bitbankcc
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)


class Public(object):
    def __init__(self):
        self.public = python_bitbankcc.public()

    def get_candles(self, pair='btc_jpy', candle_type='1hour', days=13):
        open_li = []
        high_li = []
        low_li = []
        close_li = []
        vol_li = []
        time_li = []
        date = datetime.now()
        
        if date.hour < 9:
            date = date - timedelta(days=1)
        
        try:
            for i in range(days):
                date_ = (date - timedelta(days=days-1-i)).strftime('%Y%m%d')
                candles = self.public.get_candlestick(pair=pair, candle_type=candle_type, yyyymmdd=date_)['candlestick'][0]['ohlcv']
                for candle in candles:
                    open = candle[0]
                    high = candle[1]
                    low = candle[2]
                    close = candle[3]
                    vol = candle[4]
                    open_li.append(open)
                    high_li.append(high)
                    low_li.append(low)
                    close_li.append(close)
                    vol_li.append(vol)
                    time = datetime.fromtimestamp(candle[5]/1000)
                    time_li.append(time)
                    from app.models.candle import Candle
                    Candle.create(time, open, high, low, close, vol)
                    
            df = pd.DataFrame(zip(time_li, open_li, high_li, low_li, close_li, vol_li), columns=['time', 'open', 'high', 'low', 'close', 'vol'])
            return df
        except Exception as e:
            logging.error(f'action=get_candles error={e}')
            return False
