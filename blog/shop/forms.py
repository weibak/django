from django import forms


class ProductForm(forms.Form):
    title = forms.CharField(max_length=50)
    image = forms.ImageField(required=False)
    cost = forms.IntegerField()
    text = forms.CharField(max_length=500)
