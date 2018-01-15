from django.urls import path


from .views import upload

app_name = 'blog'
urlpatterns = [
    path('upload/', upload)
]

