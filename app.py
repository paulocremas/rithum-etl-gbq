from modules.extraction.createOrders import extractData, DATA_TO_INSERT
from modules.load.loadData import load_data_to_bq
from modules.email.emailSender import sendEmail
import sys, traceback, logging

logging.basicConfig(
    filename="data_insertion.log",  # Nome do arquivo de log
    level=logging.INFO,  # Nível mínimo de log a ser capturado (INFO e superiores)
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def main():
    try:
        extractData()
        load_data_to_bq()
        logging.info(f"{len(DATA_TO_INSERT.DATA)} items inserted")
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
