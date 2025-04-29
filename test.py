from config import Fulfilments

fulfilments = Fulfilments()
print(fulfilments.ENDPOINT.format(order_id="12345"))
