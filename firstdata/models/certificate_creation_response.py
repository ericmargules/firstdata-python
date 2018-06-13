from base_model import BaseModel

class CertificateCreationResponse(BaseModel):

	ATTR = [
		'client_request_id',
		'api_trace_id',
		'certificate'
	]

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)