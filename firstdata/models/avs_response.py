from base_model import BaseModel

class AvsResponse(BaseModel):

	ATTR = [
		'streetNumberMatch',
		'postalCodeMatch'
	]

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)