from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import fields_for_model

class UserSignUpForm(UserCreationForm):

    class Meta:
        fields = ("username","email","password1","password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Account Handle'
        self.fields['email'].label = 'Email Address'
