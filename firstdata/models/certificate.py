from base_model import BaseModel

class Certificate(BaseModel):

	ATTR = [
		'certificate',
		'appLabel',
		'walletProvider',
		'status',
	]

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)