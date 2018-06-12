from base_model import BaseModel

class AuthResultSecure3d(BaseModel):

	ATTR = [
		'type',
		'verificationResponse',
		'payerAuthenticationResponse',
		'authenticationValue',
		'xid'
	]

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)
