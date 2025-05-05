from modules.configuration.config import BigQueryConfig, DATA_TO_INSERT


def load_data_to_bq():
    BIGQUERY_CONFIG = BigQueryConfig()

    job = BIGQUERY_CONFIG.CLIENT.load_table_from_dataframe(
        DATA_TO_INSERT.DATA, BIGQUERY_CONFIG.TABLE_ID
    )
    job.result()
    print("Loaded DataFrame into BigQuery table.")
