from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Bienvenido a mi aplicacion web")


def despedida(request):
    return HttpResponse("Gracias por tu visita")
