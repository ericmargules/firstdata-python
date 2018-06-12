from base_model import BaseModel
from apple_pay_header import ApplePayHeader as Header

class ApplePay(BaseModel):

	ATTR = [
		'signature',
		'data',
		'version',
		'appId'
	]

	OBJ_ATTR = {
		'header' : Header
	}

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)