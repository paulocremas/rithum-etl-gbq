import pytz
from dateutil import parser
from datetime import datetime

cst = pytz.timezone("America/Chicago")  # This timezone is also CST
utc = pytz.utc


def convertDateTimeCstToUtc(date):
    date = date.replace(tzinfo=cst)
    return date.astimezone(utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def convertStringUtcToCst(date):
    return parser.isoparse(date).astimezone(cst).replace(tzinfo=None)


def nowUtc():
    return datetime.now(utc).strftime("%Y-%m-%dT%H:%M:%SZ")
