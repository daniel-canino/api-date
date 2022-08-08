from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user_api import views

router = DefaultRouter()

router.register('user', views.CreateUserProfileViewSet)
router.register('historial', views.GetUserVieSet)

urlpatterns = [
    path('user/', include(router.urls)),
    path('', views.UserLoginApiView.as_view() ),
    path('date/', views.CalculateDateApiView.as_view()),
]