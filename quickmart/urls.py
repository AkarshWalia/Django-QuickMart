from django.contrib.auth import views as auth_views
from django.contrib import admin 
from django.urls import path,include
from user import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('items.urls')),
    path('register/' , user_views.register , name = 'register'),
    path('login/' , auth_views.LoginView.as_view(template_name = 'login.html') , name = 'login'),
    path('logout/' , auth_views.LogoutView.as_view(template_name = 'logout.html') , name = 'logout'),
    path('profile/' , user_views.profile , name = 'profile' )

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
