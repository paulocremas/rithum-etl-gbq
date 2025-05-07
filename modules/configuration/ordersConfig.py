import os
from pandas import DataFrame
from google.cloud import bigquery
from modules.transform.dateHandler import convertDateTimeCstToUtc, nowUtc


class DistributionCenters:
    def __init__(self):
        self.ENDPOINT = "https://api.channeladvisor.com/v1/DistributionCenters"
        self.PARAMS = {"$select": "ID,Name"}
        self.DISTRIBUTION_CENTERS_DICT = None


DISTRIBUTION_CENTERS = DistributionCenters()


class BigQueryConfig:
    def __init__(self):
        self.TABLE_ID = os.environ.get("TABLE_ID")
        self.GOOGLE_APPLICATION_CREDENTIALS = os.environ.get(
            "GOOGLE_APPLICATION_CREDENTIALS"
        )
        self.CLIENT = bigquery.Client()


BIGQUERY_CONFIG = BigQueryConfig()


class OrdersApiCall:
    def __init__(self):
        self.ENDPOINT = "https://api.channeladvisor.com/v1/Orders"
        self.PARAMS = SetOrdersApiParams()


def SetOrdersApiParams():
    try:
        query = f"""
            SELECT create_date
            FROM `{BIGQUERY_CONFIG.TABLE_ID}`
            ORDER BY create_date DESC
            LIMIT 1
        """

        query_job = BIGQUERY_CONFIG.CLIENT.query(query)  # API request
        rows = query_job.result()  # Waits for query to finish

        for row in rows:
            latest_create_date = row.create_date

        param_filter = f"CreatedDateUtc ge {convertDateTimeCstToUtc(latest_create_date)} and CreatedDateUtc le {nowUtc()}"
        params = {"$filter": param_filter, "$select": "ID,CreatedDateUtc"}
    except:
        params = {"$select": "ID,CreatedDateUtc"}

    return params


ORDERS_API_CALL = OrdersApiCall()

# # Uncomment the following lines to set a specific date range
# days_to_process = 2

# from datetime import datetime, timedelta


# def SetOrdersApiParams():
#     start_date = (datetime.now() - timedelta(days=days_to_process)).strftime(
#         "%Y-%m-%dT%H:%M:%SZ"
#     )
#     end_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
#     param_filter = f"CreatedDateUtc ge {start_date} and CreatedDateUtc le {end_date}"
#     params = {"$filter": param_filter, "$select": "ID,CreatedDateUtc"}
#     return params


class Fulfillments:
    def __init__(self):
        self.ENDPOINT = (
            f"https://api.channeladvisor.com/v1/Orders({{ORDER_ID}})/Fulfillments"
        )
        self.PARAMS = {"$select": "DistributionCenterID"}


FULFILLMENTS = Fulfillments()


class ItemInOrder:
    def __init__(self):
        self.ENDPOINT = f"https://api.channeladvisor.com/v1/Orders({{ORDER_ID}})/Items"
        self.PARAMS = {
            "$select": "ID,Sku,Title,Quantity,UnitPrice,TaxPrice,ShippingPrice,ShippingTaxPrice"
        }


ITEM_IN_ORDER = ItemInOrder()


class CurrentOrder:
    def __init__(self):
        self.ID = None
        self.CREATE_DATE_UTC = None
        self.CREATING_ORDER = False


CURRENT_ORDER = CurrentOrder()


class Item:
    def __init__(
        self,
        ID,
        CREATE_DATE,
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
        self.create_date = CREATE_DATE
        self.time_zone = "CST"
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
