import floppyforms as forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Reset

from users.models import CustomUser


class SignUpForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password_confirmation = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

        self.helper.form_action = ''
        self.helper.form_method = 'post'

        # Change fields position: required go first
        self.helper.layout = Layout(
            'email', 'password', 'password_confirmation',
            'name', 'card_id', 'tel')

        self.helper.add_input(Submit('submit', 'Tao tai khoan'))
        self.helper.add_input(Reset('reset', 'Reset'))

    class Meta:
        model = CustomUser
        fields = {
            'email', 'password', 'password_confirmation', 'name',
            'address', 'card_id', 'tel', 'date_of_birth'
        }
        widgets = {
            'email': forms.EmailInput,
            'date_of_birth': forms.DateInput,
            'card_id': forms.NumberInput,
            'tel': forms.NumberInput,
            'name': forms.TextInput,
        }
