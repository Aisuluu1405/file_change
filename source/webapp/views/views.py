# from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
# from django.http import HttpResponseRedirect
# from django.urls import reverse_lazy, reverse
# from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# 
# from webapp.models import Book
# 
from django.views.generic import ListView
#удалить эту строчку импорт
 class IndexView(ListView):
#     template_name = 'index.html'
#     model =  Book
#     context_object_name = 'books'
     ordering = ['id']
     paginate_by = 5
     paginate_orphans = 1
# 
# class BookDetailView(LoginRequiredMixin, DetailView):
#     template_name = 'book/detail.html'
#     model = Book
#     context_object_name = 'book'
# 
# 
# class BookCreateView(LoginRequiredMixin, CreateView):
#     template_name = 'add.html'
#     model = Book
#     # form_class = BookForm
# 
#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.reader = self.request.user
#         self.object.save()
#         return HttpResponseRedirect(self.get_success_url())
# 
#     def get_success_url(self):
#         return reverse('webapp:index')
# 
# 
# class BookUpdateView(UserPassesTestMixin, UpdateView):
#     template_name = 'update.html'
#     model = Book
#     fields = ('name', 'description', 'status', 'photo', 'type')
#     context_object_name = 'book'
# 
#     def test_func(self):
#        book_pk = self.kwargs.get('pk')
#         book = Book.objects.get(pk=book_pk)
#         return self.request.user == book.reader or self.request.user.has_perm('webapp.change_book')
# 
#     def get_success_url(self):
#         return reverse('webapp:index')
# 
# 
# class BookDeleteView(UserPassesTestMixin, DeleteView):
#     template_name = 'delete.html'
#     model = Book
#     context_object_name = 'books'
#     success_url = reverse_lazy('webapp:index')
# 
#    def test_func(self):
#        book_pk = self.kwargs.get('pk')
#        book = Book.objects.get(pk=book_pk)
#        return self.request.user == book.reader or self.request.user.has_perm('webapp.delete_book')
# 

