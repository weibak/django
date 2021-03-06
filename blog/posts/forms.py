from django import forms


class PostForm(forms.Form):
    title = forms.CharField(max_length=50)
    text = forms.CharField(max_length=200)
    image = forms.ImageField(required=False)
    slug = forms.CharField(max_length=6)
