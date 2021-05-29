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
    TeamSerializer, ProductSerializer, RequirementsToBuyProductSerializer, TestsSerializer, QuestionsSerializer, \
    AnswersSerializer, TestBlockSerializer, AchievementSerializer, RequirenmentToGetAchieveSerializer, AchieveRequirenmentStatusSerializer, \
    AchievementUserStatusSerializer, CompetitionSerializer, UserCompetitionSerializer, TestUserSerializer, QuestionThemeSerializer, TestBlockQuestionsSerializer
from .models import JobPosition, Division, QuestionTheme, Statistics, UserProfile, Task, WeeklyTask, TaskUserStatus, Team, \
    Competition, Product, RequirementsToBuyProduct, Test, Question, Answer, TestBlock, Achievement, RequirenmentToGetAchieve, \
    AchieveRequirenmentStatus, AchievementUserStatus, Purchase, TestUser
from django.http import HttpResponse, JsonResponse


class JobPositionViewSet(viewsets.ModelViewSet):
    serializer_class = JobPositionSerializer
    queryset = JobPosition.objects.all()


class DivisionViewSet(viewsets.ModelViewSet):
    serializer_class = DivisionSerializer
    queryset = Division.objects.all()


class QuestionThemeViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = QuestionThemeSerializer
    queryset = QuestionTheme.objects.all()


class UserProfileViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = UserProfile.objects.all()


@api_view(['GET', 'PUT'])
# For prod use IsAuthenticated . AllowAny using for Debug
@permission_classes([AllowAny])
# @ensure_csrf_cookie
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
# @ensure_csrf_cookie
def userFilterForCompetition(request):
    if request.method == 'GET':
        tests = Test.objects.exclude(users=request.user.id).all()
        serializer = TestsSerializer(tests, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
# For prod use IsAuthenticated . AllowAny using for Debug
@permission_classes([AllowAny])
# @ensure_csrf_cookie
def test_questions(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        testblock = Question.objects.filter(
            qst__id=1).all().prefetch_related().values()
        tst = TestBlock.objects.values("questions__qwe__id", "questions").all()
        print(tst.query)
        # print(testblock.query)
        # print(Question.objects.filter(qst__id=1).all().prefetch_related().query)
        # products_req = RequirementsToBuyProduct.objects.filter(
        #     id__in=request.data.get('ids')).all().prefetch_related('product')
        # tests = Test.objects.exclude(users=request.user.id).all()

        serializer = TestBlockQuestionsSerializer(tst, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET', 'PUT'])
# For prod use IsAuthenticated . AllowAny using for Debug
@permission_classes([AllowAny])
# @ensure_csrf_cookie
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


# Привязка страниц

def competition():
    return


def nameFunction():
    return


# /Привязка страниц

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
