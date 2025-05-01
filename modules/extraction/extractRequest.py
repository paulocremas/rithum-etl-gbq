import requests
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config import ACCESS_TOKEN


def requestApi(endpoint=None, filter_params=None):
    """Reads orders from the ChannelAdvisor API."""
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN.ACCESS_TOKEN}"}
    params = filter_params if filter_params else {}
    try:
        response = requests.get(endpoint, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error reading orders: {e}")
        if response is not None:
            print(f"Response status code: {response.status_code}")
            print(f"Response body: {response.text}")
        return None


def extractDataFromRequest(request, items):
    isProcessing = True
    processed_data = []
    while isProcessing:
        if request and "value" in request:
            for item in request["value"]:
                item = {key: item[key] for key in items}
                processed_data.append(item)
            if "@odata.nextLink" not in request:
                isProcessing = False
            else:
                request = requestApi(request["@odata.nextLink"])
        else:
            isProcessing = False
    return processed_data


# FIX THIS FIRST THING
def extractDataFromApi(configObject):
    print(configObject)
    print(type(configObject))
    extracted_data = requestApi(
        (
            configObject.ENDPOINT.format(order_id=configObject.ORDER_ID)
            if hasattr(configObject, "ORDER_ID")
            else configObject.ENDPOINT
        ),
        getattr(configObject, "PARAMS", None),
    )
    orders_data = extractDataFromRequest(extracted_data, configObject.KEYS)
    print(orders_data)
    return orders_data
