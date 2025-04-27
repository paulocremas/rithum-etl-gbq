import requests
import base64
from config import APIConfig, Endpoints

config = APIConfig()
endpoints = Endpoints()


def refresh_access_token(refresh_token):
    """Exchanges the refresh token for a new access token."""
    auth_header = base64.b64encode(
        f"{config.CLIENT_ID}:{config.CLIENT_SECRET}".encode()
    ).decode()
    headers = {
        "Authorization": f"Basic {auth_header}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {"grant_type": "refresh_token", "refresh_token": refresh_token}
    try:
        response = requests.post(endpoints.TOKEN_ENDPOINT, headers=headers, data=data)
        response.raise_for_status()
        token_data = response.json()
        return (
            token_data.get("access_token"),
            token_data.get("expires_in"),
            token_data.get("refresh_token"),
        )
    except requests.exceptions.RequestException as e:
        print(f"Error refreshing access token: {e}")
        if response is not None:
            print(f"Response status code: {response.status_code}")
            print(f"Response body: {response.text}")
        return None, None, None


def read_orders(access_token, endpoint=None, filter_params=None):
    """Reads orders from the ChannelAdvisor API."""
    headers = {"Authorization": f"Bearer {access_token}"}
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


def read_orders_handler():
    """Handles the process of reading and displaying order data."""
    order_counter = 0
    orders_data = read_orders(new_access_token, endpoints.ORDERS_ENDPOINT)
    next_link_orders = True

    if orders_data and "value" in orders_data and orders_data["value"]:
        print("\nOrders Data:")
        while next_link_orders:
            if orders_data and "value" in orders_data:
                order_counter += len(orders_data["value"])
                print(len(orders_data["value"]))
                if "@odata.nextLink" not in orders_data:
                    next_link_orders = False
            else:
                next_link_orders = False
            orders_data = read_orders(new_access_token, orders_data["@odata.nextLink"])
    else:
        print("\nFailed to read orders.")
    print(f"Total orders: {order_counter}")


if __name__ == "__main__":
    print("Requesting a new access token using the refresh token...")
    new_access_token, new_expires_in, new_refresh_token = refresh_access_token(
        config.REFRESH_TOKEN
    )

    if new_access_token:
        print("\nNew Access Token Obtained")
        print(f"Access Token: {new_access_token}")
        if new_expires_in:
            print(f"Expires in: {new_expires_in} seconds")
        if new_refresh_token:
            print(f"New Refresh Token (may have been updated): {new_refresh_token}")
            # You MUST save the new refresh token!
        print("\nAccess token refreshed successfully!")
        print("\nReading orders...")
        read_orders_handler()

    else:
        print(
            "Failed to renew the access token. It may be necessary to reauthorize the application."
        )
