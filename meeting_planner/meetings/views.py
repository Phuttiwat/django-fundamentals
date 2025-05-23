from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory
from meetings.models import Meeting, Room

@login_required
# Create your views here.
def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, 'meetings/detail.html', {'meeting':meeting})

def rooms_list(request):
    rooms = Room.objects.all()
    return render(request,'meetings/rooms_list.html', {'rooms':rooms})

MeetingForm = modelform_factory(Meeting,exclude=[])

def new(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(request, 'meetings/new.html', {'form': form})

def edit(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    if request.method == 'POST':
        form = MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
            form.save()
            return redirect('detail',id)
    else:
        form = MeetingForm(instance=meeting)
    return render(request,'meetings/edit.html',{'form':form})

def delete(request,id):
    meeting = get_object_or_404(Meeting, pk=id)
    if request.method == 'POST':
        meeting.delete()
        return redirect('welcome')
    else: return render(request,'meetings/confirm_delete.html',{'meeting':meeting})