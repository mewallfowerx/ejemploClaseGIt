from django.shortcuts import render

# Create your views here.

def Home_Noticias(request):

    #ORM
    todas = Noticia.objects.all()

    contexto = {}

    contexto['noticias'] = todas

    return render(request, 'noticias/home_noticias.html')

#ACLARACION si bien en la lista armo un diccionario del tipo
# {noticias: todas_noticias, fecha: '28-11-23'}
# en el template recibo variables separadas, una por cada clave, la cual contiene 
# como valor el valor de la clave

# variables
# ej recibo 2 variables distintas, cuyo nombre es igual a la clave
# noticias = todas_noticias
# fecha = '28-11-23'
