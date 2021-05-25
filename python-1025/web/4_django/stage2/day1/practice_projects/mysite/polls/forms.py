from django import forms
from django.core.exceptions import ValidationError
import re


def cellphone_validator(value):
    if len(value) != 11:
        raise ValidationError('电话号码必须是11位数')
    if not value.isdigit():
        raise ValidationError('电话号码必须是纯数字')


class UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.widgets.PasswordInput)
