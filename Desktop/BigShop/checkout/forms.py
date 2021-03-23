from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import BillingAddress

# Address Form
class BillingForm(ModelForm):

	class Meta:
		model = BillingAddress
		fields = ['address', 'zipcode', 'city', 'landmark']
		labels = {
			'address': _('Pays'),
			'zipcode': _('Code postal'),
   			'city': _('Ville'),
  			'landmark': _('Villa'),
		}
