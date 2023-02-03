from django.urls import path
from django.contrib.auth import views as authViews
from .views import password_reset_request

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('shop/', views.shop, name='shop'),
    path('product/<int:id>/', views.product, name='product'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('post-list/', views.post_list, name='post_list'),
    path(r'(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),
    path('accounts/password-reset/', password_reset_request, name='password_reset'),

    path('accounts/password-reset/done/', authViews.PasswordResetDoneView.as_view(
        template_name="registration/password_reset_done.html"), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(
        template_name="registration/password_reset_confirm.html"), name='password_reset_confirm'),
    path('accounts/password-reset/done/', authViews.PasswordResetCompleteView.as_view(
        template_name="registration/password_reset_complete.html"), name='password_reset_complete'),

]