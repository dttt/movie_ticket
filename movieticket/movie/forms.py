# -*- coding: utf-8 -*-

import floppyforms as forms
#from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Reset


class SearchForm(forms.Form):
    movie_name = forms.CharField(max_lenth=100)
