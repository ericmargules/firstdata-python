from base_model import BaseModel

class CertificateCreationResponse(BaseModel):

	ATTR = [
		'clientRequestId',
		'apiTraceId',
		'certificate'
	]

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)