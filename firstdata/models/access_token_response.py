from base_model import BaseModel
from error import ResponseError

class AccessTokenResponse(BaseModel):

	ATTR = [
		'accessToken',
		'clientRequestId',
		'apiTraceId',
		'transactionStatus'
	]

	OBJ_ATTR = {
		'error' : ResponseError
	}

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)

	def valid_token(self):
		return True 