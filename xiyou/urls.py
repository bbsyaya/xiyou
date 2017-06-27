"""xiyou URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

import xadmin

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^captche/', include('captcha.urls')),
    url(r'', include('apps.users.urls', namespace='user')),
    url(r'', include('apps.service.urls', namespace='service')),
    url(r'', include('apps.operation.urls', namespace='operation')),
    url(r'', include('apps.university.urls', namespace='university')),
]
