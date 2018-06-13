from base_model import BaseModel

class SepaMandate(BaseModel):

	ATTR = [
		'reference',
		'url',
		'signature_date',
		'type'
	]

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)
