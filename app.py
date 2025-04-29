import requests
import base64
from config import (
    APIConfig,
    AccessToken,
    DistributionCenters,
    DateParams,
    Orders,
    Fulfilments,
    ItemInOrder,
    Item,
    DataToInsert,
)


config = APIConfig()
access_token = AccessToken()
distribution_centers = DistributionCenters()
date_params = DateParams()
orders = Orders()
fulfilments = Fulfilments()
item_in_order = ItemInOrder()
item = Item()
data_to_insert = DataToInsert()


def refreshAccessToken():
    """Exchanges the refresh token for a new access token."""
    auth_header = base64.b64encode(
        f"{config.CLIENT_ID}:{config.CLIENT_SECRET}".encode()
    ).decode()
    headers = {
        "Authorization": f"Basic {auth_header}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {"grant_type": "refresh_token", "refresh_token": config.REFRESH_TOKEN}
    try:
        response = requests.post(config.TOKEN_ENDPOINT, headers=headers, data=data)
        response.raise_for_status()
        token_data = response.json()
        return (
            token_data.get("access_token"),
            token_data.get("expires_in"),
        )
    except requests.exceptions.RequestException as e:
        print(f"Error refreshing access token: {e}")
        if response is not None:
            print(f"Response status code: {response.status_code}")
            print(f"Response body: {response.text}")
        return None, None, None


def requestApi(endpoint=None, filter_params=None):
    """Reads orders from the ChannelAdvisor API."""
    headers = {"Authorization": f"Bearer {access_token.ACCESS_TOKEN}"}
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


def extractData(request, items):
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


def readDistributionCenters():
    distribution_centers_data = extractData(
        requestApi(distribution_centers.ENDPOINT), distribution_centers.KEYS
    )
    # Transform the list of dictionaries into a dictionary with ID as key and Name as value
    distribution_centers.DISTRIBUTION_CENTERS_DICT = {
        str(item["ID"]): item["Name"] for item in distribution_centers_data
    }


def readOrders():
    orders_data = extractData(
        requestApi(orders.ENDPOINT, date_params.PARAMS), orders.KEYS
    )
    # for order in orders_data:
    #     distribution_centers_id = extractData(
    #         requestApi(fulfilments.ENDPOINT.format(order_id=order["ID"])),
    #         fulfilments.KEYS,
    #     )
    print(orders_data)
    print(len(orders_data))


if __name__ == "__main__":
    print("Requesting a new access token using the refresh token...")
    access_token.ACCESS_TOKEN, access_token.EXPIRES_IN = refreshAccessToken()

    if access_token.ACCESS_TOKEN:
        print("\nNew Access Token Obtained")
        print(f"Access Token: {access_token.ACCESS_TOKEN}")
        if access_token.EXPIRES_IN:
            print(f"Expires in: {access_token.EXPIRES_IN} seconds")
        if access_token.ACCESS_TOKEN:
            print(
                f"New Refresh Token (may have been updated): {access_token.ACCESS_TOKEN}"
            )
            # You MUST save the new refresh token!
        print("\nAccess token refreshed successfully!")
        print("\nReading orders...")
        readDistributionCenters()
        readOrders()

    else:
        print(
            "Failed to renew the access token. It may be necessary to reauthorize the application."
        )
