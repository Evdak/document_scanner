from django.shortcuts import render, redirect
from .forms import FileUpload
from .models import UploadFiles
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
import logging


@csrf_exempt
def upload_file(request):
    files = None
    if request.method == "POST":
        form = FileUpload(request.POST, request.FILES)
        files = request.FILES.getlist('files')
        if form.is_valid():
            for f in files:
                file_instance = UploadFiles(files=f)
                file_instance.save()

        return JsonResponse(
            {
                'urls': [f'/media/upload_files/{el}' for el in files]
            }
        )
    return redirect('main')


@csrf_exempt
def main(request):
    form = FileUpload()
    if request.method == "POST":
        form = FileUpload(request.POST, request.FILES)
        files = request.FILES.getlist('files')
        if form.is_valid():
            for f in files:
                file_instance = UploadFiles(files=f)
                file_instance.save()

    return render(request, 'upload_file.html', {'form': form, 'files': UploadFiles.objects.all()})
