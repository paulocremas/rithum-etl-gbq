from modules.authorization.refreshAccessToken import tokenRefresher
from modules.extraction.createOrders import extractData
from modules.load.loadData import load_data_to_bq
from modules.configuration.authorizationConfig import SYNCHRONIZE_CONFIG
from modules.email.emailSender import sendEmail
import threading, sys


def main():
    try:
        """
        Start a separate thread to refresh the access token
        in the background (every 3500s). This token aways expires in 1 hour.
        """
        thread = threading.Thread(target=tokenRefresher, daemon=True)
        thread.start()

        """
        Checks if the code is refreshing the token. Then, runs ETL process.
        """
        while True:
            if not SYNCHRONIZE_CONFIG.RUNNING:
                extractData()
                load_data_to_bq()
                sys.exit(0)
    except Exception as e:
        sendEmail(
            "RITHUM ETL ERROR",
            f"Something went wrong with the code: {str(e)}. Contact the administrator.",
        )
        sys.exit(0)


if __name__ == "__main__":
    main()
