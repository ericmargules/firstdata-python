from base_model import BaseModel

class AuthResultApplePay(BaseModel):

	ATTR = [
		'onlinePaymentCryptogram',
		'eciIndicator'
	]

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)
