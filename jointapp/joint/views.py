from django.shortcuts import get_object_or_404, render, redirect
from .models import Joint

# Create your views here.
def joint(request):
    joints = Joint.objects.all()
    return render(request, 'joint/jointGui.html', {'joints': joints})    


def change_joint(request, id):
    joint = get_object_or_404(Joint, id=id)

    if request.method == "POST":
        new_angle = request.POST.get("new_angle")   
        
        if new_angle is not None:
            joint.degree = new_angle
            joint.save()
            return redirect("list_joint")
        else:
            pass

    return redirect("list_joint")