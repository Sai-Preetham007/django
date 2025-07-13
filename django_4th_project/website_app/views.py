from django.shortcuts import render

# Create your views here.
def index(request):
    name = "$@! **7"
    user_name = "Sai_Preetham_26"
    password = "26102000S@i12579"

    context = {
        'Name' : name,
        'User_Name' : user_name,
        'Password' : password
    }

    return render(request, "index.html", context)