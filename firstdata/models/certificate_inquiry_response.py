from base_model import BaseModel
from certificate import Certificate

class CertificateInquiryResponse(BaseModel):

	ATTR = [
		'clientRequestId',
		'apiTraceId',
		'certificates'
	]

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)
		if hasattr(self,'certificates'):
			self.set_list_items('certificates', Certificate)