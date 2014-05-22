# -*- coding: utf-8 -*-

import floppyforms as forms
#from django import forms

from helper.misc import Message
from .models import Version


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version

    def clean_end_date(self):
        begin = self.cleaned_data['begin_date']
        end = self.cleaned_data['end_date']

        if begin >= end:
            raise forms.ValidationError(Message.BEGIN_DATE_END_DATE_NOT_VALID)

        return end
