from django.shortcuts import render
from django.http import HttpResponse
from . models import User
from . forms import UserForm


def users(request):
    user_list = User.objects.order_by('last_name')
    result_dict = {'all_users': user_list}
    return render(request, 'exercise/users.html', context=result_dict)


def register(request):
    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return users(request)
        else:
            print("Form is invalid. So sad.")

    return render(request, 'exercise/registration.html', {'form': form})


def index(request):
    return HttpResponse('Hello! You need to check <strong>/users</strong> page to see what you need.')
