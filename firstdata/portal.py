import firstdata

class Portal:

	def __init__(self, params):
			if isinstance(params, firstdata.Config):
				self.config = params
			elif isinstance(params, dict):
				self.config = firstdata.Config(**kwargs)

	def transaction(self):
		return firstdata.TransactionPortal(self)