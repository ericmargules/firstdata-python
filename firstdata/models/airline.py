from base_model import BaseModel
from travel_route import TravelRoute
from ancillary_service_category import AncillaryServiceCategory

class Airline(BaseModel):

	ATTR = [
		'passengerName',
		'ticketNumber',
		'issuingCarrier',
		'carrierName',
		'travelAgencyIataCode',
		'travelAgencyName',
		'airlinePlanNumber',
		'airlineInvoiceNumber',
		'reservationSystem',
		'restricted',
		'travelRoute',
		'relatedTicketNumber',
		'ancillaryServiceCategory',
		'ticketPurchase'
	]

	def __init__(self, **kwargs):
		self.set_attributes(kwargs)
		if hasattr(self, 'travelRoute'):
			self.set_list_items('travelRoute', TravelRoute)
		if hasattr(self, 'ancillaryServiceCategory'):
			self.set_list_items('ancillaryServiceCategory', AncillaryServiceCategory)