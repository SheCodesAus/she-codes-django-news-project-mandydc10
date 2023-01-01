from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
# from news.models import NewsStory

# @ login_required
# def favourite_add(request, id):
#     NewsStory = get_object_or_404(NewsStory, id=id)
#     if NewsStory.favourites.filter(id=request.user.id).exists():
#         NewsStory.favourites.remove(request.user)
#     else:
#         NewsStory.favourites.add(request.user)
#     return HttpResponseRedirect(request.META['HTTP_REFERER'])


class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

    def form_valid(self,form):
        f=super().form_valid(form)
        user = self.get_object
        login(self.request, user)
        return f

class ViewAccount(generic.DetailView):
    model = CustomUser
    success_url = reverse_lazy('login')
    template_name = 'users/viewAccount.html'
    context_object_name = 'profile'

class UpdateAccount(UpdateView):
    form_class = CustomUserChangeForm
    model = CustomUser
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'
    context_object_name = 'update-account'
