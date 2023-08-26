from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.custom_login_view, name='login'),
    path('search_modify/', views.search_modify, name='search_modify'),
    path('modify_data/', views.modify_data, name='modify_data'),
    path('update_data/', views.update_data, name='update_data'),
    path('send_reminder_emails/', views.send_reminder_emails, name='send_reminder_emails'),
]

