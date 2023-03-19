from django.shortcuts import render, redirect
from .forms import FileUpload
from .models import UploadFiles


def upload_file(request):
    files = None
    if request.method == "POST":
        form = FileUpload(request.POST, request.FILES)
        files = request.FILES.getlist('files')
        if form.is_valid():
            for f in files:
                file_instance = UploadFiles(files=f)
                file_instance.save()
    else:
        form = FileUpload()

    if files:
        files = [f'/media/upload_files/{el}' for el in files]

    return render(request, 'upload_file.html', {'form': form, 'files': files})
