from base_model import BaseModel

class SepaMandate(BaseModel):

	ATTR = [
		'reference',
		'url',
		'signatureDate',
		'type'
	]

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)
