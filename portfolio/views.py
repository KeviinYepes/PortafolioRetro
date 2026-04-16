from django.contrib import messages
from django.shortcuts import redirect, render


def home(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()

        print(f"Mensaje de: {name} <{email}>: {message}")
        messages.success(request, "Gracias por escribir. Me pondre en contacto pronto.")
        return redirect("home")

    return render(request, "portafolio/main.html")
