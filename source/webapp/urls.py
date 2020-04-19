from django.urls import path
from webapp.views import IndexView, FileCreateView, FileDetailView, FileUpdateView, FileDeleteView, PrivateUserAdd, PrivateUserDelete


app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('file/<int:pk>/', FileDetailView.as_view(), name='file_detail'),
    path('file/add/', FileCreateView.as_view(), name='file__add'),
    path('file/update/<int:pk>/', FileUpdateView.as_view(), name='file_update'),
    path('file/delete/<int:pk>/', FileDeleteView.as_view(), name='file_delete'),
    # path('advert/add-to-favorites/', AddToPrivates.as_view(), name='add_to_privates'),
    # path('advert/delete-from-favorites/', DeleteFromPrivates.as_view(), name='delete_from_privates'),
    path('user_private_delete/', PrivateUserDelete.as_view(), name='user_private_delete'),
    path('user_private_add/', PrivateUserAdd.as_view(), name='user_private_add'),
    # path('search_user/', SearchUserView.as_view(), name='search_user'),
]
