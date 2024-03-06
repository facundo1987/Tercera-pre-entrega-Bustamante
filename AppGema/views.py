from django.shortcuts import render
from django.http import HttpResponse
from AppGema.models import Habitacion
from AppGema.forms import HuespedFormulario
from AppGema.models import Huesped

# Create your views here.

def inicio (request):
    
    return render(request, "AppGema/inicio.html")

def  habitacion (request):
    
    return render(request, "AppGema/habitacion.html")


def huesped (request):
    
    if request.method == "POST":
        
        info_formulario = HuespedFormulario(request.POST)
        
        if info_formulario.is_valid():
            
            info_dic = info_formulario.cleaned_data
            
            huesped_nuevo = Huesped(
                nombre=info_dic["nombre"],
                apellido= info_dic["apellido"], 
                correo=info_dic["correo"]
                )
            
            huesped_nuevo.save()
            
            return render(request, "AppGema/inicio.html")
    
    else:
        
        formulario = HuespedFormulario()
            
    
    return render(request, "AppGema/huesped.html", {"formu":formulario})


def reserva (request):
    
    return render(request, "AppGema/reserva.html")



def buscar_huesped(request):
    
    
    if "nombre" in request.GET and request.GET["nombre"]:
        
        nombre = request.GET["nombre"]
        
        huespedes = Huesped.objects.filter(nombre__icontains = nombre)
        
        
        mensaje= f"buscando al huesped {nombre}"
       
    
        return render(request, "AppGema/resultado_busqueda.html", {"mensaje":mensaje, "resultado":huespedes})

    
    return render(request, "AppGema/resultado_busqueda.html")
        


    

