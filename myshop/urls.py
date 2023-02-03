from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include
from users import views as userViews
from django.contrib.auth import views as authViews
from django.conf import settings
from django.conf.urls.static import static

from users.views import profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('registration/', userViews.register, name='reg'),
    path('accounts/login/', authViews.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('exit/', authViews.LogoutView.as_view(template_name='web/index.html'), name='exit'),
    path('profile/', profile, name='profile'),

    # path('accounts/password-reset/', authViews.PasswordResetView.as_view(
    #     template_name="registration/password_reset_form.html"), name='password_reset'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

