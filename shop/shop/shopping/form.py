from django import forms

class ImageUploadForm(forms.Form):
    profile_photo = forms.ImageField()