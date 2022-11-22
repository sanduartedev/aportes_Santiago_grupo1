from django.shortcuts import render
from django.http import HttpResponse
from turnos.forms import ContactoForm
from django.contrib import messages
#para mandar el email
from django.core.mail import send_mail
from django.conf import settings 
# para el mapa
from django.shortcuts import redirect
from .models import Search
from .forms import SearchForm
import folium
import geocoder
#Faq
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.views import generic
from django.utils import timezone
#institucional
from turnos.models import Personal
#noticias
from .models import Noticia
from .forms import NoticiaForm



# Create your views here.
    
def bienvenida(request, nombre='Visitante'):    
    return HttpResponse(f"""
        <h1>Hola {nombre}, <br> Bienvenido a la página de turnos web de Django Hospital</h1>
        <h3>Seleccionar turno</h3>
    """)

def index(request):
    return render(request, 'turnos/public/index.html')

def turnos(request):
    return render(request, 'turnos/public/turnos.html')   

def login(request):
    return render(request, 'turnos/public/login.html')

def registro(request):
    return render(request, 'turnos/public/registro.html')

def registro(request):    
    if(request.method == 'POST'):
        contacto_form = ContactoForm(request.POST)
        if (contacto_form.is_valid()):
            messages.success(request,'Hemos recibido tu consulta, en breve te responderemos.')
            messages.info(request,'Te estará llegando un email.')
        else:
            messages.warning(request,'Por favor revisa los errores del formulario.')

    else:
        contacto_form = ContactoForm()

    return render(request,'turnos/public/registro.html',
                {'contacto_form':contacto_form,                
                })

#Función para mandar mails
def libro_de_quejas(request):
    return render(request, 'turnos/public/libro_de_quejas.html')

def libro_de_quejas(request):
    if request.method=="POST":
        subject=request.POST["asunto"]
        message=request.POST["mensaje"]+ ". Mensaje enviado por " + request.POST["email"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["djangohospital.grupo1@outlook.com"]
        send_mail(subject, message, email_from, recipient_list)

        return render(request, 'turnos/public/gracias.html')
    
    return render(request, 'turnos/public/libro_de_quejas.html')

#para el mapa

def donde_estamos(request, address=Search.objects.all().last()):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/donde_estamos')
    else:
        form = SearchForm()
    #address = Search.objects.all().last()
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country
    if lat == None or lng == None:
        lat = 0
        lng = 0
        #address.delete()
        # render(request, 'turnos/public/donde_estamos.html', context)

    # Create Map Object
    m = folium.Map(location=[19, -12], zoom_start=2)

    folium.Marker([lat, lng], tooltip='Click para acercarse',
                  popup=country).add_to(m)
    # Get HTML Representation of Map Object
    m = m._repr_html_()
    context = {
        'm': m,
        'form': form,
    }
    return render(request, 'turnos/public/donde_estamos.html', context)

def donde_estamos_caba(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/donde_estamos')
    else:
        form = SearchForm()
    address = "Balcarce 50"
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country
    if lat == None or lng == None:
        lat = 0
        lng = 0
        #address.delete()
        # render(request, 'turnos/public/donde_estamos.html', context)

    # Create Map Object
    m = folium.Map(location=[19, -12], zoom_start=2)

    folium.Marker([lat, lng], tooltip='Click para acercarse',
                  popup=country).add_to(m)
    # Get HTML Representation of Map Object
    m = m._repr_html_()
    context = {
        'm': m,
        'form': form,
    }
    return render(request, 'turnos/public/donde_estamos.html', context)

def donde_estamos_washington(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/donde_estamos')
    else:
        form = SearchForm()
    address = "1600 Pennsylvania Avenue, N.W."
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country
    if lat == None or lng == None:
        lat = 0
        lng = 0
        #address.delete()
        # render(request, 'turnos/public/donde_estamos.html', context)

    # Create Map Object
    m = folium.Map(location=[19, -12], zoom_start=2)

    folium.Marker([lat, lng], tooltip='Click para acercarse',
                  popup=country).add_to(m)
    # Get HTML Representation of Map Object
    m = m._repr_html_()
    context = {
        'm': m,
        'form': form,
    }
    return render(request, 'turnos/public/donde_estamos_washington.html', context)

#Faq
class FaqView(generic.ListView):
    template_name = "turnos/public/faq.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("pub_date")

class DetailView(generic.DetailView):
    model=Question
    template_name = "turnos/public/detail.html"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultView(generic.DetailView):
    model=Question
    template_name = "turnos/public/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "turnos/public/detail.html", {
            "question": question, 
            "error_message": "No elegiste una respuesta"
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("results", args=(question.id,)))

#Institucional
def institucional(request):
    personas = Personal.objects.all()
    return render(request, 'turnos/public/institucional.html', {"personas": personas})

#noticias
def noticias(request):
    noticias = Noticia.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'turnos/public/noticias.html', {'noticias': noticias})