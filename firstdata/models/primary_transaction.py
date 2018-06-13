from base_model import BaseModel
from amount import Amount
from payment_method import PaymentMethod
from order import Order
from split_shipment import SplitShipment
from industry_specific_extensions import IndustrySpecificExtensions
from basket_item import BasketItem
from pt_additional_details import AdditionalDetails

class PrimaryTransaction(BaseModel):

	ATTR = [
		'transaction_type',
		'store_id',
		'client_transaction_id',
		'basket_items'
	]

	OBJ_ATTR = {
		'amount' : Amount,
		'payment_method' : PaymentMethod,
		'order' : Order,
		'split_shipment' : SplitShipment,
		'additional_details' : AdditionalDetails,
		'industry_specific_extensions' : IndustrySpecificExtensions
	}

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)
		if hasattr(self, 'basket_items'):
			self.set_list_items('basket_items', BasketItem)