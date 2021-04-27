import jwt
import datetime
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework import exceptions
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken

from .serializers import JobPositionSerializer, DivisionSerializer, \
    UserProfileSerializer, StatisticsSerializer, TaskSerializer, TaskUserStatusSerializer, WeeklyTaskSerializer, \
    TeamSerializer
from .models import JobPosition, Division, Statistics, UserProfile, Task, WeeklyTask, TaskUserStatus, Team, Competition


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


class LogoutView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            token = RefreshToken(request.data["refresh_token"])
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class LogoutAllView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)

        return Response(status=status.HTTP_205_RESET_CONTENT)
