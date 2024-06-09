from django.urls import path
from .views import index, article_post, article_detail

urlpatterns = [
    path('', index, name='main-page'),
    path('advertisement-post/', article_post, name='adv-post'),
    path('advertisement/<int:pk>', article_detail, name='adv-detail')
]
