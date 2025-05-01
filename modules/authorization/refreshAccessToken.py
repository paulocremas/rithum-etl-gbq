import requests, base64
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config import (
    API_CONFIG,
    ACCESS_TOKEN,
)


def refreshAccessToken():
    """Exchanges the refresh token for a new access token."""
    auth_header = base64.b64encode(
        f"{API_CONFIG.CLIENT_ID}:{API_CONFIG.CLIENT_SECRET}".encode()
    ).decode()
    headers = {
        "Authorization": f"Basic {auth_header}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {"grant_type": "refresh_token", "refresh_token": API_CONFIG.REFRESH_TOKEN}
    try:
        response = requests.post(API_CONFIG.ENDPOINT, headers=headers, data=data)
        response.raise_for_status()
        token_data = response.json()
        ACCESS_TOKEN.ACCESS_TOKEN = token_data.get("access_token")
        ACCESS_TOKEN.EXPIRES_IN = token_data.get("expires_in")
    except requests.exceptions.RequestException as e:
        print(f"Error refreshing access token: {e}")
        if response is not None:
            print(f"Response status code: {response.status_code}")
            print(f"Response body: {response.text}")
