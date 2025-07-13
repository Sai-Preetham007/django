from django.shortcuts import render

# Create your views here.
def index(request):
    developer = "Sai Preetham Reddy"
    family_members = ["Venkateswara", "Subhashini", "Sai Preetham", "Krishna Chaitanya"]

    context = {
        'dev' : developer,
        'members' : family_members
    }

    response = render(request, "index.html", context)
    return response