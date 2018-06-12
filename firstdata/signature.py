import base64
import uuid
import time
import hashlib
import hmac

class Signature:
	
	nonce = str(uuid.uuid4())
	timestamp = str(int(round(time.time()*1000)))

	def __init__(self, **kwargs):
		self.api_key = kwargs['api_key']
		self.api_secret = kwargs['api_secret']

	def sign(self, payload=None):
		data = self.api_key + self.nonce + self.timestamp
		if payload:
			data += payload.to_json()
		h = hmac.new(self.api_secret, data, hashlib.sha256).hexdigest()
		return base64.b64encode(h)