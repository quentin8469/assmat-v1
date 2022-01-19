from django.shortcuts import render
from famille.models import Employeur


# Create your views here.
def index(request):
    """ """
    employeurs = Employeur.objects.all()
    context = {"employeurs":employeurs}
    
    return render(request, "dashboard/base_dashboard.html", context)


