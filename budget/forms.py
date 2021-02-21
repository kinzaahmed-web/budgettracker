from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from bootstrap_datepicker_plus import DatePickerInput
 
""" The purpose of the forms.py class is to make it easier to get input from the user, validate
data, render html and retrieve values by the user. This represents all of the 'inputs' of the application"""

# Form for the User to add a new expense to their budget 
class ExpenseForm(forms.Form):
    title = forms.CharField()
    amount = forms.IntegerField()
    category = forms.CharField()
    date = forms.DateField(
         widget=DatePickerInput(format='%m/%d/%Y')
     )

# Form for the User to add a new budget project 
class AddForm(forms.Form):
    name = forms.CharField()
    budget = forms.IntegerField()
    category = forms.CharField()


# Form to create a new user 
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']