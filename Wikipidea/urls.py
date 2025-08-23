from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='home'),
    path('accounts/',include('accounts.urls'), name='accounts'),
    path('posts/',include('post.urls'), name='posts'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
