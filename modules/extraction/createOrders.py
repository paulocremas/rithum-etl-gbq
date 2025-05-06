from modules.configuration.ordersConfig import (
    DISTRIBUTION_CENTERS,
    ORDERS_API_CALL,
    ITEM_IN_ORDER,
    FULFILLMENTS,
    CURRENT_ORDER,
    DATA_TO_INSERT,
)
from modules.configuration.ordersConfig import Item
from modules.extraction.extractDataFromApi import extractDataFromApi
from modules.transform.nameDistributionCenters import getDistributionCenterName
from modules.transform.dateHandler import convertStringUtcToCst
from pandas import concat, DataFrame
import sys


def extractData():
    orders_data = extractDataFromApi(ORDERS_API_CALL)
    getDistributionCenters()

    if not orders_data:
        print("No orders to extract.")
        sys.exit(0)

    total = len(orders_data)
    current = total
    CURRENT_ORDER.CREATING_ORDER = True
    for order in orders_data:
        print(f"Orders left to process: {total}/{current}")
        CURRENT_ORDER.ID = order["ID"]
        CURRENT_ORDER.CREATE_DATE_UTC = order["CreatedDateUtc"]
        createItemsInOrder()
        current -= 1
    CURRENT_ORDER.CREATING_ORDER = False


def getDistributionCenters():
    distribution_centers_data = extractDataFromApi(DISTRIBUTION_CENTERS)
    # Transform the list of dictionaries into a dictionary with ID as key and Name as value
    DISTRIBUTION_CENTERS.DISTRIBUTION_CENTERS_DICT = {
        str(item["ID"]): item["Name"] for item in distribution_centers_data
    }


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
        DATA_TO_INSERT.DATA = concat(
            [
                DATA_TO_INSERT.DATA,
                DataFrame(
                    [
                        Item(
                            ID=items[i]["ID"],
                            CREATE_DATE=convertStringUtcToCst(
                                CURRENT_ORDER.CREATE_DATE_UTC
                            ),
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
                    ]
                ),
            ],
            ignore_index=True,
        )
