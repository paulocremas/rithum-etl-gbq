import requests, base64
from modules.configuration.authorizationConfig import (
    API_CONFIG,
    ACCESS_TOKEN,
)
from modules.configuration.authorizationConfig import SYNCHRONIZE_CONFIG
import time

""" Controls token refreshing """


def tokenRefresher():
    while True:
        SYNCHRONIZE_CONFIG.RUNNING = True
        refreshAccessToken()
        SYNCHRONIZE_CONFIG.RUNNING = False
        time.sleep(3500)


""" 
Sends a request with a fix token (refresh_token) to get the access token
which expieres in 1 hour
"""


def refreshAccessToken():
    """Exchanges the refresh token for a new access token using the OAuth2 protocol."""

    # Encode client ID and client secret in base64 for Basic Auth
    auth_header = base64.b64encode(
        f"{API_CONFIG.CLIENT_ID}:{API_CONFIG.CLIENT_SECRET}".encode()
    ).decode()

    # Set request headers
    headers = {
        "Authorization": f"Basic {auth_header}",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    # Prepare the request body with the grant type and refresh token
    data = {"grant_type": "refresh_token", "refresh_token": API_CONFIG.REFRESH_TOKEN}

    # Make the POST request to the OAuth2 token endpoint
    response = requests.post(API_CONFIG.ENDPOINT, headers=headers, data=data)
    response.raise_for_status()  # Raise an exception for non-2xx status codes

    # Parse JSON response and update the ACCESS_TOKEN variables
    token_data = response.json()
    ACCESS_TOKEN.ACCESS_TOKEN = token_data.get("access_token")
    ACCESS_TOKEN.EXPIRES_IN = token_data.get("expires_in")
