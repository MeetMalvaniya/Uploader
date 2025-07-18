from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .models import UploadedFile

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('uploaded_files')
            except Exception as e:
                return render(request, 'upload.html', {'form': form, 'error': str(e)})
    else:
        form = FileUploadForm()
    return render(request, 'upload.html', {'form': form})

def uploaded_files(request):
    files = UploadedFile.objects.order_by('-uploaded_at')
    return render(request, 'files.html', {'files': files})
