from base_model import BaseModel

class AmountComponents(BaseModel):

	ATTR = [
		'subtotal',
		'vat_amount',
		'local_tax',
		'shipping',
		'cashback',
		'tip',
		'convenience_fee'
	]

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)