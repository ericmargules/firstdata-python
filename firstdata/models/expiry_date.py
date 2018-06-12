from base_model import BaseModel

class ExpiryDate(BaseModel):

	ATTR = [
		'month',
		'year'
	]

	def __init__(self, **kwargs):
		if 'expiryDate' in kwargs:
			self.filter_expiry_date(kwargs)
		self.set_attributes(kwargs)

	def filter_expiry_date(self, params):
		expiration = str(params['expiryDate'])
		if len(expiration) == 4:
			params['month'] = expiration[0:2]
			params['year'] = expiration[2:4]
		elif len(expiration) == 3:
			params['month'] = "0" + expiration[0]
			params['year'] = expiration[1:3]
		else:
			raise ValueError("Expiry date must be 3 or 4 characters long")