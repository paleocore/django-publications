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
    path('', views.cite, name='index'),
    path('citekey/<citekey>/', views.cite, name='cite'),
    path('year/<int:year>/', views.year, name='year'),
    path('<int:publication_id>/', views.id, name='id'),
    path('tag/<keyword>/', views.keyword, name='keyword'),
    path('list/<list>/', views.list, name='list'),
    path('unapi/', views.unapi, name='unapi'),
    path('<name>/', views.author, name='author'),
]
