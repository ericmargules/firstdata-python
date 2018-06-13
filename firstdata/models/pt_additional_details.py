from base_model import BaseModel

class AdditionalDetails(BaseModel):

	ATTR = [
		'reference_number',
		'comments',
		'dynamic_merchant_name',
		'invoice_number',
		'purchase_order_number',
		'recurring_type'
	]

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)
