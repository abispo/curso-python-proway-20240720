from django.shortcuts import render

def pre_registro(request):
    return render(request, "registro/pre_registro.html")
