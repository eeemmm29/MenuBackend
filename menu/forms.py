from django import forms
from .models import MenuItem
import cloudinary.uploader


class MenuItemAdminForm(forms.ModelForm):
    image = forms.ImageField(
        required=False,
        help_text="Upload an image file. Will be uploaded to Cloudinary.",
    )

    class Meta:
        model = MenuItem
        fields = "__all__"

    def save(self, commit=True):
        image = self.cleaned_data.get("image")
        if image:
            result = cloudinary.uploader.upload(image)
            self.instance.image_url = result.get("secure_url")
        return super().save(commit=commit)
