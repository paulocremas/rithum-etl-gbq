from modules.authorization.refreshAccessToken import refreshAccessToken
from modules.extraction.createOrders import extractData
from modules.load.loadData import load_data_to_bq
from modules.configuration.authorizationConfig import SYNCHRONIZE_CONFIG
import time, threading, sys


def tokenRefresher():
    while True:
        SYNCHRONIZE_CONFIG.RUNNING = True
        refreshAccessToken()
        SYNCHRONIZE_CONFIG.RUNNING = False
        time.sleep(3500)


def main():
    thread = threading.Thread(target=tokenRefresher, daemon=True)
    thread.start()

    while True:
        if not SYNCHRONIZE_CONFIG.RUNNING:
            extractData()
            load_data_to_bq()
            sys.exit(0)
        else:
            time.sleep(1)


if __name__ == "__main__":
    main()
