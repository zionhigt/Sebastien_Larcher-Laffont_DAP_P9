from django import forms
from attachments.models import ImageProfil

class ImageProfilForm(forms.ModelForm):
    class Meta:
        model = ImageProfil
        fields = ['image']