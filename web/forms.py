from django import forms


class EURForm(forms.Form):
    euro_value = forms.DecimalField(label='EUR value to convert to BTC', max_digits=12, decimal_places=4)
