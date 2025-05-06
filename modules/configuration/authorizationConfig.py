import os


# This config works for refreshAccessToken.py and extractDataFromApi.py


class synchronizeConfig:
    def __init__(self):
        self.RUNNING = False


SYNCHRONIZE_CONFIG = synchronizeConfig()


class APIConfig:
    def __init__(self):
        self.CLIENT_ID = os.environ.get("APPLICATION_ID")
        self.CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
        self.REFRESH_TOKEN = os.environ.get("REFRESH_TOKEN")
        self.ENDPOINT = "https://api.channeladvisor.com/oauth2/token"


API_CONFIG = APIConfig()


class AccessToken:
    def __init__(self):
        self.ACCESS_TOKEN = None
        self.EXPIRES_IN = None


ACCESS_TOKEN = AccessToken()


# Used only on firstAuth.py
class EndpointsFirstAuth:
    def __init__(self):
        self.ENDPOINT = "https://api.channeladvisor.com/oauth2/authorize"
        self.REDIRECT_URI = ""
