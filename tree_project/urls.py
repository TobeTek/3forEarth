"""tree_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls 
\

API_TITLE = '3 For Earth API'
API_DESCRIPTION = 'API support for non-profit green movement, #3ForEarth'

schema_view = get_schema_view(title= '3ForEarth API')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/accounts/', include('accounts.urls')),
    path('api/v1/', include('trees.urls')),
    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    path('schema/', schema_view)
]
