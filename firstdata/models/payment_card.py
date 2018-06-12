from base_model import BaseModel
from expiry_date import ExpiryDate
from authentication_request import AuthenticationRequest
from authentication_result import AuthenticationResult

class PaymentCard(BaseModel):

	ATTR = [
		'number',
		'securityCode',
		'cardFunction',
		'cardholderName',
		'brand',
		'wallet_provider_id',
		'enableTokenization'
	]

	OBJ_ATTR = {
		'expiryDate' : ExpiryDate,
		'authenticationRequest' : AuthenticationRequest,
		'authenticationResult' : AuthenticationResult
	}

	def __init__(self, **kwargs):
		if 'expiryDate' in kwargs :
			kwargs['expiryDate'] = self.format_expiration(kwargs['expiryDate'])
			print kwargs['expiryDate'].month
		self.set_attributes(kwargs)

	def format_expiration(self, exp):
		if isinstance(exp, str) or isinstance(exp, int):
			return ExpiryDate(expiryDate=exp)
		else:
			return exp