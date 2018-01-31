from django import forms


class EURForm(forms.Form):
    euro_value = forms.DecimalField(label='EUR value to convert to BTC')