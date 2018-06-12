from base_model import BaseModel

class AuthenticationRedirectParams(BaseModel):

	ATTR = [
		'PaReq',
		'TermUrl',
		'MD'
	]

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)