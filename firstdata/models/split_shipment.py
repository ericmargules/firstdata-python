from base_model import BaseModel

class SplitShipment(BaseModel):

	ATTR = [
		'total_count',
		'final_shipment',
	]

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)