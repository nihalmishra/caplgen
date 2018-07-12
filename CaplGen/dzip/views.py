from django.shortcuts import render, redirect
from dzip.models import UploadForm, Upload
from django.urls import reverse

def index(request):
    excel_file = UploadForm()
    return render(request,'dzip/dzip.html',
    {'form': excel_file}
    )

def generate(request):
    if request.method=="POST":
        excel_file = UploadForm(request.POST, request.FILES)
        if excel_file.is_valid():
            excel_file.save()
            return redirect(reverse('dzip:index'))
    else:
        excel_file = UploadForm()
    return render(request,'dzip/dzip.html', {'form': excel_file})
# def generate(request):
#     if "GET" == request.method:
#         return render(request,'dzip.html',{})
#     else:
#         excel_file = request.FILES["excel_file"]
#         with open('some/file/name.txt', 'wb+') as destination:
#         for chunk in excel_file.chunks():
#             destination.write(chunk)
#         # wb = openpyxl.load_workbook(excel_file)
#         # wb.save("media/userdata.xlsx")
#     return redirect('dzip:index')