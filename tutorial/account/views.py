from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def home(request):
    name = "Abhishek"
    branch = "Information Technology"
    college = "College of Engineering Roorkee "
    num = [1, 2, 3, 4]
    args = {"name": name, "college": college, "branch": branch, "year": num}
    return render(request, 'account/home.html', args)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')
    else:
        form = UserCreationForm()

        args={'form':form}
        return render(request, 'account/reg_form.html', args)



