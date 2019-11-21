from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Notes
from .forms import NotesForm
# Create your views here.
def index(request):
    text = {'notes' : Notes.objects.all()}

    return render(request,"index.html",text)

def add_notes(request: HttpRequest):
    notes = Notes(text=request.POST['text'])
    notes.save()
    return redirect('/notes/')

def delete_notes(request,id):
    delete_notes = Notes.objects.get(id=id)
    delete_notes.delete()
    return redirect('/notes/')

def edit_notes(request,id):
    if (request.method == "GET"):
        notes = Notes.objects.get(id=id)
        return render(request,'edit_notes.html',{'notes':notes})
    elif(request.method == "POST"):
        notes = Notes.objects.get(id=id)
        form = NotesForm(request.POST, instance=notes)
        if form.is_valid():
            form.save()
            return redirect('/notes/')
