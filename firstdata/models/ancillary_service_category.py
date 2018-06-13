from base_model import BaseModel

class AncillaryServiceCategory(BaseModel):

	ATTR = [
		'service_category'
	]

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)