from django import forms

class CreateListForm(forms.Form):
    name = forms.CharField(label="Todo Name")
    completed = forms.BooleanField(required=False)
