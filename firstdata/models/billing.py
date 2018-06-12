from base_model import BaseModel
from contact import Contact
from address import Address

class Billing(BaseModel):

	ATTR = [
		'name',
		'personalNumber',
		'birthdate',
		'gender',
	]

	OBJ_ATTR = {
		'contact' : Contact,
		'address' : Address
	}

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)