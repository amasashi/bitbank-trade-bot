import datetime
import logging
import sys

from app.models.candle import Candle
from app.models.database import init_db
import settings


logging.basicConfig(level=logging.INFO, stream=sys.stdout)


if __name__ == "__main__":
    init_db(True)

    




