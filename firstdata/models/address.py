from base_model import BaseModel

class Address(BaseModel):

	ATTR = [
		'company',
		'address1',
		'address2',
		'locality',
		'region',
		'postal_code',
		'country'
	]

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)