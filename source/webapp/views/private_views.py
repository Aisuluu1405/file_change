from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views import View
from webapp.models import Private, File


class PrivateUserAdd(View):

    def post(self, request):
        file = File.objects.get(pk = int(request.POST['file']))
        user = request.POST['user_name']
        try:
            user_obj = User.objects.get(username=user)
            file_exists = Private.objects.get_or_create(file=file, user=user_obj)
            if file_exists[1] == False:
                return JsonResponse({'answer': 'Пользователь уже существует!'})
            else:
                return JsonResponse({'answer': 'Пользователь успешно добавлен!', 'user' : user_obj.username, 'user_id' : user_obj.id, 'file_id': file.pk})
        except User.DoesNotExist as e:
            print(e)
            return JsonResponse({'answer':'Нет такого пользователя'})


class PrivateUserDelete(View):

    def post(self, request):
        file = File.objects.get(pk=int(request.POST['file_id']))
        user = User.objects.get(id=int(request.POST['user_id']))
        Private.objects.filter(file=file, user=user).delete()
        return JsonResponse({'status': '200'})


