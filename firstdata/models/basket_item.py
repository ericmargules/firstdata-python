from base_model import BaseModel
from amount import Amount
from split_shipment import SplitShipment

class BasketItem(BaseModel):

	ATTR = [
		'id',
		'description',
		'count'
	]

	OBJ_ATTR = {
		'unitPrice' : Amount,
	}

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)
