from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages

# Create your views here.
def root(request):
    return redirect('/shows')

def shows(request):
    context = {
        'shows': Show.objects.all() 
    }
    print(context['shows'].values())
    return render(request, 'shows.html', context)

def new(request):
    return render(request, 'new_show.html')

def addShow(request):
    errors = Show.objects.showValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        title = request.POST['title']
        network = request.POST['network']
        rel_date = request.POST['release_date']
        desc = request.POST['desc']
        Show.objects.create(title=title, network=network, release_date=rel_date, desc=desc)
        newId = Show.objects.last()
        return redirect('/shows/' + str(newId.id))

def showDetails(request, show_id):
    context = {
        'show': Show.objects.get(id=show_id)
    }
    return render(request, 'show_details.html', context)

def editShow(request, show_id):
    if request.method == 'GET':
        context = {
            'show': Show.objects.get(id=show_id)
        }   
        return render(request, 'edit_show.html', context)
        
    if request.method == 'POST':
        errors = Show.objects.showValidator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/shows/' + str(show_id) + '/edit')
        else:
            show = Show.objects.get(id=show_id)
            show.title = request.POST['title']
            show.network = request.POST['network']
            show.release_date = request.POST['release_date']
            show.desc = request.POST['desc']
            show.save()
            return redirect('/shows/' + str(show.id))

def deleteShow(request, show_id):
    show = Show.objects.get(id=show_id)
    show.delete()
    return redirect('/shows')