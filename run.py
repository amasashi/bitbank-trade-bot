import datetime
import logging
import sys

from app.models.candle import Candle

logging.basicConfig(level=logging.INFO, stream=sys.stdout)


if __name__ == "__main__":
    import app.models
    now = datetime.datetime.now()
    Candle.create(now, 1.0, 2.0, 1.0, 2.0, 1.0)
    candle = Candle.get(now)
    print(candle.open)
    candle.open = 3.0
    candle.save()
    print(candle.open)


