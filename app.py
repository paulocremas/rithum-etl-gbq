from modules.authorization.refreshAccessToken import refreshAccessToken
from modules.extraction.createOrders import extractData
from modules.load.loadData import load_data_to_bq
from modules.configuration.config import DATA_TO_INSERT

if __name__ == "__main__":

    refreshAccessToken()
    extractData()
    print(DATA_TO_INSERT.DATA["create_date"])
    load_data_to_bq()
