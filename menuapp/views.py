from django.shortcuts import render

def menu_view(request):
    return render(request, 'menuapp/base.html')

def contacts_view(request):
    return render(request, 'menuapp/contacts.html')

def person_view(request):
    return render(request, 'menuapp/person.html')