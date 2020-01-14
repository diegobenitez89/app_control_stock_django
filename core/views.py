from django.shortcuts import render, redirect
from .models import Producto, Registrado
from .forms import ProductoForm, RegModelForm, ContactForm
from django.core.mail import send_mail
from django.conf import settings



def home(request):
    return render(request,'core/home.html')

def inicio(request):
    titulo = "Bienvenidos"
    if request.user.is_authenticated:
        titulo = "Bienvenid@ %s" %(request.user)
    form = RegModelForm(request.POST or None)
    
    context = {
                "titulo": titulo,
                "el_form": form,
            }

    if form.is_valid():
        instance = form.save(commit=False)
        nombre = form.cleaned_data.get("nombre")
        email = form.cleaned_data.get("email")
        if not instance.nombre:
            instance.nombre = "persona"
        instance.save()

        context = {
            "titulo" : "gracias %s!" %(nombre)
        }
        print (instance.nombre)
        print (instance.timestamp)

    if request.user.is_authenticated and request.user.is_staff:
        queryset = Registrado.objects.all().order_by("-timestamp")
        context = {
            "queryset": queryset,
        }
    return render(request, "inicio.html", context)

def contact(request):
    titulo = "Contacto"
    form =  ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_mensaje = form.cleaned_data.get("mensaje")
        form_nombre = form.cleaned_data.get("nombre")
        asunto = "form de contacto"
        email_from = settings.EMAIL_HOST_USER
        email_to = [email_from, "otroemail@gmail.com"]
        email_mensaje = "%s: %s enviado por %s" %(form_nombre, form_mensaje, form_email)
        send_mail(asunto,
            email_mensaje,
            email_from,
            email_to,
            fail_silently=False
            )


    context = {
        "form" : form,
        "titulo" : titulo,
    }
    return render (request, "forms.html", context)

def listado_producto(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request,'core/lista_producto.html', data)


def nuevo_producto(request):
    data = {
        'form': ProductoForm()
   
    }

    if request.method == "POST":
        form = ProductoForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            data['mensaje'] = "Guardado correctamente"

    return render(request,'core/nuevo_producto.html', data)


def modificar_producto(request, id):
    producto = Producto.objects.get(id=id)
    data = {
        'form': ProductoForm(instance=producto)
   
    }


    if request.method == "POST":
        form = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if form.is_valid():
            form.save()
            data['mensaje'] = "Modificado correctamente"
        data['form'] = ProductoForm(instance=Producto.objects.get(id=id))

    return render(request, 'core/modificar_producto.html', data)


def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()

    return redirect(to='listado_producto')

