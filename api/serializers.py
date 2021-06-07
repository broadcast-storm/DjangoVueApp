from rest_framework import serializers

from .models import CompetitionUser, JobPosition, Division, TestUser, UserProfile, Statistics, Task, TaskUserStatus, Team, Product, \
    RequirementsToBuyProduct, Test, Question, Answer, TestBlock, Achievement, RequirenmentToGetAchieve, AchieveRequirenmentStatus, AchievementUserStatus, QuestionTheme, Competition


class JobPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosition
        fields = ["id", "title", "description"]


class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = ["id", "title", "description"]


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['users', 'division', 'title', 'description',
                  'maxUsersCount', 'created_at', 'updated_at']


class WeeklyTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


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


class TestsWithoutUsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Test
        fields = ["id", "title", "description", "pointsToComplete", "canLeave", "canSkip", "showAnswers",
                  "isInterview", "canSeeSpentTime", "canSeeTestClosing", "created_at", "updated_at"]


class QuestionThemeSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionTheme
        fields = '__all__'


class QuestionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'


class TestBlockQuestionsSerializer(serializers.ModelSerializer):
    questions = QuestionsSerializer(many=True)

    class Meta:
        model = TestBlock
        fields = '__all__'


class TestBlockSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestBlock
        fields = '__all__'


class TestUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestUser
        fields = '__all__'


class AnswersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = '__all__'


class AnswersWithoutFlagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['id', 'text', 'description', 'image', 'question']


class AnswersIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['id', 'question']

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


class CompetitionUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompetitionUser
        fields = '__all__'
