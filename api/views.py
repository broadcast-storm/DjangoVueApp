import jwt
import datetime
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework import exceptions
from django.conf import settings
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from .utils import generate_access_token, generate_refresh_token
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import JobPositionSerializer, DivisionSerializer, \
    UserProfileSerializer, StatisticsSerializer, TaskSerializer, TaskUserStatusSerializer, WeeklyTaskSerializer, \
    TeamSerializer, ProductSerializer, RequirementsToBuyProductSerializer, TestsSerializer, QuestionsSerializer, \
    AnswersSerializer, TestBlockSerializer, AchievementSerializer, RequirenmentToGetAchieveSerializer, AchieveRequirenmentStatusSerializer, \
    AchievementUserStatusSerializer, CompetitionSerializer, UserCompetitionSerializer, TestUserSerializer
from .models import JobPosition, Division, Statistics, UserProfile, Task, WeeklyTask, TaskUserStatus, Team, \
    Competition, Product, RequirementsToBuyProduct, Test, Question, Answer, TestBlock, Achievement, RequirenmentToGetAchieve, \
    AchieveRequirenmentStatus, AchievementUserStatus, Purchase, TestUser
from django.http import HttpResponse, JsonResponse


class JobPositionViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = JobPositionSerializer
    queryset = JobPosition.objects.all()


class DivisionViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = DivisionSerializer
    queryset = Division.objects.all()


class UserProfileViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()


@api_view(['GET', 'PUT'])
# For prod use IsAuthenticated . AllowAny using for Debug
@permission_classes([AllowAny])
@ensure_csrf_cookie
def update_user_money_energy(request):
    if request.method == 'GET':
        serializer = UserProfileSerializer(id=request.user.id)
        return Response(serializer.data)

    if request.method == 'PUT':
        user = UserProfile.objects.get(id=request.user.id)
        user.energy += request.data.get('energy')
        user.money += request.data.get('money')
        user.save()

        return Response(data="Done")
    #
    # if request.method == 'PUT':
    #     serializer = UserProfileSerializer(user, request.data)
    #     if serializer.is_valid():
    #         print(serializer.validated_data['password'])
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductViewSet(viewsets.ModelViewSet):
    # For prod use IsAuthenticated . AllowAny using for Debug
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer
    queryset = Product.objects.all().filter(count__gt=0)


class TestsViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = TestsSerializer
    queryset = Test.objects.all()


class TestUserViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = TestUserSerializer
    queryset = TestUser.objects.all()


class TestBlockViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = TestBlockSerializer
    queryset = TestBlock.objects.all()


class QuestionsViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = QuestionsSerializer
    queryset = Question.objects.all()


class AnswersViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = AnswersSerializer
    queryset = Answer.objects.all()


class AchievementViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = AchievementSerializer
    queryset = Achievement.objects.all()


class RequirenmentToGetAchieveViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = RequirenmentToGetAchieveSerializer
    queryset = RequirenmentToGetAchieve.objects.all()


class AchieveRequirenmentStatusViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = AchieveRequirenmentStatusSerializer
    queryset = AchieveRequirenmentStatus.objects.all()


class AchievementUserStatusViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = AchievementUserStatusSerializer
    queryset = AchievementUserStatus.objects.all()


@api_view(['GET'])
# For prod use IsAuthenticated . AllowAny using for Debug
@permission_classes([AllowAny])
@ensure_csrf_cookie
def userFilterForCompetition(request):
    if request.method == 'GET':
        users = UserProfile.objects.all().filter(level=request.data['level'])
        serializer = UserCompetitionSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET', 'PUT'])
# For prod use IsAuthenticated . AllowAny using for Debug
@permission_classes([AllowAny])
@ensure_csrf_cookie
def shop(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        products = RequirementsToBuyProduct.objects.all().prefetch_related('product')
        serializer = RequirementsToBuyProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)

    # TODO controll transactios
    if request.method == 'PUT':
        summary_cost = 0
        user = UserProfile.objects.get(id=request.user.id)
        products_req = RequirementsToBuyProduct.objects.filter(
            id__in=request.data.get('ids')).all().prefetch_related('product')
        for product_req in products_req:
            if product_req.product.count <= 0:
                return Response(data="Product out of stock")
            if product_req.level > user.level:
                return Response(data="You need higher level")
            summary_cost += product_req.money
            if summary_cost > user.money:
                return Response(data="You dont have money")
        user.money -= summary_cost
        user.save()
        products = Product.objects.all()
        p = Purchase(user=request.user)
        p.save()
        p.products.set(products)
        for product in products:
            product.count -= 1
            product.save()
        return Response(data="Done")


@api_view(['POST'])
@permission_classes([AllowAny])
@ensure_csrf_cookie
def login(request):
    user_model = get_user_model()
    username = request.data.get('username')
    password = request.data.get('password')
    response = Response()
    if (username is None) or (password is None):
        raise exceptions.AuthenticationFailed(
            'username and password required')

    user = user_model.objects.filter(username=username).first()
    if user is None:
        raise exceptions.AuthenticationFailed('user not found')
    if not user.check_password(password):
        raise exceptions.AuthenticationFailed('wrong password')

    serialized_user = UserProfileSerializer(user).data

    new_access_token = generate_access_token(user)
    new_refresh_token = generate_refresh_token(user)

    max_age = settings.REFRESH_TOKEN_EXPIRES * 24 * 60 * 60
    expires = datetime.datetime.strftime(
        datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
        "%a, %d-%b-%Y %H:%M:%S GMT",
    )

    response.set_cookie(key='refreshtoken', value=new_refresh_token, httponly=True, max_age=max_age,
                        expires=expires, )
    response.data = {
        'access_token': new_access_token,
        'user': serialized_user,
    }

    return response


@api_view(['POST'])
@permission_classes([AllowAny])
@ensure_csrf_cookie
def logout(request):
    response = Response()
    response.delete_cookie('refreshtoken')

    return response


@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_protect
def refresh_token(request):
    """
    To obtain a new access_token this view expects 2 important things:
        1. a cookie that contains a valid refresh_token
        2. a header 'X-CSRFTOKEN' with a valid csrf token, client app can get it from cookies "csrftoken"
    """
    user_model = get_user_model()
    req_refresh_token = request.COOKIES.get('refreshtoken')
    if refresh_token is None:
        raise exceptions.AuthenticationFailed(
            'Authentication credentials were not provided.')
    try:
        payload = jwt.decode(
            req_refresh_token, settings.REFRESH_TOKEN_SECRET, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise exceptions.AuthenticationFailed(
            'expired refresh token, please login again.')

    user = user_model.objects.filter(id=payload.get('user_id')).first()
    if user is None:
        raise exceptions.AuthenticationFailed('User not found')

    if not user.is_active:
        raise exceptions.AuthenticationFailed('user is inactive')

    access_token = generate_access_token(user)
    return Response({'access_token': access_token})


# Привязка страниц

def competition():
    return


def nameFunction():
    return


# /Привязка страниц


class StatisticsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = StatisticsSerializer
    queryset = Statistics.objects.all()


class TeamsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TeamSerializer
    queryset = Team.objects.all()


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class WeeklyTaskViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = WeeklyTaskSerializer
    queryset = WeeklyTask.objects.all()


class TaskUserStatusViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskUserStatusSerializer
    queryset = TaskUserStatus.objects.all()
