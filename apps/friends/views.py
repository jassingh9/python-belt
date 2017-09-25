# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from models import *
import bcrypt
# Create your views here.


def index(request):
    return render(request, "friends/index.html")


def create(request):
    errors = User.objects.register_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error)
        return redirect('/')
    if request.method == "POST":
        new_password = request.POST['password']
        User.objects.create(
            name=request.POST['name'],
            alias=request.POST['alias'],
            email=request.POST['email'],
            birthday=request.POST['birthday'],
            password=bcrypt.hashpw(
                new_password.encode('utf8'), bcrypt.gensalt())
        )
        a = User.objects.last()
        request.session['user'] = a.id
        request.session['user_name'] = a.name

    return redirect('/friends')


def login(request):
    errors = User.objects.login_validator(request.POST)
    if request.method == 'POST':
        email = request.POST['login_email']
        password = request.POST['login_pass']
        user = User.objects.filter(email=email)
        if len(user):
            for u in user:
                if bcrypt.checkpw(password.encode('utf8'), u.password.encode('utf8')):
                    request.session['user_name'] = u.name
                    request.session['user'] = u.id
                    print request.session['user']
                    return redirect('/friends')
            else:
                messages.error(request, "email/password incorrect")
        else:
            messages.error(request, "email/password incorrect")

    return redirect('/')


def friends(request):
    friends = Friend.objects.filter(client_friend=request.session['user'])
    not_friends = Friend.objects.exclude(
        receive_friend=request.session['user'])
    friend_id = []
    for user in friends:
        friend_id.append(user.receive_friend.id)
    context = {
        'users': User.objects.all(),
        'friends': Friend.objects.all(),
        'friends_name': User.objects.filter(id__in=friend_id),
        'not_friends': User.objects.exclude(id__in=friend_id),

    }

    return render(request, 'friends/friends.html', context)


def addFriend(request, user_id, friend_id):
    user = User.objects.get(id=user_id)
    friend = User.objects.get(id=friend_id)
    Friend.objects.create(client_friend=user, receive_friend=friend)
    Friend.objects.create(client_friend=friend, receive_friend=user)
    return redirect('/friends')


def removeFriend(request, user_id, friend_id):
    user = User.objects.get(id=user_id)
    friend = User.objects.get(id=friend_id)
    Friend.objects.get(client_friend=user, receive_friend=friend).delete()
    Friend.objects.get(client_friend=friend, receive_friend=user).delete()
    return redirect('/friends')


def user(request, user_id):
    context = {
        'users': User.objects.get(id=user_id)
    }
    return render(request, 'friends/user.html', context)
