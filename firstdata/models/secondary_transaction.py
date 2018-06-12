from base_model import BaseModel
from amount import Amount
from split_shipment import SplitShipment

class SecondaryTransaction(BaseModel):

	ATTR = [
		'storeId'
	]

	OBJ_ATTR = {
		'amount' : Amount,
		'splitShipment' : SplitShipment
	}

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)
