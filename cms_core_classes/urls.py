from django.urls import path

from cms_core_classes import views

app_name = 'cms_core_classes'

urlpatterns = [
    path('search/', views.search, name='search'),
    path('extsearch/', views.ext_search_form, name='extsearch'),
]
