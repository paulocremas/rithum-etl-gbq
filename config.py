import os


class APIConfig:
    def __init__(self):
        self.CLIENT_ID = os.environ.get("APPLICATION_ID")
        self.CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
        self.REFRESH_TOKEN = os.environ.get("REFRESH_TOKEN")
        self.TOKEN_ENDPOINT = "https://api.channeladvisor.com/oauth2/token"


class AccessToken:
    def __init__(self):
        self.ACCESS_TOKEN = None
        self.EXPIRES_IN = None


class DistributionCenters:
    def __init__(self):
        self.ENDPOINT = "https://api.channeladvisor.com/v1/DistributionCenters"
        self.KEYS = ["ID", "Name"]
        self.DISTRIBUTION_CENTERS_DICT = None


class Orders:
    def __init__(self):
        self.ENDPOINT = "https://api.channeladvisor.com/v1/Orders"
        self.KEYS = ["ID", "CreatedDateUtc"]


# Used only on firstAuth.py
class EndpointsFirstAuth:
    def __init__(self):
        self.AUTHORIZE_ENDPOINT = "https://api.channeladvisor.com/oauth2/authorize"
        self.REDIRECT_URI = ""
