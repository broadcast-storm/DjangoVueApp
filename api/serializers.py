from rest_framework import serializers
from .models import JobPosition, Division, UserProfile, Statistics, Task, TaskUserStatus, Team, Product, \
    RequirementsToBuyProduct, Test, Question, Answer, TestBlock, Achievement, RequirenmentToGetAchieve, AchieveRequirenmentStatus,\
    AchievementUserStatus, Competition, WeeklyTask
from .models import JobPosition, Division, TestUser, UserProfile, Statistics, Task, TaskUserStatus, Team, Product, \
    RequirementsToBuyProduct, Test, Question, Answer, TestBlock, Achievement, RequirenmentToGetAchieve, AchieveRequirenmentStatus, AchievementUserStatus


class EmptySerializer(serializers.Serializer):
    pass


class JobPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosition
        fields = ["id", "title", "description"]


class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = ["id", "title", "description"]

# ============================================
# ПОЛЬЗОВАТЕЛИ
# ============================================


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserGetSerializer(serializers.ModelSerializer):
    division_details = DivisionSerializer(source="division")

    class Meta:
        model = UserProfile
        fields = ["id", "email", "username", "name", "userType", "surname", "patronymic",
                  "birthDate", "description", "photo", "level", "money", "health", "energy", "quality",
                  "productivity", "competitionCount", "winCompetitionCount", "jobPosition", "division_details",
                  "userType"]


class UserGetListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["id", "username", "name", "userType", "surname",
                  "birthDate", "photo", "level", "quality",
                  "productivity",  "jobPosition", "division", "userType"]


class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['users', 'division', 'title', 'description',
                  'maxUsersCount', 'created_at', 'updated_at']


class WeeklyTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyTask
        fields = ["id", "difficulty", "title", "description",
                  "subTasksCount", "isTeamTask", "accessLevel", "deadline",
                  "money",  "health", "energy", "division", ]


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "difficulty", "taskType", "title", "description",
                  "subTasksCount", "isTeamTask", "accessLevel", "deadline",
                  "money",  "health", "energy", "division", ]


class TaskUserStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskUserStatus
        fields = ['task', 'user',
                  'subTasksCount', 'subTasksCompletedCount', 'status'
                                                             'started_at', 'done_at']


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class RequirementsToBuyProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = RequirementsToBuyProduct
        fields = '__all__'


class TestsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Test
        fields = '__all__'


class TestBlockSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestBlock
        fields = '__all__'


class TestUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestUser
        fields = '__all__'


class TestUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestUser
        fields = '__all__'


class QuestionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'


class AnswersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = '__all__'


# class ShopSerializer(serializers.ModelSerializer):
#     product = ProductSerializer(read_only=True)

#     class Meta:
#         model = RequirementsToBuyProduct
#         fields = ['album_name', 'artist', 'tracks']


class AchievementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Achievement
        fields = '__all__'


class RequirenmentToGetAchieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = RequirenmentToGetAchieve
        fields = '__all__'


class AchieveRequirenmentStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = AchieveRequirenmentStatus
        fields = '__all__'


class AchievementUserStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = AchievementUserStatus
        fields = '__all__'


class UserCompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'name', 'surname',
                  'productivity', 'quality', 'level', 'photo']


class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = '__all__'
