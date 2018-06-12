from base_model import BaseModel

class ErrorDetails(BaseModel):

	ATTR = [
		'field',
		'message'
	]

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)