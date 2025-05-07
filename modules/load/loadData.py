from modules.configuration.ordersConfig import BigQueryConfig, DATA_TO_INSERT


def load_data_to_bq():
    if not len(DATA_TO_INSERT.DATA) == 0:
        BIGQUERY_CONFIG = BigQueryConfig()

        job = BIGQUERY_CONFIG.CLIENT.load_table_from_dataframe(
            DATA_TO_INSERT.DATA, BIGQUERY_CONFIG.TABLE_ID
        )
        job.result()
        print("Loaded DataFrame into BigQuery table.")
