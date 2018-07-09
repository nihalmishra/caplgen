from django.shortcuts import render, redirect
#import openpyxl
# Create your views here.
def index(request):
    return render(request,'dzip.html',{})

# def upload(request):
#     if "GET" == request.method:
#         return render(request,'dzip.html',{})
#     else:
#         excel_file = request.FILES["excel_file"]
#         wb = openpyxl.load_workbook(excel_file)
#         wb.save("media/userdata.xlsx")
#     return redirect('dzip:index')