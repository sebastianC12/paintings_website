from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='website-home'),
    path('about/', views.about, name='website-about'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name ='post-details'),
    path('post/create/', views.PostCreate.as_view(), name ='post-create'),
    path('post/<int:pk>//update', views.PostUpdate.as_view(), name ='post-update'),
    path('post/<int:pk>/delete/', views.PostDelete.as_view(), name ='post-delete')
]
