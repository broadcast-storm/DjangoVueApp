from rest_framework import serializers
from .models import JobPosition, Division, UserProfile, Statistics, Task, TaskUserStatus, Team, Product, RequirementsToBuyProduct, Test


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
        fields = ['id', 'username', 'email', "name", "surname", "patronymic",
                  "jobPosition", "userType", "division",
                  "description", "photo", "level",
                  "money", "health", "energy",
                  "quality", "productivity",
                  "competitionCount", "winCompetitionCount"]


class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = ['user', 'level', 'quality', 'productivity', 'completedTests', 'completedTasks',
                  'completedQuests', 'achievements', 'competitions', 'competitionWins']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['taskType', 'parent', 'weekly', 'division', 'tags',  'title', 'description', 'subTasksCount', 'isTeamTask',
                  'accessLevel', 'deadline',
                  "money", "health", "energy",
                  'created_at', 'updated_at', 'tags']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['users', 'division', 'title', 'description',
                  'maxUsersCount', 'created_at', 'updated_at']


class WeeklyTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['division', 'difficulty', 'taskType', 'title', 'description', 'subTasksCount', 'isTeamTask',
                  "money", "health", "energy",
                  'created_at', 'updated_at', 'tags']


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


# class ShopSerializer(serializers.ModelSerializer):
#     product = ProductSerializer(read_only=True)

#     class Meta:
#         model = RequirementsToBuyProduct
#         fields = ['album_name', 'artist', 'tracks']
