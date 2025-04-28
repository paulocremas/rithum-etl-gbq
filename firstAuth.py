from urllib.parse import urlencode
from config import APIConfig, EndpointsFirstAuth
import webbrowser

config = APIConfig()
endpoints = EndpointsFirstAuth()
SCOPES = "orders inventory"


def get_authorization_url():
    """Constructs the authorization URL."""
    params = {
        "client_id": config.CLIENT_ID,
        "response_type": "code",
        "access_type": "offline",
        "scope": SCOPES,
        "redirect_uri": endpoints.REDIRECT_URI,
    }
    auth_url = f"{endpoints.AUTHORIZE_ENDPOINT}?{urlencode(params)}"
    return auth_url


def open_browser_for_authorization(authorization_url):
    """Opens the user's browser to the authorization URL."""
    print(f"Opening your browser to authorize the application: {authorization_url}")
    webbrowser.open(authorization_url)


if __name__ == "__main__":
    # Step 1: Register your application (described in the document)
    print(
        "Step 1: Ensure you have registered your application and have your Client ID and Secret."
    )

    # Step 2: Redirect the user to the authorize endpoint
    authorization_url = get_authorization_url()
    print(f"\nStep 2: Redirecting user to: {authorization_url}")
    open_browser_for_authorization(authorization_url)
