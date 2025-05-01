import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config import (
    DISTRIBUTION_CENTERS,
    ORDERS_API_CALL,
    FULFILLMENTS,
    ITEM_IN_ORDER,
    DATA_TO_INSERT,
)
from modules.config import Item
from modules.extraction.extractRequest import extractDataFromApi


def readDistributionCenters():
    distribution_centers_data = extractDataFromApi(DISTRIBUTION_CENTERS)
    # Transform the list of dictionaries into a dictionary with ID as key and Name as value
    DISTRIBUTION_CENTERS.DISTRIBUTION_CENTERS_DICT = {
        str(item["ID"]): item["Name"] for item in distribution_centers_data
    }


def readOrders():
    orders_data = extractDataFromApi(ORDERS_API_CALL)
    for order in orders_data:
        createItemsInOrder(order["ID"], order["CreatedDateUtc"])


def createItemsInOrder(order_id, createDate):
    ITEM_IN_ORDER.ORDER_ID = order_id
    items = extractDataFromApi(ITEM_IN_ORDER)
    distribution_centers_id = extractDataFromApi(FULFILLMENTS)
    if len(distribution_centers_id) > 1:
        print(order_id)
    if len(items) < len(distribution_centers_id):
        print(order_id)
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
                CREATE_DATE_UTC=createDate,
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
                ORDER_ID=order_id,
            ).__dict__
        )


def getDistributionCenterName(distribution_center_id):
    """Returns the name of the distribution center based on its ID."""
    return DISTRIBUTION_CENTERS.DISTRIBUTION_CENTERS_DICT.get(
        str(distribution_center_id), "Unknown Distribution Center"
    )


def extractData():
    readDistributionCenters()
    readOrders()
