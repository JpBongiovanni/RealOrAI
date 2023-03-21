from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from PIL import Image, ExifTags
from io import BytesIO
import textwrap
import PIL.Image
import PIL.ExifTags as ExifTags
from django.http import HttpResponse
import requests
import json
import base64
from decimal import Decimal

def image_form(request):
    return render(request, 'image_form.html', {})

def image_metadata(request):
    if request.method == 'POST':
        image_url = request.POST.get('image_url')
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))
        metadata = image._getexif()
        image_base64 = base64.b64encode(response.content).decode('utf-8')
        wrapped_base64 = textwrap.wrap(image_base64, width=76)
        final_base64 = "\n".join(wrapped_base64)
        if metadata:
            exif_data = {}
            for tag, value in metadata.items():
                decoded = ExifTags.TAGS.get(tag, tag)
                exif_data[decoded] = value
            return HttpResponse(str(exif_data) + " " + final_base64)
        else:
            return HttpResponse("No metadata found for the given image.")
    else:
        return render(request, 'image_form.html')