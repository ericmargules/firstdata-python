from base_model import BaseModel
from billing import Billing
from shipping import Shipping

class Order(BaseModel):

	ATTR = [
		'order_id'
	]

	OBJ_ATTR = {
		'billing' : Billing,
		'shipping' : Shipping
	}

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)