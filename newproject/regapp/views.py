from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request,'req.html')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        # first_name=request.POST.get("first_name", "default value")
        # last_name = request.POST.get("last_name", "default value")
        # email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            # if User.objects.filter(email=email).exists():
            #     messages.info(request, 'Email Taken')
            #     return redirect('register')
            # elif User.objects.filter(username=username).exists():
            #     messages.info(request, 'Username Taken')
            #     return redirect('register')
            # else:
           user=User.objects.create_user(username=username, password=password,  )
           user.save();
           return redirect('login')
        else:
            messages.info(request, "Password don't match!")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")
def req(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        user = auth.authenticate(username=username, email=email)

        return render(request, 'msg.html')


    return render(request, 'form.html')
        # if request.method == 'POST':
        #     Name = request.POST['Name']
        #     phonenumber = request.POST['phonenumber']
        #     Accounttype = request.POST['Accounttype']
        #     email = request.POST['email']
        #     username = request.POST['username']
        #     country = request.POST['country']
        #     Address = request.POST['Address']
        #     account = request.POST['account']
        #     Gender = request.POST['Gender']
        #     remember = request.POST['remember']
        #
        #
        #     user = auth.authenticate(username=username,name=Name,phonenumber=phonenumber,Accounttype=Accounttype,email=email,country=country,Address=Address,account=account,Gender=Gender,remember=remember)
        #     if user is not None:
        #         auth.req(request, user)
        #         return render(request, 'msg.html')
        #     else:
        #         messages.info(request, 'Invalid Credentials')
        #




        #     if request.method == 'POST':
#         name = request.POST['name']
#         first_name = request.POST.get("first_name", "default value")
#         last_name = request.POST.get("last_name", "default value")
#         email = request.POST['email']
#         password = request.POST['password']
#         cpassword = request.POST['password1']
#         if password == cpassword:
#             if User.objects.filter(email=email).exists():
#                 messages.info(request, 'Email Taken')
#                 return redirect('register')
#             elif User.objects.filter(username=name).exists():
#                 messages.info(request, 'Username Taken')
#                 return redirect('register')
#             else:
#                 user = User.objects.create_user(username=name, first_name=first_name, last_name=last_name,
#                                                 password=password, email=email)
#                 user.save();
#                 return redirect('login')
#         else:
#             messages.info(request, "Password don't match!")
#             return redirect('register')
#         return redirect('/')
#     return render(request, "register.html")
# # def register(request):
# #     if request.method=='POST':
# #        name=request.POST['name']
# #         first_name=request.POST.get("first_name", "default value")
# #         last_name = request.POST.get("last_name", "default value")
# #         email = request.POST['email']
# #         password = request.POST['password']
# #         cpassword = request.POST['password1']
#
def home(request):
    return render(request, 'index.html')



