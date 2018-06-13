from base_model import BaseModel
from decrypted_data import DecryptedData

class WalletDecryptionResponse(BaseModel):

	OBJ_ATTR = {
		'decrypted_data' : DecryptedData
	}

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)
