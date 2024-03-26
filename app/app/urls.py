from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registrar/', views.registrar_paes, name='registrar_paes'),
]
