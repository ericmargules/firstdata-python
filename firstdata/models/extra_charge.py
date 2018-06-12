from base_model import BaseModel

class ExtraCharge(BaseModel):

	ATTR = [
		'chargeItem'
	]

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)