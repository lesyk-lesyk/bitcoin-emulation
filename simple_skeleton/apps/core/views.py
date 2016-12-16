from django.shortcuts import render

from django.core.context_processors import csrf
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# def home(request):
#     return render(request, 'core/home.html')

def loginview(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('core/login.html', c)

def logoutview(request):
    logout(request)
    return HttpResponse("Bye!")

def auth_and_login(request, onsuccess='/', onfail='/login/'):
    user = authenticate(username=request.POST['email'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect(onsuccess)
    else:
        return redirect(onfail)  

def save(request, onsuccess='/'):
    if request.user.is_authenticated():
         user = request.user
         print user

def create_user(username, email, password):
    user = User(username=username, email=email)
    user.set_password(password)
    user.save()
    return user

def user_exists(username):
    user_count = User.objects.filter(username=username).count()
    if user_count == 0:
        return False
    return True

def sign_up_in(request):
    post = request.POST
    if not user_exists(post['email']): 
        user = create_user(username=post['email'], email=post['email'], password=post['password'])
    	return auth_and_login(request)
    else:
    	return redirect("/login/")

@login_required(login_url='/login/')
def secured(request):
    userMail = request.user.email
    return render_to_response("core/secure.html", {'userMail': userMail})



from django.shortcuts import render
from django.http import HttpResponseRedirect

from django import forms
class NameForm(forms.Form):
    message = forms.CharField(label='Message', max_length=100)

def message(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if request.user.is_authenticated():
                user = request.user
                
                text = form.cleaned_data['message']
                user.message = message
                user.save()
                print text
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponse("Saved!")

    # if a GET (or any other method) we'll create a blank form
    else:
        # text = request.user.text
        form = NameForm(initial={'message': 'Start Message'})

    return render(request, "core/message.html", {'form': form})    

   