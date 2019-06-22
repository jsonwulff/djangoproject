from django.urls import path
from . import views

urlpatterns = [
    # ex: /posts/
    path('', views.index, name='index'),
    # ex: /posts/5/
    path('<int:posts_id>/', views.detail, name='detail'),
    # ex: # ex: /posts/5/results/
    path('<int:posts_id>/results', views.results, name='results'),
    
]