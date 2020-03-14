from django.urls import path
from webapp.views import IndexView
# 
app_name = 'webapp'
# 
 urlpatterns = [
     path('', IndexView.as_view(), name='index'),
#     path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
#     path('book/add/', BookCreateView.as_view(), name='book__add'),
#     path('book/update/<int:pk>/', BookUpdateView.as_view(), name='book_update'),
#     path('book/delete/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),
# 
 ]
