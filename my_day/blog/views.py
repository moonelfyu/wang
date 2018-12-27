# encoding=utf8
from django.shortcuts import render, redirect
from my_day import settings
import os
from django.core.urlresolvers import reverse
from datetime import  datetime
from models import *
from django.http import HttpResponse




def index(request):
    uname = request.session.get('uname')
    context = {'uname': uname}
    #return HttpResponse("你好")
    return render(request, 'index.html', context)


def login(request):
    return render(request, 'login.html')


def login_handle(request):
    try:
        user_login = Usr.objects.get(uname=request.POST['uname'])
        request.session['uname'] = user_login
        request.session['upwd'] = request.POST['upwd']
        # return redirect(reverse('home:index'))
        # return render(request, 'index.html',context)
        context = {'uname': request.session.get('uname')}
        return render(request, 'index.html', context)
    except:
        # user_login = False
        context = {'uname': None}
        return render(request, 'index.html', context)


def logout(request):
    # request.session['uname'] = None
    # del request.session['uname']
    # request.session.clear()
    request.session.flush()
    return redirect(reverse('home:index'))


def register(request):
    return render(request, 'register.html')


def submit(request):
    new_usr = Usr()
    new_usr.uname = request.POST['uname']
    new_usr.upassword = request.POST['upwd']
    new_usr.umsg = request.POST['umsg']
    new_usr.ugender = request.POST['ugender']
    new_usr.uprivate = request.POST['uprivate']
    new_usr.ulogo = 0
    new_usr.ubackground = 0
    new_usr.save()
    context = {'uname': new_usr.uname, 'upwd': new_usr.upassword,
               'umsg': new_usr.umsg, 'ugender': new_usr.ugender,
               'uprivate': new_usr.uprivate}
    return render(request, 'submit.html', context)


def usr_info(request):
    user_login = Usr.objects.get(uname=request.session['uname'])
    new_usr = user_login
    context = {'uname': new_usr.uname, 'upwd': new_usr.upassword,
               'umsg': new_usr.umsg, 'ugender': new_usr.ugender,
               'uprivate': new_usr.uprivate}
    return render(request, 'usr_info.html', context)


def contact(request):
    uname = request.session.get('uname')
    mycontect1 = os.path.join(settings.MEDIA_ROOT, '1.png')
    mycontect = {'mypath': mycontect1}
    if uname != 'None':
        mycontect['uname'] = request.session.get('uname')
    return render(request, 'contact.html', mycontect)


def content(request):
    uname = request.session.get('uname')
    Msg = Message.objects.get(mowner=uname)
    # Msg = Message()
    Msg.mowner = uname
    if Msg.mowner != uname:
        return render(request, 'index.html')
    else:
        Msg.mtitle = request.POST['mtitle']
        Msg.mbody = request.POST['mbody']
        Msg.mdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # Msg.mowner = uname
        Msg.save()

    return render(request, 'index.html', {'content': Msg})
