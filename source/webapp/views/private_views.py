from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import TemplateView

from webapp.models import Private, File


class AddToPrivates(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        user = request.user
        file = get_object_or_404(File, pk=request.POST.get('pk'))
        Private.objects.get_or_create(user=user, file=file)
        return JsonResponse({'pk': file.pk})


class DeleteFromPrivates(LoginRequiredMixin, View):
    permission_required = "webapp.delete_favorite"

    def post(self, request, *args, **kwargs):
        user = request.user
        file = get_object_or_404(File, pk=request.POST.get('pk'))
        Private.objects.filter(file=file, user=user).delete()
        return JsonResponse({'pk': file.pk})

#
# class SearchUser(TemplateView):
#     template_name = "user-search.html"
#
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         result_list = []
#         q = self.request.GET.get('q', None)
#         if q:
#             result_list = [user for user in User.objects.filter(
#                 Q(username__icontains=q))]
#             context = {
#                 "result": result_list,
#                 "query": q,
#             }
#         return context