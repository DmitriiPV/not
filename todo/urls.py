from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #
    path('deletePpl', views.deletePpl, name='deletePpl'),
    #
    path('createPpl', views.createPpl, name='createPpl'),
    # роут для отображения страницы - Регистрация нового пациента
    path('reg', views.reg, name='reg'),
    # роут Домашней страницы
    path('', views.index, name='index'),
    #
    path('doctorspecial', views.doctorspecial, name='doctorspecial'),
    #

    # роут для отображения страницы - Дата обращения
    path('dateof', views.dateof, name='dateof'),
    #

    #

    # роут для отображения страницы - Сотрудники

    #

    #

    #

    #

    #

]
