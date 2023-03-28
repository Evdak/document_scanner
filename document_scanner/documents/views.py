from django.shortcuts import render, redirect

from documents.helpers import convert_image, predict
from .forms import FileUpload
from .models import ResultFiles, UploadFiles
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
            res: list[ResultFiles] = []
            for f in files:
                file_instance = UploadFiles(files=f)
                file_instance.save()
                res.append(convert_image(file_instance))

        res = [
            {
                "original": str(el.upload_file.files.url),
                "scan_png": str(el.scan_png.url),
                "scan_pdf": str(el.scan_pdf.url)
            } for el in res
        ]
        import logging
        logging.warning(res)

        return JsonResponse(
            {"result": res}
        )
    return redirect('main')


@csrf_exempt
def main(request):
    form = FileUpload()
    if request.method == "POST":
        form = FileUpload(request.POST, request.FILES)
        files = request.FILES.getlist('files')
        if form.is_valid():
            res: list[ResultFiles] = []
            for f in files:
                file_instance = UploadFiles(files=f)
                file_instance.save()
                res.append(convert_image(file_instance))
                file_instance.type = predict(file=file_instance.files.path)
                file_instance.save()
    return render(request, 'upload_file.html', {'form': form, 'files': UploadFiles.objects.all()[::-1]})
