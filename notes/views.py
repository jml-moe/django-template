from django.shortcuts import render
from .models import Notes

# Create your views here.
def index_view(request):
    notes = Notes.objects.all()

    context = {
        "notes": notes
    }

    return render(request, 'index.html', context)

    # context = {
    #     "username": "Jamil",
    #     "email": "jamil@me.com"
    # } # -> bentuknya dict, bisa berupa third-party api atau database dll.

    # my_hobbies = ["reading", "coding", "sleeping"]

    # # return render(request, 'index.html', context) # -> fungsi render() hanya menerima satu parameter
    # return render(request, 'index.html', {"hobbies": my_hobbies}) # -> hobbies itu nama key-nya

    # Solusi penggabungan data kedalam satu dict.
    
    # context = {
    # "username": "Jamil",
    # "email": "jamil@me.com",
    # "my_hobbies": ["reading", "coding", "sleeping"]
    # }
    # return render(request, 'index.html', context)