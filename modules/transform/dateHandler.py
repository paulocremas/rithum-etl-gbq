import pytz
from dateutil import parser
from datetime import datetime, timedelta

"""
Converts time, this is used when reading and inserting data. 
Data is requested as UTC and stored as CST.
"""

cst = pytz.timezone("America/Chicago")  # This timezone is also CST
utc = pytz.utc


def convertDateTimeCstToUtc(date):
    date = date + timedelta(seconds=1)
    date = cst.localize(date)
    return date.astimezone(utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def convertStringUtcToCst(date):
    return parser.isoparse(date).astimezone(cst).replace(tzinfo=None)


def nowUtc():
    return datetime.now(utc).strftime("%Y-%m-%dT%H:%M:%SZ")
