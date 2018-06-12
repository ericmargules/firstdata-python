from base_model import BaseModel
from payment_card import PaymentCard
from sepa_direct_debit import SepaDirectDebit
from apple_pay import ApplePay

class PaymentMethod(BaseModel):

	ATTR = [
		'type'
	]

	OBJ_ATTR = {
		'paymentCard' : PaymentCard, 
		'sepaDirectDebit' : SepaDirectDebit, 
		'applePay' : ApplePay
	}

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)