import floppyforms as forms
#from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Reset

from helper.validate import Message
from users.models import CustomUser


class SignUpForm(forms.ModelForm):
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
    )
    password_confirmation = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

        # Change Form layout
        self.helper.form_action = ''
        self.helper.form_method = 'post'
        #self.helper.html5_required = True
        # Change fields position: required go first
        self.helper.layout = Layout(
            'email', 'password', 'password_confirmation',
            'name', 'card_id', 'tel')
        self.helper.add_input(Submit('submit', 'Tao tai khoan'))
        self.helper.add_input(Reset('reset', 'Reset'))

        # Add Vietnamese validation's errors
        self.fields['email'].error_messages = Message.REQUIRED
        self.fields['name'].error_message = Message.REQUIRED
        self.fields['password'].error_message = Message.REQUIRED
        self.fields['password_confirmation'].error_message = Message.REQUIRED

    def clean(self):
        input_data = super(SignUpForm, self).clean()
        password1 = input_data['password']
        password2 = input_data['password_confirmation']

        if password1 and password2:
            # Validate password min length
            length = len(str(password1))
            if length < 6 or length > 20:
                raise forms.ValidationError(Message.PASSWORD_LENGTH_NOT_VALID)
            # Validate password confirmation
            if password1 != password2:
                raise forms.ValidationError(Message.PASSWORD_NOT_MATCH)

        return input_data

    class Meta:
        model = CustomUser
        fields = {
            'email', 'password', 'password_confirmation', 'name',
            'address', 'card_id', 'tel', 'date_of_birth'
        }
        widgets = {
            'date_of_birth': forms.DateInput(attrs={
                'class': 'datepicker',
            }),
        }
