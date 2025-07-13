from django.shortcuts import render

# Create your views here.
def index(request):
    developed_by = "Sai Preetham"
    family_members = [
        "Sai Preetham",
        "Krishna Chaitanya",
        "Subhashini",
        "Venkateswara"]

    context = {
        "Developer" : developed_by,
        "Family_Members" : family_members
    }

    response = render(request, "index.html", context)
    return response