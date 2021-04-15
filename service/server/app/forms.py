from django import forms

class UploadForm(forms.Form):
    name = forms.CharField(required=False)
    image = forms.ImageField(required=False)