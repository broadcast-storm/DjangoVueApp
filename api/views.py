from rest_framework import viewsets
from .serializers import JobPositionSerializer, DivisionSerializer, \
    UserProfileSerializer, StatisticsSerializer, TaskSerializer, TaskUserStatusSerializer, WeeklyTaskSerializer, \
    TeamSerializer
from .models import JobPosition, Division, Statistics, UserProfile, Task, WeeklyTask, TaskUserStatus, Team


class JobPositionViewSet(viewsets.ModelViewSet):
    serializer_class = JobPositionSerializer
    queryset = JobPosition.objects.all()


class DivisionViewSet(viewsets.ModelViewSet):
    serializer_class = DivisionSerializer
    queryset = Division.objects.all()


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()


class StatisticsViewSet(viewsets.ModelViewSet):
    serializer_class = StatisticsSerializer
    queryset = Statistics.objects.all()

class TeamsViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

class WeeklyTaskViewSet(viewsets.ModelViewSet):
    serializer_class = WeeklyTaskSerializer
    queryset = WeeklyTask.objects.all()


class TaskUserStatusViewSet(viewsets.ModelViewSet):
    serializer_class = TaskUserStatusSerializer
    queryset = TaskUserStatus.objects.all()
