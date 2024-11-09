
from django import forms

class PreRegistroForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "id": "email",
                "placeholder": "E-mail"
            }
        )
    )
