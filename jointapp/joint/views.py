from django.shortcuts import render

# Create your views here.
def joint(request):
    return render(request, 'joint/jointGui.html')