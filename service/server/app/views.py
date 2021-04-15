from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadForm
from .models import ImageModel

def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            name = form.cleaned_data.get("name")
            img = form.cleaned_data.get("image")
            obj = ImageModel.objects.create(
                                 img = img
                                 )
            obj.save()
            return HttpResponseRedirect('/process')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UploadForm()

    return render(request, 'index.html', {'form': form})

def process_upload(request):
    pass