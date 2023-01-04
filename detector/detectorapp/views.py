from django.shortcuts import render

def home(request):
        context={}
        return render(request, 'detectorapp/home.html', context)