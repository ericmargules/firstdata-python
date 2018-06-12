from base_model import BaseModel
from avs_response import AvsResponse
from amount import Amount
from authentication_redirect import AuthenticationRedirect
from error import ResponseError

class TransactionResponse(BaseModel):

	ATTR = [
		'clientRequestId',
		'apiTraceId',
		'ipgTransactionId',
		'orderId',
		'transactionType',
		'authorizationCode',
		'securityCodeResponse',
		'brand',
		'country',
		'terminalId',
		'clientTransactionId',
		'transactionTime',
		'transactionStatus'
	]

	OBJ_ATTR = {
		'avsResponse' : AvsResponse,
		'approvedAmount' : Amount,
		'authenticationRedirect' : AuthenticationRedirect,
		'error' : ResponseError
	}

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)
