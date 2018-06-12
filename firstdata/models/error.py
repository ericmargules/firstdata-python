from base_model import BaseModel
from error_details import ErrorDetails

class ResponseError(BaseModel):

	ATTR = [
		'code',
		'message'
	]

	OBJ_ATTR = {
		'details' : ErrorDetails 
	}

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)
		if hasattr(self, 'details'):
			set_list_items('details', ErrorDetails)