from base_model import BaseModel

class AdditionalDetails(BaseModel):

	ATTR = [
		'referenceNumber',
		'comments',
		'dynamicMerchantName',
		'invoiceNumber',
		'purchaseOrderNumber',
		'recurringType'
	]

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)
