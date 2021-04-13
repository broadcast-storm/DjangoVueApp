from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobPositionViewSet, DivisionViewSet, UserProfileViewSet, StatisticsViewSet, \
    TaskViewSet, WeeklyTaskViewSet, TeamsViewSet, LogoutView, LogoutAllView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'job-positions', JobPositionViewSet)
router.register(r'divisions', DivisionViewSet)
router.register(r'users', UserProfileViewSet)
router.register(r'statistics', StatisticsViewSet)
router.register(r'teams', TeamsViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'weekly-tasks', WeeklyTaskViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('login', TokenObtainPairView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='auth_logout'),
    path('logout-all', LogoutAllView.as_view(), name='auth_logout_all'),
    path('refresh-token', TokenRefreshView.as_view(), name='refresh-token'),
    # path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('register/', RegisterView.as_view(), name='auth_register'),
    # path('change_password/<int:pk>/', ChangePasswordView.as_view(),
    #      name='auth_change_password'),
    # path('update_profile/<int:pk>/', UpdateProfileView.as_view(),
    #      name='auth_update_profile'),
]
