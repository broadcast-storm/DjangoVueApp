from rest_framework import serializers
from . import models


class EmptySerializer(serializers.Serializer):
    pass


class JobPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JobPosition
        fields = ["id", "title", "description"]


class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Division
        fields = ["id", "title", "description"]

# ============================================
# ПОЛЬЗОВАТЕЛИ
# ============================================


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = '__all__'


class UserGetSerializer(serializers.ModelSerializer):
    division_details = DivisionSerializer(source="division")

    class Meta:
        model = models.UserProfile
        fields = ["id", "email", "username", "name", "userType", "surname", "patronymic",
                  "birthDate", "description", "photo", "level", "money", "health", "energy", "quality",
                  "productivity", "competitionCount", "winCompetitionCount", "jobPosition", "division_details",
                  "userType"]


class UserGetListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ["id", "username", "name", "userType", "surname",
                  "birthDate", "photo", "level", "quality",
                  "productivity",  "jobPosition", "division", "userType"]


class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Statistics
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Team
        fields = ['users', 'division', 'title', 'description',
                  'maxUsersCount', 'created_at', 'updated_at']


class WeeklyTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WeeklyTask
        fields = ["id", "difficulty", "title", "description",
                  "subTasksCount", "isTeamTask", "accessLevel", "deadline",
                  "money",  "health", "energy", "division", ]


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = ["id", "difficulty", "taskType", "title", "description",
                  "subTasksCount", "isTeamTask", "accessLevel", "deadline",
                  "money",  "health", "energy", "division", ]


class QuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MainQuest
        fields = ["id", "tasks", "difficulty", "title", "description",
                  "accessLevel", "money", "health", "energy", "is_active", "time_left"]


class QuestTreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MainQuestTree
        fields = ["id", "mainQuest", "task", "parentTask"]


class TaskUserStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TaskUserStatus
        fields = ['task', 'user',
                  'subTasksCount', 'subTasksCompletedCount', 'status'
                                                             'started_at', 'done_at']


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = '__all__'


class RequirementsToBuyProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = models.RequirementsToBuyProduct
        fields = '__all__'


class TestsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Test
        fields = '__all__'


class TestsWithoutUsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Test
        fields = ["id", "title", "description", "pointsToComplete", "canLeave", "canSkip", "showAnswers",
                  "isInterview", "canSeeSpentTime", "canSeeTestClosing", "created_at", "updated_at"]


class QuestionThemeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.QuestionTheme
        fields = '__all__'


class QuestionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Question
        fields = '__all__'


class TestBlockQuestionsSerializer(serializers.ModelSerializer):
    questions = QuestionsSerializer(many=True)

    class Meta:
        model = models.TestBlock
        fields = '__all__'


class TestBlockSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TestBlock
        fields = '__all__'


class TestUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TestUser
        fields = '__all__'


class AnswersSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Answer
        fields = '__all__'


class AnswersWithoutFlagSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Answer
        fields = ['id', 'text', 'description', 'image', 'question']


class AnswersIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Answer
        fields = ['id', 'question']

# class ShopSerializer(serializers.ModelSerializer):
#     product = ProductSerializer(read_only=True)

#     class Meta:
#         model = RequirementsToBuyProduct
#         fields = ['album_name', 'artist', 'tracks']


class AchievementSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Achievement
        fields = '__all__'


class RequirenmentToGetAchieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.RequirenmentToGetAchieve
        fields = '__all__'


class AchieveRequirenmentStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.AchieveRequirenmentStatus
        fields = '__all__'


class AchievementUserStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.AchievementUserStatus
        fields = '__all__'


class UserCompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ['id', 'username', 'name', 'surname',
                  'productivity', 'quality', 'level', 'photo']


class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Competition
        fields = '__all__'
