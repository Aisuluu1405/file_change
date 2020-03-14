# pk объекта Favorite теперь в ответе не нужен, т.к.
# соответствующий DeleteFromFavorites на него больше не
# ориентируется.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
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
