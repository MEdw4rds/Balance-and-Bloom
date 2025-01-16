from django.shortcuts import render

# Create your views here.
def about(request):
    """
    Renders the homepage.

    **Template:**

    :template:`about/about.html`
    """
    return render(request, 'about/about.html')
