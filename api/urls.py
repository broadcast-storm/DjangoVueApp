from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobPositionViewSet, DivisionViewSet, UserProfileViewSet, StatisticsViewSet, \
    TaskViewSet, WeeklyTaskViewSet, TeamsViewSet, login, refresh_token, logout, competition, ProductViewSet, shop, \
    TestsViewSet, QuestionsViewSet, AnswersViewSet, TestBlockViewSet, AchievementViewSet, RequirenmentToGetAchieveViewSet, \
    AchieveRequirenmentStatusViewSet, AchievementUserStatusViewSet, update_user_money_energy, userFilterForCompetition

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
    path('user-filter-for-competitions', userFilterForCompetition, name='user-filter-for-competitions')

    # path('competition/currentcompetitions', currentcompetitions, name = 'currentcompetitions')
    # path('searchcompetitions')
]
