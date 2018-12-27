from django.shortcuts import render, redirect
from my_day import settings
import os
from django.core.urlresolvers import reverse
from datetime import  datetime
from models import *
def index(request):
    uname = request.session.get('uname')
    context = {'uname': uname}
    return render(request, 'index.html', context)


def login(request):
    return render(request, 'login.html')


def login_handle(request):
    request.session['uname'] = request.POST['uname']
    request.session['upwd'] = request.POST['upwd']
    # return redirect(reverse('home:index'))
    # return render(request, 'index.html',context)
    uname = request.session.get('uname')
    context = {'uname':uname}
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
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    umsg = request.POST['umsg']
    ugender = request.POST['ugender']
    uprivate = request.POST['uprivate']
    context = {'uname': uname, 'upwd': upwd,'umsg':umsg, 'ugender': ugender, 'uprivate': uprivate}
    return render(request, 'submit.html', context)


def usr_info(request):
    uname = request.session['uname']
    context = {'uname': uname}
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

    try:
        Msg = Message.objects.get(mowner=uname)
    except:
        pass
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
