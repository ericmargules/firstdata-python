from base_model import BaseModel

class SplitShipment(BaseModel):

	ATTR = [
		'totalCount',
		'finalShipment',
	]

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)