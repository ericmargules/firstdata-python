from base_model import BaseModel
from amount_components import AmountComponents
from currencies import CURRENCY_CODES

class Amount(BaseModel):

	ATTR = [
		'total',
		'currency'
	]

	OBJ_ATTR = {
		'components' : AmountComponents
	}

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)
		if not self.valid_currency(kwargs['currency']):
			raise ValueError("Currency designator must be ISO 4217 standard")

	def valid_currency(self, currency):
		return currency.upper() in CURRENCY_CODES