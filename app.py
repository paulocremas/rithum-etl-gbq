import requests
import base64
from config import APIConfig, AccessToken, DistributionCenters, Orders

config = APIConfig()
access_token = AccessToken()
distribution_centers = DistributionCenters()
orders = Orders()


def refresh_access_token():
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


def request_api(endpoint=None, filter_params=None):
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


def extract_data(request, items):
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
                request = request_api(request["@odata.nextLink"])
        else:
            isProcessing = False
    return processed_data


def read_distribution_centers():
    distribution_centers_data = extract_data(
        request_api(distribution_centers.ENDPOINT), distribution_centers.KEYS
    )
    # Transform the list of dictionaries into a dictionary with ID as key and Name as value
    distribution_centers.DISTRIBUTION_CENTERS_DICT = {
        str(item["ID"]): item["Name"] for item in distribution_centers_data
    }


def read_orders():
    orders_data = extract_data(request_api(orders.ENDPOINT), orders.KEYS)
    print(orders_data)
    print(len(orders_data))


if __name__ == "__main__":
    print("Requesting a new access token using the refresh token...")
    access_token.ACCESS_TOKEN, access_token.EXPIRES_IN = refresh_access_token()

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
        read_distribution_centers()
        read_orders()

    else:
        print(
            "Failed to renew the access token. It may be necessary to reauthorize the application."
        )
