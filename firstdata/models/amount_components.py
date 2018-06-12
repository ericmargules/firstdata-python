from base_model import BaseModel

class AmountComponents(BaseModel):

	ATTR = [
		'subtotal',
		'vatAmount',
		'localTax',
		'shipping',
		'cashback',
		'tip',
		'convenienceFee'
	]

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)