from base_model import BaseModel
from extra_charge import ExtraCharge

class Lodging(BaseModel):

	ATTR = [
		'arrival_date',
		'departure_date',
		'folio_number',
		'extra_charges',
		'no_show_indicator'
	]

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)
		if hasattr(self, 'extra_charges'):
			set_list_items('extra_charges', ExtraCharge)