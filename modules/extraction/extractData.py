import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from modules.configuration.config import (
    DISTRIBUTION_CENTERS,
    ORDERS_API_CALL,
    ITEM_IN_ORDER,
    FULFILLMENTS,
    CURRENT_ORDER,
    DATA_TO_INSERT,
)
from modules.configuration.config import Item
from modules.extraction.extractDataFromApi import extractDataFromApi
from modules.transform.nameDistributionCenters import getDistributionCenterName


def getDistributionCenters():
    distribution_centers_data = extractDataFromApi(DISTRIBUTION_CENTERS)
    # Transform the list of dictionaries into a dictionary with ID as key and Name as value
    DISTRIBUTION_CENTERS.DISTRIBUTION_CENTERS_DICT = {
        str(item["ID"]): item["Name"] for item in distribution_centers_data
    }


def readOrders():
    orders_data = extractDataFromApi(ORDERS_API_CALL)
    for order in orders_data:
        CURRENT_ORDER.ID = order["ID"]
        CURRENT_ORDER.CREATE_DATE_UTC = order["CreatedDateUtc"]
        createItemsInOrder()
    print(DATA_TO_INSERT.DATA)


def createItemsInOrder():
    items = extractDataFromApi(ITEM_IN_ORDER)
    distribution_centers_id = extractDataFromApi(FULFILLMENTS)
    for i in range(len(items)):
        try:
            distribution_centers_id[i]["DistributionCenterID"]
            distribution_centers_index = i
        except IndexError:
            distribution_centers_index = 0
            continue
        DATA_TO_INSERT.DATA.append(
            Item(
                ID=items[i]["ID"],
                CREATE_DATE_UTC=CURRENT_ORDER.CREATE_DATE_UTC,
                SKU=items[i]["Sku"],
                TITLE=items[i]["Title"],
                QUANTITY=items[i]["Quantity"],
                UNIT_PRICE=items[i]["UnitPrice"],
                TAX_PRICE=items[i]["TaxPrice"],
                SHIPPING_PRICE=items[i]["ShippingPrice"],
                SHIPPING_TAX_PRICE=items[i]["ShippingTaxPrice"],
                DISTRIBUTION_CENTER=getDistributionCenterName(
                    distribution_centers_id[distribution_centers_index][
                        "DistributionCenterID"
                    ]
                ),
                ORDER_ID=CURRENT_ORDER.ID,
            ).__dict__
        )


def extractData():
    getDistributionCenters()
    readOrders()
