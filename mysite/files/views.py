from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings

from .forms import FileForm
from .models import File

import os
import requests


def home(request):
    return render(request, "files/home.html")


def upload(request):
    context = dict()

    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            file_name = request.FILES["csv_file"].name
            try:
                text = open(
                    os.path.join(f"{settings.MEDIA_ROOT}\\myfiles", file_name), "r"
                ).read()

                res = []
                content = [line for line in text.split("\n")]
                for line in content:
                    res.append(line.split(","))

                context["headers"] = res[0]
                context["data"] = res[1:]

                result = []
                for item in context["data"]:
                    res_json = dict()

                    for head, x in zip(context["headers"], item):
                        res_json[head] = x

                    result.append(res_json)

                r = requests.post("http://127.0.0.1:5000/file_upload", json=result[:10])
            except:
                print("fuck")

            return render(request, "files/upload.html", context)
    else:
        form = FileForm()

    context["form"] = form

    return render(request, "files/upload.html", context)
