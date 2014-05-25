import datetime

import floppyforms as forms
#from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class SearchForm(forms.Form):
    movie = forms.CharField(max_length=100)
    theater = forms.CharField(max_length=100)
    date = forms.DateField(initial=datetime.date.today)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        # Change Form layout
        self.helper.form_method = 'get'
        self.helper.html5_required = True
        self.helper.add_input(Submit('submit', 'Search'))

    class Meta:
        widgets = {
            'date': forms.DateInput(attrs={
                'class': 'datepicker',
            }),
        }
