from base_model import BaseModel
from extra_charge import ExtraCharge

class Lodging(BaseModel):

	ATTR = [
		'arrivalDate',
		'departureDate',
		'folioNumber',
		'extraCharges',
		'noShowIndicator'
	]

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)
		if hasattr(self, 'extraCharges'):
			set_list_items('extraCharges', ExtraCharge)