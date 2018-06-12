from base_model import BaseModel

class ApplePayHeader(BaseModel):

	ATTR = [
		'applicationDataHash',
		'ephemeralPublicKey',
		'publicKeyHash',
		'transactionId'
	]

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)