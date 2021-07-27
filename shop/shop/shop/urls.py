"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from shopping import views as s
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', s.home, name="home"),
    path('signup/', s.user_signup, name='signup'),
    path('login/', s.user_login, name='login'),
    path('logout/', s.user_logout, name='logout'),
    path('userList/', s.user_list, name='userList'),
    path('detail/<str:id>', s.detail, name='detail'),
    path('order/<str:id>/<str:user_id>', s.order, name='order'),
    path('order_list/<str:user_id>', s.order_list, name='order_list'),
    path('new/', s.new, name='new'),
    path('delete/<str:id>', s.delete, name='delete'),
    path('update/<str:id>', s.update, name='update'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
