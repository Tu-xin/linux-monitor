from django import forms
 
class WebSshForm(forms.Form):
    command = forms.CharField(required=True)
