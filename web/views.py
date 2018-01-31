"""
User interface views.
"""
from django.template.response import TemplateResponse
from django.views.generic import FormView, ListView

from web.forms import EURForm
from web.models import Conversion
from web.service import make_eur_to_btc_conversion


class UserEntry(FormView):
    """
    GET: Diplay user form.
    POST: Process form and store conversion into a database.
    """
    form_class = EURForm
    template_name = 'index.html'

    def form_valid(self, form):
        """
        Validates form.
        """
        eur_value = form.cleaned_data['euro_value']
        request_ip = self.request.META.get('HOST', '0.0.0.0')

        try:
            # fetch exchange rate and calculate conversion
            btc_value, btc_price = make_eur_to_btc_conversion(eur_value=eur_value)

            # create a conversion log
            Conversion.objects.create(eur_amount=eur_value, conversion_rate=btc_price, request_ip=request_ip)

        except Exception as exc:
            print(str(exc))
            return TemplateResponse(request=self.request, template='result.html')

        else:
            return TemplateResponse(
                request=self.request,
                template='result.html',
                context={'btc_value': btc_value, 'eur_value': eur_value, 'btc_price': btc_price})


class LogEntryList(ListView):
    """
    GET: Display a list from Conversion table.
    """
    model = Conversion
    template_name = 'conversion_list.html'
