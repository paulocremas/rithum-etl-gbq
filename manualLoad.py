from datetime import datetime
import pandas as pd
from modules.configuration.ordersConfig import DATA_TO_INSERT, Item
from modules.load.loadData import load_data_to_bq

df = pd.read_csv(
    "C:\\Users\\Marajauni\\Documents\\GitHub\\rithum-etl-gbq\\2024-data.csv"
)


def transform(df):
    DATA_TO_INSERT.DATA = pd.concat(
        [
            DATA_TO_INSERT.DATA,
            pd.DataFrame(
                [
                    Item(
                        ID=int(df.id),
                        CREATE_DATE=datetime.strptime(df.create_date, "%Y/%m/%d"),
                        SKU=df.sku,
                        TITLE=df.title,
                        QUANTITY=int(df.quantity),
                        UNIT_PRICE=df.unit_price,
                        TAX_PRICE=df.tax_price,
                        SHIPPING_PRICE=df.shipping_price,
                        SHIPPING_TAX_PRICE=df.shipping_tax_price,
                        DISTRIBUTION_CENTER=df.distribution_center,
                        ORDER_ID=int(df.order_id),
                    ).__dict__
                ]
            ),
        ],
        ignore_index=True,
    )


df.apply(transform, axis=1)

print(DATA_TO_INSERT.DATA)
load_data_to_bq()
