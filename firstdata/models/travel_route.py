from base_model import BaseModel

class TravelRoute(BaseModel):

	ATTR = [
		'departureDate',
		'origin',
		'destination',
		'carrierCode',
		'serviceClass',
		'stopoverType',
		'fareBasisCode',
		'departureTax',
		'flightNumber'
	]

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)