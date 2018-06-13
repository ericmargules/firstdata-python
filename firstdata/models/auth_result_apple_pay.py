from base_model import BaseModel

class AuthResultApplePay(BaseModel):

	ATTR = [
		'online_payment_cryptogram',
		'eci_indicator'
	]

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)
