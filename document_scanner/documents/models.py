from django.db import models


class UploadFiles(models.Model):
    files = models.FileField(
        upload_to='upload_files/',
        blank=True,
        null=True
    )
