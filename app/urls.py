from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'upload', views.FileUploadViewSet, basename='upload')

urlpatterns = [
    path('', include(router.urls)),
    path('mylogin/', views.Login.as_view(), name='login')
]
