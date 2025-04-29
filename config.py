import os
from datetime import datetime, timedelta

days_to_process = 5


class APIConfig:
    def __init__(self):
        self.CLIENT_ID = os.environ.get("APPLICATION_ID")
        self.CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
        self.REFRESH_TOKEN = os.environ.get("REFRESH_TOKEN")
        self.TOKEN_ENDPOINT = "https://api.channeladvisor.com/oauth2/token"


class AccessToken:
    def __init__(self):
        self.ACCESS_TOKEN = None
        self.EXPIRES_IN = None


class DistributionCenters:
    def __init__(self):
        self.ENDPOINT = "https://api.channeladvisor.com/v1/DistributionCenters"
        self.KEYS = ["ID", "Name"]
        self.DISTRIBUTION_CENTERS_DICT = None


# Preciso corrigir as horas (checar com cliente)
class DateParams:
    def __init__(self):
        start_date = (datetime.now() - timedelta(days=days_to_process)).strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        )
        end_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        param_filter = (
            f"CreatedDateUtc ge {start_date} and CreatedDateUtc le {end_date}"
        )
        params = {
            "$filter": param_filter,
        }
        self.PARAMS = params


class Orders:
    def __init__(self):
        self.ENDPOINT = "https://api.channeladvisor.com/v1/Orders"
        self.KEYS = ["ID", "CreatedDateUtc"]
        self.PARANS = []


class Fulfilments:
    def __init__(self):
        self.ENDPOINT = (
            f"https://api.channeladvisor.com/v1/Orders({{order_id}})/Fulfillments"
        )
        self.KEYS = ["DistributionCenterID"]


class ItemInOrder:
    def __init__(self):
        self.ITEM_ORDER_ID = (
            f"https://api.channeladvisor.com/v1/Orders({{order_id}})/Items"
        )
        self.ORDER_ID = [
            "ID",
            "Sku",
            "Title",
            "Quantity",
            "UnitPrice",
            "TaxPrice",
            "ShippingPrice",
            "ShippingTaxPrice",
        ]


class Item:
    def __init__(self):
        self.ID = None
        self.Created_DATE_UTC = None
        self.SKU = None
        self.TITLE = None
        self.QUANTITY = None
        self.UNIT_PRICE = None
        self.TAX_PRICE = None
        self.SHIPPING_PRICE = None
        self.SHIPPING_TAX_PRICE = None
        self.DISTRIBUTION_CENTER = None
        self.ORDER_ID = None


class DataToInsert:
    def __init__(self):
        self.DATA = []


# Used only on firstAuth.py
class EndpointsFirstAuth:
    def __init__(self):
        self.AUTHORIZE_ENDPOINT = "https://api.channeladvisor.com/oauth2/authorize"
        self.REDIRECT_URI = ""
