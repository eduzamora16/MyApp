from django.http import HttpResponse
import datetime
from django.template import Template,Context

def saludo(request):
     documento="""<html>
     <body>
     <h1>
     Bienvenidos a mi aplicacion desde html (Ubuntu)
     </h1>
     </body>
     </html>"""
     return HttpResponse(documento)

def nuevosaludo(request):
    doc_externo= open("/home/eduzam16/ProyectoPython/Proyecto1/Proyecto1/plantillas/miplantilla.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)



def despedida(request):
    return HttpResponse("Gracias por tu visita")

def fecha(request):
    fecha_actual = datetime.datetime.now()
    documento="""<html>
    <body>
    <h1>
    Fecha y Hora Actual %s
    </h1>
    </body>
    </html>""" % fecha_actual
    return HttpResponse(documento)
