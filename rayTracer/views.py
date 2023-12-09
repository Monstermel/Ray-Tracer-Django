import io
import requests
from PIL import Image
from .forms import RayTracerForm
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect


def programa(request):
    if request.method == 'POST':
        form = RayTracerForm(request.POST)
        if form.is_valid():
            headers = {
                'Content-Type': 'application/json'
            }
            response = requests.post('http://localhost:5050/', json=form.cleaned_data, headers=headers)
            if response.status_code == 200:
                print('POST request successful')
                image = Image.open(io.BytesIO(response.content))
                image.save("rayTracer/static/img/result.jpg")

                duration = int(response.headers['Render-time']) / 1_000_000_000

                return render(request, 'programa.html', {'form': form,
                                                         'Time': duration,
                                                         'Image': "rayTracer/static/img/result.jpg"})
            else:
                print('POST request failed')
                print('Status Code:', response.status_code)

    else:
        form = RayTracerForm()

    form = RayTracerForm()
    return render(request, 'programa.html', {'form': form})