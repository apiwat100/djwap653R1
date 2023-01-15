from django.shortcuts import render,HttpResponse

# Create your views here.
def Home(request):
    return render(request,'Home.html')

def test(request):
    return HttpResponse("<H1>Hello world <br> This is My World  Wide web </H1>")

def firstweb(request):
    return render(request, 'firstweb.html')

def secondpage(request):
    return render(request, 'secondpage.html')

def thirdpage(request):
    return  render(request, 'thirdpage.html')

def HNY(request):
    return  render(request, 'HNY.html')