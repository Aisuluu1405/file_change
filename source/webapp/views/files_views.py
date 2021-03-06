from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils.http import urlencode
from webapp.forms import FileForm, SimpleSearchForm, CommonFileForm, SearchUserForm
from webapp.models import File


class IndexView(ListView):
    template_name = 'index.html'
    model = File
    context_object_name = 'files'
    ordering = ['-create']
    paginate_by = 10
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(). get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        # context['common'] = File.objects.filter(access='common')
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context


    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(name__icontains=self.search_value) & Q(access='common')
            queryset = queryset.filter(query)
        else:
            queryset = queryset.filter(access='common')
        return queryset

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


class FileDetailView(UserPassesTestMixin, DetailView):
    template_name = 'detail.html'
    model = File
    context_object_name = 'file'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchUserForm()
        return context

    def test_func(self):
        file = self.get_object()
        return self.request.user == file.author or self.request.user in file.private.all()


class FileCreateView(CreateView):
    template_name = 'add.html'
    model = File

    def get_form_class(self):
        if self.request.user.is_anonymous:
            self.form_class = CommonFileForm
        else:
            self.form_class = FileForm
        return self.form_class

    def form_valid(self, form):
        self.object = form.save(commit=False)
        if self.request.user.username:
            self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('webapp:file_detail', kwargs={'pk': self.object.pk})


class FileUpdateView(UserPassesTestMixin, UpdateView):
    template_name = 'update.html'
    model = File
    fields = ('name', 'file', 'access')
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


