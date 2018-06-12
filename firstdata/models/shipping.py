from base_model import BaseModel
from contact import Contact
from address import Address

class Shipping(BaseModel):

	ATTR = [
		'name',
	]

	OBJ_ATTR = {
		'contact' : Contact,
		'address' : Address
	}

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)