from base_model import BaseModel

class Permissions(BaseModel):

	ATTR = [
		'authType',
		'authId'		
	]

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)