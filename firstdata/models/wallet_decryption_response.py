from base_model import BaseModel
from decrypted_data import DecryptedData

class WalletDecryptionResponse(BaseModel):

	OBJ_ATTR = {
		'decryptedData' : DecryptedData
	}

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)
