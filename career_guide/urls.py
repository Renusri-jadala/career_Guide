"""career_guide URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from application import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login_view,name='login'),
    path('logout',views.logout_view,name='logout'),
    path('add-career',views.add_career,name='add_career'),
    path('add-technology',views.add_technology,name='add_technology'),
    path('career-list',views.career_list,name='career_list'),
    path('technologies/<int:pk>/',views.technologies,name='technologies'),
    path("career/<int:pk>/wishlist/add/",views.add_to_wishlist, name="add_to_wishlist"),
    path('add-wish/<int:pk>/',views.add_wish,name='add_wish'),
    path("wishlist/",views.wishlist, name="wishlist"),
    path("wishlist/remove/<int:pk>/",views.remove_item, name="remove_item"),
    
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)