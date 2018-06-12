from base_model import BaseModel
from auth_result_apple_pay import AuthResultApplePay as ApplePay
from auth_result_secure3d import AuthResultSecure3d as Secure3d


class AuthenticationResult(BaseModel):

	OBJ_ATTR = {
		'applePay' : ApplePay,
		'secure3d' : Secure3d
	}

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)
