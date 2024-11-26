"""wgdnet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from filebrowser.sites import site

from lite_cms_core_sample import views


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/filebrowser/', site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('admin/', admin.site.urls),

    path('', views.index, name='home'),

    path('lite_cms_core/', include('lite_cms_core.urls')),

    path('base/<int:pk>/', views.BaseItemDetailView.as_view(), name='base-item-detail'),
    path('slugged/<slug:slug>/', views.SluggedItemDetailView.as_view(), name='slugged-item-detail'),
    path('content/<slug:slug>/', views.ContentItemDetailView.as_view(), name='content-item-detail'),
]
if settings.DEBUG:  # pragma: no cover
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
