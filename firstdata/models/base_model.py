import json

class BaseModel:

	def set_attributes(self, kwargs):
		if hasattr(self, 'ATTR'):
			for attr in self.ATTR:
				if attr in kwargs and kwargs[attr] is not None:
					setattr(self, attr, kwargs[attr])

		if hasattr(self, 'OBJ_ATTR'):
			for var_name, class_name in self.OBJ_ATTR.items():
				if var_name in kwargs and kwargs[var_name] is not None:
					setattr(self, var_name, self.obj_or_dict(kwargs[var_name], class_name))

	def obj_or_dict(self, params, obj):
		if isinstance(params, dict):
			return obj(**params)
		elif isinstance(params, obj):
			return params
		else:
			raise ValueError("{0} requires {1} object or dictionary".format(str(self), str(obj)))

	def to_json(self):
		return json.dumps(self.to_dict())

	def to_dict(self):
		self_dict = {}
		for var, val in self.__dict__.items():
			value = None
			if hasattr(val, 'to_dict'):
				value = val.to_dict()
			elif isinstance(val, list):
				values = map(lambda x: x.to_dict(), val)
			else:
				value = str(val)
			self_dict[var] = value
		return self_dict

	def set_list_items(self, attr_name, obj):
		items = []
		for item in getattr(self, attr_name):
			items.append(obj(**item))
		setattr(self, attr_name, items)