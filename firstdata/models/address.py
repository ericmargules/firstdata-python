from base_model import BaseModel

class Address(BaseModel):

	ATTR = [
		'company',
		'address1',
		'address2',
		'locality',
		'region',
		'postalCode',
		'country'
	]

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)