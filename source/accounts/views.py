from django.contrib.auth import login
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.models import User

from accounts.models import Profile
from .forms import UserCreationForm, UserChangeForm, PasswordChangeForm


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],

            )
            user.set_password(form.cleaned_data['password'])
            user.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('webapp:index')
    else:
        form = UserCreationForm()
    return render(request, 'user_create.html', context={'form': form})


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'

   # def get_context_data(self, **kwargs):
    #    context = super().get_context_data()
     #   user = User.objects.get(pk=self.kwargs['pk'])
      #  context['adverts'] = Advert.objects.filter(author=user.pk)
       # return context



class UserPersonalInfoChangeView(UserPassesTestMixin, UpdateView):
    model = User
    template_name = 'user_info_change.html'
    form_class = UserChangeForm
    context_object_name = 'user_obj'

    def test_func(self):
        return self.request.user.pk == self.kwargs['pk']

    def get_success_url(self):
        return reverse('accounts:user_detail', kwargs={'pk': self.object.pk})


class UserPasswordChangeView(UserPassesTestMixin, UpdateView):
    model = User
    template_name = 'user_password_change.html'
    form_class = PasswordChangeForm
    context_object_name = 'user_obj'

    def test_func(self):
        return self.request.user.pk == self.kwargs['pk']

    def get_success_url(self):
        return reverse('accounts:login')


