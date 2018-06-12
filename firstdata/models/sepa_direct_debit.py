from base_model import BaseModel
from sepa_mandate import SepaMandate

class SepaDirectDebit(BaseModel):

	ATTR = [
		'iban',
		'name',
		'country',
		'email'
	]

	OBJ_ATTR = {
		'mandate' : SepaMandate
	}

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)
