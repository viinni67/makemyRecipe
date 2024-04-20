from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    students=[
        {"name":"vineet",'age':21},
        {"name":"susy",'age':13},
        {"name":"kenjaru",'age':18}  
    ]
    months=[
        "jan","feb","march","dec"
    ]
    # for students in students:
    #     print(students)
    return render(request,"home/index.html",context={"students":students ,"months":months})
def test(request):
    print("#"*10)
    return HttpResponse("<h1>hello hi testing ---</h1>")