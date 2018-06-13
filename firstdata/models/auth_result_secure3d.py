from base_model import BaseModel

class AuthResultSecure3d(BaseModel):

	ATTR = [
		'type',
		'verification_response',
		'payer_authentication_response',
		'authentication_value',
		'xid'
	]

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)
