from base_model import BaseModel
from airline import Airline
from lodging import Lodging
from car_rental import CarRental

class IndustrySpecificExtensions(BaseModel):

	OBJ_ATTR = {
		'airline' : Airline,
		'lodging' : Lodging,
		'carRental' : CarRental
	}

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)