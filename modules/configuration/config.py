import os
from datetime import datetime, timedelta
from pandas import DataFrame
from dateutil import parser
import pytz

days_to_process = 1


class APIConfig:
    def __init__(self):
        self.CLIENT_ID = os.environ.get("APPLICATION_ID")
        self.CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
        self.REFRESH_TOKEN = os.environ.get("REFRESH_TOKEN")
        self.ENDPOINT = "https://api.channeladvisor.com/oauth2/token"


API_CONFIG = APIConfig()


class AccessToken:
    def __init__(self):
        self.ACCESS_TOKEN = None
        self.EXPIRES_IN = None


ACCESS_TOKEN = AccessToken()


class DistributionCenters:
    def __init__(self):
        self.ENDPOINT = "https://api.channeladvisor.com/v1/DistributionCenters"
        self.KEYS = ["ID", "Name"]
        self.DISTRIBUTION_CENTERS_DICT = None


DISTRIBUTION_CENTERS = DistributionCenters()


class OrdersApiCall:
    def __init__(self):
        self.ENDPOINT = "https://api.channeladvisor.com/v1/Orders"
        self.KEYS = ["ID", "CreatedDateUtc"]
        self.PARAMS = SetOrdersApiDateParams()


def SetOrdersApiDateParams():
    start_date = (datetime.now() - timedelta(days=days_to_process)).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )
    end_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
    param_filter = f"CreatedDateUtc ge {start_date} and CreatedDateUtc le {end_date}"
    params = {
        "$filter": param_filter,
    }
    return params


ORDERS_API_CALL = OrdersApiCall()


class Fulfillments:
    def __init__(self):
        self.ENDPOINT = (
            f"https://api.channeladvisor.com/v1/Orders({{ORDER_ID}})/Fulfillments"
        )
        self.KEYS = ["DistributionCenterID"]
        self.ORDER_ID = None


FULFILLMENTS = Fulfillments()


class ItemInOrder:
    def __init__(self):
        self.ENDPOINT = f"https://api.channeladvisor.com/v1/Orders({{ORDER_ID}})/Items"
        self.KEYS = [
            "ID",
            "Sku",
            "Title",
            "Quantity",
            "UnitPrice",
            "TaxPrice",
            "ShippingPrice",
            "ShippingTaxPrice",
        ]
        self.ORDER_ID = None


ITEM_IN_ORDER = ItemInOrder()


class CurrentOrder:
    def __init__(self):
        self.ID = None
        self.CREATE_DATE_UTC = None


CURRENT_ORDER = CurrentOrder()


class Item:
    def __init__(
        self,
        ID,
        CREATE_DATE_UTC,
        SKU,
        TITLE,
        QUANTITY,
        UNIT_PRICE,
        TAX_PRICE,
        SHIPPING_PRICE,
        SHIPPING_TAX_PRICE,
        DISTRIBUTION_CENTER,
        ORDER_ID,
    ):
        self.id = ID
        self.create_date = parser.isoparse(CREATE_DATE_UTC).astimezone(
            pytz.timezone("America/Los_Angeles")
        )
        self.sku = SKU
        self.title = TITLE
        self.quantity = QUANTITY
        self.unit_price = UNIT_PRICE
        self.tax_price = TAX_PRICE
        self.shipping_price = SHIPPING_PRICE
        self.shipping_tax_price = SHIPPING_TAX_PRICE
        self.distribution_center = DISTRIBUTION_CENTER
        self.order_id = ORDER_ID


class DataToInsert:
    def __init__(self):
        self.DATA = DataFrame()


DATA_TO_INSERT = DataToInsert()


class BigQueryConfig:
    def __init__(self):
        self.TABLE_ID = os.environ.get("TABLE_ID")
        self.GOOGLE_APPLICATION_CREDENTIALS = os.environ.get(
            "GOOGLE_APPLICATION_CREDENTIALS"
        )
        self.BUCKET_URI = os.environ.get("BUCKET_URI")


# Used only on firstAuth.py
class EndpointsFirstAuth:
    def __init__(self):
        self.ENDPOINT = "https://api.channeladvisor.com/oauth2/authorize"
        self.REDIRECT_URI = ""
