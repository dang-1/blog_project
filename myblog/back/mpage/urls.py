from django.urls import path,re_path

from . import views

urlpatterns = [
    #basic
    #path('xxx/xxxx', views.xxxx),
    path('/', views.index),
    #path converters
    #path('articles/<int:year>/<int:month>/', views.month_archive),
    #re
    #re_path('articles/(?P<year>[0-9]{4})/', views.year_archive')
]
