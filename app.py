from modules.extraction.createOrders import extractData
from modules.load.loadData import load_data_to_bq
from modules.email.emailSender import sendEmail
import sys, traceback


def main():
    try:
        extractData()
        load_data_to_bq()
    except:
        sendErrorEmail()


def sendErrorEmail():
    exc_type, exc_value, exc_traceback = sys.exc_info()
    error_details = traceback.format_exception(exc_type, exc_value, exc_traceback)
    error_message = "".join(error_details)
    sendEmail(
        "RITHUM ETL ERROR",
        f"Contact the administrator. Something went wrong with the code:\n\n{error_message}",
    )


if __name__ == "__main__":
    main()
