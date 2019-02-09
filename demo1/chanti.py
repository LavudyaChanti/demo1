from  django.http import HttpResponse
def wish(request):
    return HttpResponse("<h1 style='color:blue'>Welcome</h1>")
def wish1(request):
    return HttpResponse("<h1 style='color:green'>Good Mrng</h1>")
def wish2(request):
    return HttpResponse("<h1 style='color:red'>Good Evening</h1>")