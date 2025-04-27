import os


class APIConfig:
    def __init__(self):
        self.CLIENT_ID = os.environ.get("APPLICATION_ID")
        self.CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
        self.REFRESH_TOKEN = os.environ.get("REFRESH_TOKEN")


class Endpoints:
    def __init__(self):
        self.TOKEN_ENDPOINT = "https://api.channeladvisor.com/oauth2/token"
        self.ORDERS_ENDPOINT = "https://api.channeladvisor.com/v1/Orders"
        self.DISTRIBUTION_CENTERS_ENDPOINT = (
            "https://api.channeladvisor.com/v1/DistributionCenters"
        )


# Used only on firstAuth.py
class EndpointsAuth:
    def __init__(self):
        self.AUTHORIZE_ENDPOINT = "https://api.channeladvisor.com/oauth2/authorize"
        self.REDIRECT_URI = ""
