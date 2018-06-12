from base_model import BaseModel

class AuthenticationRequest(BaseModel):

	ATTR = [
		'type'
	]

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)