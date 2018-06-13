from base_model import BaseModel
from payment_card import PaymentCard
from sepa_direct_debit import SepaDirectDebit
from apple_pay import ApplePay

class PaymentMethod(BaseModel):

	ATTR = [
		'type'
	]

	OBJ_ATTR = {
		'payment_card' : PaymentCard, 
		'sepa_direct_debit' : SepaDirectDebit, 
		'apple_pay' : ApplePay
	}

	def __init__(self, params):
		self.set_attributes(params)