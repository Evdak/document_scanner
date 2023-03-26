from django.contrib import admin
from . import models


@admin.register(models.UploadFiles)
class UploadFilesAdmin(admin.ModelAdmin):
    list_display = (
        'files',
    )

    list_filter = list_display


@admin.register(models.ResultFiles)
class ResultFilesAdmin(admin.ModelAdmin):
    list_display = (
        'upload_file',
        'scan_png',
        'scan_pdf',
    )

    list_filter = list_display
