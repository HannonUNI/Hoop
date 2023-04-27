from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('account/', views.accountManage,name='account'),
    path('account/register/', views.register,name='register'),
    path('contests/', views.contests,name='contests'),
    path('contests/<str:id>/', views.contests,name='contest'),
]

