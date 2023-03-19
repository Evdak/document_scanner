from django.contrib import admin
from . import models


@admin.register(models.UploadFiles)
class UploadFilesAdmin(admin.ModelAdmin):
    list_display = (
        'files',
    )

    list_filter = list_display
