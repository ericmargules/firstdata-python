import firstdata

class Portal:

	def __init__(self, **kwargs):
			self.config = firstdata.Config(**kwargs)

	def transaction(self):
		return firstdata.TransactionPortal(self)