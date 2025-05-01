import os
from datetime import datetime, timedelta

days_to_process = 5000


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
        self.ID = ID
        self.CREATE_DATE_UTC = CREATE_DATE_UTC
        self.SKU = SKU
        self.TITLE = TITLE
        self.QUANTITY = QUANTITY
        self.UNIT_PRICE = UNIT_PRICE
        self.TAX_PRICE = TAX_PRICE
        self.SHIPPING_PRICE = SHIPPING_PRICE
        self.SHIPPING_TAX_PRICE = SHIPPING_TAX_PRICE
        self.DISTRIBUTION_CENTER = DISTRIBUTION_CENTER
        self.ORDER_ID = ORDER_ID


class DataToInsert:
    def __init__(self):
        self.DATA = []


DATA_TO_INSERT = DataToInsert()


# Used only on firstAuth.py
class EndpointsFirstAuth:
    def __init__(self):
        self.ENDPOINT = "https://api.channeladvisor.com/oauth2/authorize"
        self.REDIRECT_URI = ""
