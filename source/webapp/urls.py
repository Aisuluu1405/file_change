from django.urls import path
from webapp.views import IndexView, FileCreateView, FileDetailView, FileUpdateView, FileDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('file/<int:pk>/', FileDetailView.as_view(), name='file_detail'),
    path('file/add/', FileCreateView.as_view(), name='file__add'),
    path('file/update/<int:pk>/', FileUpdateView.as_view(), name='file_update'),
    path('file/delete/<int:pk>/', FileDeleteView.as_view(), name='file_delete'),
]
