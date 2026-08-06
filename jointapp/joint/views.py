from django.shortcuts import render
from .models import Joint

# Create your views here.
def joint(request):
    joints = Joint.objects.all()
    return render(request, 'joint/jointGui.html', {'joints': joints})    