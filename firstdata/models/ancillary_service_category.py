from base_model import BaseModel

class AncillaryServiceCategory(BaseModel):

	ATTR = [
		'serviceCategory'
	]

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)