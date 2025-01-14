from django.shortcuts import render

# Create your views here.


def home(request):
    """
    Renders the homepage.

    **Template:**

    :template:`homepage/home.html`
    """
    return render(request, 'homepage/home.html')
