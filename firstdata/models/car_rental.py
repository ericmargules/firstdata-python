from base_model import BaseModel
from extra_charge import ExtraCharge

class CarRental(BaseModel):

	ATTR = [
		'agreementNumber',
		'renterName',
		'returnCity',
		'returnDate',
		'pickupDate',
		'rentalClassId',
		'extraCharges',
		'noShowIndicator'
	]

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)
		if hasattr(self, 'extraCharges'):
			set_list_items('extraCharges', ExtraCharge)