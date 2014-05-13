from django.shortcuts import render


def about(request):
    return render(request, 'about.html')


def contract(request):
    return render(request, 'contract.html')
