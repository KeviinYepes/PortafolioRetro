from django.shortcuts import render, redirect
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        # Capturamos los datos que vienen del formulario
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Por ahora, imprimimos en la terminal para confirmar que llegan
        print(f"Mensaje de: {name} <{email}>: {message}")

        # Añadimos un mensaje de éxito que puedes mostrar en el HTML
        messages.success(request, '¡Gracias por escribir! Me pondré en contacto pronto.')
        
        return redirect('home') # Recarga la página para limpiar el formulario

    return render(request, 'portafolio/main.html')