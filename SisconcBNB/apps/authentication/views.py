from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, login, authenticate
# class based views.
from django.views.generic import TemplateView, View
# import mixins
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class HomeTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'pagina/bienahab.html'

# login
class LoginView(View):

    def get(self, request):
        form = AuthenticationForm()
        return render(request, "login/login.html", { 'form': form })

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # redirect
                url_next = request.GET.get('next')
                if url_next is not None:
					return redirect(url_next)
                else:
					#return redirect(reverse_lazy('eventos:list'))
                    return render(request,'pagina/bienahab.html')
            else:
                return HttpResponse("Inactive user.")
        else:
            return redirect('/')
        return render(request)

# logout
class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('/')