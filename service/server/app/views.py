from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from .models import ImageModel
from django.conf import settings
from app.classifier import classifier
from PIL import Image, ImageOps,ImageFilter
import random 
import os.path

def index(request):
    context ={}
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            print(request.FILES['File'])
            name = handle_uploaded_file(request.FILES['File'])
            outputfilename = "static/images/"+ name
            prediction = process_upload(name)
            emotion =prediction[0]
            prob= prediction[1]
            print("Outputfile: ",outputfilename)
            return render(request, 'result.html',{'file': outputfilename, 'emotion': emotion, 'probability': prob})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UploadFileForm()
    return render(request, 'index.html', {'form': form})

def handle_uploaded_file(f):
    context={}
    uploadfilename= os.path.abspath(os.path.dirname(__file__))+ '/static/images/'+f.name
    with open(uploadfilename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return f.name

def process_upload(f):
    print("In process upload function")
    c = classifier()
    return c.make_prediction(f)