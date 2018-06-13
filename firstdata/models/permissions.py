from base_model import BaseModel

class Permissions(BaseModel):

	ATTR = [
		'auth_type',
		'auth_id'		
	]

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)