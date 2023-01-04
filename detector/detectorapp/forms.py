from django import forms
class URLForm(forms.Form):
   name = forms.CharField(max_length=100)