from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobPositionViewSet, DivisionViewSet, UserProfileViewSet, StatisticsViewSet, \
    TaskViewSet, WeeklyTaskViewSet, TeamsViewSet, login, refresh_token, logout, competition, ProductViewSet, shop, \
    TestsViewSet, TestUserViewSet, QuestionsViewSet, AnswersViewSet, TestBlockViewSet, AchievementViewSet, RequirenmentToGetAchieveViewSet, AchieveRequirenmentStatusViewSet, AchievementUserStatusViewSet, update_user_money_energy, unresolved_test

router = DefaultRouter()
router.register(r'job-positions', JobPositionViewSet)
router.register(r'divisions', DivisionViewSet)
router.register(r'users', UserProfileViewSet)
router.register(r'statistics', StatisticsViewSet)
router.register(r'teams', TeamsViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'weekly-tasks', WeeklyTaskViewSet)
router.register(r'products', ProductViewSet)
router.register(r'tests', TestsViewSet)
router.register(r'tests-user', TestUserViewSet)
router.register(r'questions', QuestionsViewSet)
router.register(r'answers', AnswersViewSet)
router.register(r'test-block', TestBlockViewSet)
router.register(r'achievement', AchievementViewSet)
router.register(r'requirenment-to-get-achieve',
                RequirenmentToGetAchieveViewSet)
router.register(r'achieve-requirenment-status',
                AchieveRequirenmentStatusViewSet)
router.register(r'achievement-user-status',
                AchievementUserStatusViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('login', login, name='login'),
    path('refresh-token', refresh_token, name='refresh-token'),
    path('shop', shop, name='shop'),
    path('update-data', update_user_money_energy, name='update-data'),
    path('logout', logout, name='logout'),
    path('competition', competition, name='competition'),
    path('unresolved_test', unresolved_test, name='unresolved_test')
    # path('competition/currentcompetitions', currentcompetitions, name = 'currentcompetitions')
    # path('searchcompetitions')
]
