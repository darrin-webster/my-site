# Django imports paths 
from django.urls import path
# from polls view
from . import views

# the definition of index from views
urlpatterns = [
    path('', views.index, name='index'),
]