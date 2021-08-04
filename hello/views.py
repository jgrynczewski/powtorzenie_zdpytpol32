from django.shortcuts import render


# Create your views here.
def hello(request):
    return render(
        request,
        'hello/hello.html'
    )


def home(request):
    return render(
        request,
        'hello/home.html'
    )