from django.shortcuts import render,redirect
from .models import signup

def home(request):
    return render(request,'form.html',{})

def login_page(request):
    return render(request,'login.html',{})

def show_page(request):
    data = signup.objects.all()
    return render(request,"show.html",{'data':data})

def InsertData(request):
    username = request.POST['uname']
    email = request.POST['email']
    password = request.POST['pass']
    login = signup.objects.filter(email=email)
    if login:
        context={
            "signupMsg":"email already exist"
        }
        return render(request,"form.html",context)
    else:
        user = signup.objects.create(username=username,email=email,password=password)
        context={
            "signupemail":email
        }
        return render(request,'login.html',context)

def loginData(request):
    email = request.POST['email']
    password = request.POST['pass']
    login = signup.objects.get(email=email)
    if login:
        if login.password == password:
            request.session['id'] = login.id
            request.session['name'] = login.username
            return redirect('show')
        else:
            context={
                "loginPass":"incorrect password"
            }
            return render(request,'login.html',context)
    else:
        context={
            "loginEmail":"email not exist"
        }
        return render(request,'login.html',context)

def deleteData(request,pk):
    udata = signup.objects.get(id=pk)
    udata.delete()
    return redirect('show')

def EditPage(request,pk):
    data = signup.objects.get(id=pk)
    return render(request,"edit.html",{'data':data})

def UpdateData(request,pk):
    uid = signup.objects.get(id=pk)
    # username = request.POST['uname']
    # email = request.POST['email']
    # password = request.POST['pass']
    # editEmail = signup.objects.filter(email=email)
    # if editEmail:
    #     context={
    #         "editmsg":"email already exist"
    #     }
    #     return render(request,"edit.html",context)
    # else:
    #     context1={
    #         "editmsg2":email
    #     }
    uid.username = request.POST['uname'];
    uid.email = request.POST['email'];
    uid.password = request.POST['pass'];
    uid.save()
    return redirect('show')

