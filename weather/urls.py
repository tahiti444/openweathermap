
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('hwi/', views.today_hwi, name='today_hwi')
]