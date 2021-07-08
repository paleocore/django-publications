__license__ = 'MIT License <http://www.opensource.org/licenses/mit-license.php>'
__author__ = 'Lucas Theis <lucas@theis.io>'
__docformat__ = 'epytext'

from django.urls import include, path, re_path
try:
    from django.conf.urls import url
except ImportError:
    from django.conf.urls.defaults import url

from publications import views

app_name = 'publications'
urlpatterns = [
    path('', views.year, name='index'),
    path('year/<int:year>/', views.year, name='year'),
    path('<int:pk>/', views.id, name='id'),
    path('tag/<keyword>/', views.keyword, name='keyword'),
    path('list/<list>/', views.list, name='list'),
    path('unapi/', views.unapi, name='unapi'),
    path('<name>/', views.author, name='author'),
    #re_path(r'(?P<publication_id>\d+)/', views.id, name='id'),
    #path('year/(?P<year>\d+)/', views.year, name='year'),
    #re_path(r'^tag/(?P<keyword>.+)/$', views.keyword, name='keyword'),
    #re_path(r'^list/(?P<list>.+)/$', views.list, name='list'),
    #re_path(r'^unapi/$', views.unapi, name='unapi'),
    #e_path(r'^(?P<name>.+)/$', views.author, name='author'),
]
