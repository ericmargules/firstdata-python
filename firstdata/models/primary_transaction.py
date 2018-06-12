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
		'transactionType',
		'storeId',
		'clientTransactionId',
		'basketItems'
	]

	OBJ_ATTR = {
		'amount' : Amount,
		'paymentMethod' : PaymentMethod,
		'order' : Order,
		'splitShipment' : SplitShipment,
		'additionalDetails' : AdditionalDetails,
		'industrySpecificExtensions' : IndustrySpecificExtensions
	}

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)
		if hasattr(self, 'basketItems'):
			self.set_list_items('basketItems', BasketItem)