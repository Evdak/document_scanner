from django import forms
from django.forms import ClearableFileInput
from .models import UploadFiles


class FileUpload(forms.ModelForm):
    class Meta:
        model = UploadFiles
        fields = ['files']
        widgets = {
            'files': ClearableFileInput(attrs={'multiple': True}),
        }
