from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'job-positions', views.JobPositionViewSet)
router.register(r'divisions', views.DivisionViewSet)
router.register(r'users', views.UserProfileViewSet)
router.register(r'statistics', views.StatisticsViewSet)
router.register(r'teams', views.TeamsViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'weekly-tasks', views.WeeklyTaskViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'tests', views.TestsViewSet)
router.register(r'tests-user', views.TestUserViewSet)
router.register(r'questions', views.QuestionsViewSet)
router.register(r'answers', views.AnswersViewSet)
router.register(r'test-block', views.TestBlockViewSet)
router.register(r'question-theme', views.QuestionThemeViewSet)
router.register(r'achievement', views.AchievementViewSet)
router.register(r'requirenment-to-get-achieve',
                views.RequirenmentToGetAchieveViewSet)
router.register(r'achieve-requirenment-status',
                views.AchieveRequirenmentStatusViewSet)
router.register(r'achievement-user-status',
                views.AchievementUserStatusViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path('login', TokenObtainPairView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='auth_logout'),
    path('logout-all', views.LogoutAllView.as_view(), name='auth_logout_all'),
    path('refresh-token', TokenRefreshView.as_view(), name='refresh-token'),
    path('shop', views.shop, name='shop'),
    path('update-data', views.update_user_money_energy, name='update-data'),
    path('unresolved_test', views.unresolved_test, name='unresolved_test'),
    path('test-questions', views.test_questions, name='test_questions'),
    path('test-post', views.test_post, name='test_post'),
    path('user-filter-for-competitions', views.userFilterForCompetition,
         name='user-filter-for-competitions'),
    path('get-quests', views.get_quests, name='get-quests'),
    path('get-daily-tasks', views.get_daily_tasks, name='get-daily-tasks'),
    path('get-weekly-tasks', views.get_weekly_tasks, name='get-weekly-tasks'),
    path('users-select', views.users_select, name='users_select'),
    path('competition-request', views.competition_request, name='competition_request'),
    path('start-competition', views.start_competition, name='start_competition'),
    path('competition', views.competition, name='competition')]


# path('competition/currentcompetitions', currentcompetitions, name = 'currentcompetitions')
# path('searchcompetitions')
