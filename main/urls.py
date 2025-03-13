from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='home'),
    path('articles/', views.articles_view, name='articles'),
    path('article-detail/', views.article_detail, name='artice_detail'),
    path('register-login/',views.auth_view, name='auth_view'),
    path('team/', views.team_view, name='teams'),
    path('sequence/', views.sequence_view, name='sequence'),
    path('news/', views.news_view, name='news'),
    path('contact/', views.contact_view, name='contact'),
    path('logout/',views.logout_view, name='logout'),
]
