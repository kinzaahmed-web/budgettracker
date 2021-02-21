"""django_budget URL Configuration

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
from django.urls import path
from django.conf.urls import include
from django.contrib.auth import views as auth
from register import views as v
from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path('', include('budget.urls')),
    path("register/", v.register, name="register"),
    path('login/', auth.LoginView.as_view(template_name='register/login.html'), name='login'),
    path('logout/', auth.LogoutView.as_view(template_name='register/logout.html'), name='logout'),
    path('admin/', admin.site.urls),
    path('jsi18n', JavaScriptCatalog.as_view(), name='javascript-catalog'),
]