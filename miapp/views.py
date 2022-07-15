from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
# MVC =Modelo Vista Controlador -> Acciones(metodos)
# MVT =Modelo Vista Template -> Acciones (metodos)

layout = """
<h1>Bienvenidos a la pagina de inicio </h1>
<hr>
<ul>
    <li>
     <a href="/inicio">Inicio</a>
    </li>
    <li>
     <a href="/hola-django">Hola Django/</a>
    </li>
    <li>
     <a href="/pagina-pruebas">Pagina de pruebas/</a>
    </li>
    <li>
     <a href="/contacto">Contacto/</a>
    </li>
</ul>  
</hr>   
"""
def index(request):
    html = """ 
      <br></br>
      <h3>Años hasta el 2050</h3>
      <ul>
    """

    year = 2022
    while year <= 2060:

        if year % 2 == 0:

          html += f"<li>{str(year)}</li>"

        year += 1

    html += "</ul>"

    nombre = 'Oscar Alejandro Meza Avendaño'
    lenguajes = ['Javascript', 'Python', 'PHP', 'C', 'Java']

    return render(request,'index.html', {
        'title' : "Inicio",
        'mi_variable' : "Soy un dato que está a la vista",
        'nombre' : nombre,
        'lenguajes' : lenguajes
    })

def hola_django(request):
    return render(request, 'hola_Django.html')
   
def pagina(request,redirigir=0):
    if redirigir == 1:
        return redirect('contacto', nombre="Leonardo", apellidos="Espindola")
    return render(request, 'pagina.html')

def contacto(request):
    return render(request, 'contacto.html')