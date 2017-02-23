from django.conf.urls import url
from gaming_patrada import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/(?P<game_name_slug>[\w\-]+)/$', views.gamedetail, name='gamedetail'),
    url(r'^games/', views.all_games, name='allgames'),
    url(r'^review/', views.review, name='review'),
    url(r'^donate/', views.donate, name='donate'),

]
