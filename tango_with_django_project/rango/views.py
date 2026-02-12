from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    # I'm 99% sure it doesn't want me to copy down the comments as well since that would be
    # borderline Sisyphean
    context_dict = {'boldmessage' : 'Crunchy, creamy, cookie, candy, cupcake!'}
    # interesting message there rango mate

    return render(request, 'rango/index.html', context=context_dict)

def about(request):

   
    context_dict = {'boldmessage' : 'This tutorial has been put together by David.'}
    return render(request, 'rango/about.html', context=context_dict)
    