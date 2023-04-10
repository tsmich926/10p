from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<pk>/cancel',views.cancel,name='cancel'),
    path('<pk>/complete',views.complete,name='complete'),
    path('<pk>/delete/', views.delete,name='delete'),
]