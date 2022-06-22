from django.db.models import Q
from django.shortcuts import render , redirect
from django.contrib import messages
from .models import Room, Topic , Message
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import RoomForm
from django.http import HttpResponse
from django.forms import *
import urllib

# rooms = [
#     {'id': 1 , 'name': 'Python'},
#     {'id': 2, 'name': 'Java 8'},
#     {'id': 3, 'name': 'C++ 14'}
# ]
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('passwd')
        try:
            user= User.objects.get(username=username)
        except :
            messages.error(request, 'User does not exist')

        u1 = authenticate(request, username=username, password=password)
        if u1 is not None:
            login(request, u1)
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'base/login_register.html', context)

def logout_page(request):
     logout(request)
     return redirect('home')

def home(request):
    q = ''
    if request.GET.get('q') != None:
        q = str(request.GET.get('q'))

    print(q)
    rooms = Room.objects.filter(Q(topic__name__icontains=q) | Q(name__icontains=q) | Q(desc__icontains=q))
    topics = Topic.objects.all()
    room_cnt = rooms.count()
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))
    return render(request, 'base/home.html', {'rooms': rooms, 'topics': topics, 'room_cnt': room_cnt , 'room_messages':room_messages})

def room(request, pk):

    myres = Room.objects.get(id=pk)
    room_messages = myres.message_set.all().order_by('-updated')
    participants = myres.participants.all()
    # res = None
    #
    # for j in rooms:
    #     if j['id'] == int(pk):
    #         res = j
    if request.method=='POST':
        msg = Message.objects.create(
            user=request.user,
            room=myres,
            body=request.POST.get('body')
        )
        myres.participants.add(request.user)
        return redirect('room',pk=myres.id)
    r1 = {'room': myres, 'room_messages': room_messages, 'participants': participants}
    return render(request, 'base/room.html', r1)

@login_required(login_url='login')
def create_room(request):
    f1 = RoomForm()

    if request.method == 'POST':
        frm = RoomForm(request.POST)
        if frm.is_valid():
            frm.save()
            return redirect('home')
    context = {'form': f1}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='login')
def update_room(request, pk):
    room = Room.objects.get(id=int(pk))
    curr_frm = RoomForm(instance=room)

    if room.host != request.user:
        return HttpResponse('You are not allowed here')

    if request.method == 'POST':
        curr_frm = RoomForm(request.POST, instance=room)
        if curr_frm.is_valid():
            curr_frm.save()
            return redirect('home')

    context = {'form': curr_frm}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='login')
def delete_room(request, pk):
    room = Room.objects.get(id=pk)

    if room.host != request.user:
        return HttpResponse('You are not allowed here')

    if request.method == 'POST':
        room.delete()
        return redirect('home')

    context = {'room': room}
    return render(request, 'base/delete.html', context)

@login_required(login_url='login')
def delete_message(request, pk):
    msg = Message.objects.get(id=pk)

    if msg.user != request.user:
        return HttpResponse('You are not allowed here')

    if request.method == 'POST':
        msg.delete()
        return redirect('home')

    context = {'room': msg}
    return render(request, 'base/delete.html', context)