from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import FileForm
from webapp.models import File


class IndexView(ListView):
    template_name = 'index.html'
    model = File
    context_object_name = 'files'
    ordering = ['-create']
    paginate_by = 10
    paginate_orphans = 1

class FileDetailView(DetailView):
    template_name = 'detail.html'
    model = File
    context_object_name = 'file'


class FileCreateView(CreateView):
    template_name = 'add.html'
    model = File
    form_class = FileForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('webapp:file_detail', kwargs={'pk': self.object.pk})


class FileUpdateView(UserPassesTestMixin, UpdateView):
    template_name = 'update.html'
    model = File
    fields = ('name', 'access')
    context_object_name = 'file'

    def test_func(self):
        file_pk = self.kwargs.get('pk')
        file = File.objects.get(pk=file_pk)
        return self.request.user == file.author or self.request.user.has_perm('webapp.change_file')

    def get_success_url(self):
        return reverse('webapp:file_detail', kwargs={'pk': self.object.pk})


class FileDeleteView(UserPassesTestMixin, DeleteView):
    template_name = 'delete.html'
    model = File
    context_object_name = 'files'
    success_url = reverse_lazy('webapp:index')

    def test_func(self):
        file_pk = self.kwargs.get('pk')
        file = File.objects.get(pk=file_pk)
        return self.request.user == file.author or self.request.user.has_perm('webapp.delete_file')


