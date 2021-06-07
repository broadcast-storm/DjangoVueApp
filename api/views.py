import jwt
import datetime
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework import exceptions
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken

from .serializers import CompetitionUserSerializer, JobPositionSerializer, DivisionSerializer, \
    UserProfileSerializer, StatisticsSerializer, TaskSerializer, TaskUserStatusSerializer, WeeklyTaskSerializer, \
    TeamSerializer, ProductSerializer, RequirementsToBuyProductSerializer, TestsSerializer, QuestionsSerializer, \
    AnswersSerializer, TestBlockSerializer, AchievementSerializer, RequirenmentToGetAchieveSerializer, AchieveRequirenmentStatusSerializer, \
    AchievementUserStatusSerializer, CompetitionSerializer, UserCompetitionSerializer, TestUserSerializer, QuestionThemeSerializer, TestBlockQuestionsSerializer, AnswersWithoutFlagSerializer, AnswersIdSerializer, TestsWithoutUsersSerializer
from .models import JobPosition, Division, QuestionTheme, Statistics, UserProfile, Task, WeeklyTask, TaskUserStatus, Team, \
    Competition, Product, RequirementsToBuyProduct, Test, Question, Answer, TestBlock, Achievement, RequirenmentToGetAchieve, \
    AchieveRequirenmentStatus, AchievementUserStatus, Purchase, TestUser, CompetitionUser
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
    # serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()

    def get_permissions(self):
        if self.action == 'retrieve' or self.action == 'update':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'list':
            return UserGetListSerializer
        elif self.action == 'retrieve':
            return UserGetSerializer
        elif self.action == 'update':
            return UserProfileSerializer
        else:
            return EmptySerializer


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


class CompetitionViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = CompetitionSerializer
    queryset = Competition.objects.all()


class CompetitionUserDetailView(APIView):
    def patch(self, request, pk, *args, **kwargs):
        competition = CompetitionUser.objects.get(id=pk)
        competition.isCompleted = True
        competition.winner = request.data['winner']
        competition.save()
        return competition


class CompetitionUserViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = CompetitionUserSerializer
    queryset = CompetitionUser.objects.all()


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
def unresolved_test(request):
    """
    List all code snippets, or create a new snippet.
    """
    ##################
    # serializer без user
    ##################
    if request.method == 'GET':
        tests = Test.objects.exclude(users=request.user.id).all()
        serializer = TestsWithoutUsersSerializer(tests, many=True)
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
        question_choice_id = []
        question_without_choice_id = []
        # all_data это массив первый элемент которого тестблок внутри которого вопросы второй элемент массива это ответы
        all_data = []
        test_block = TestBlock.objects.filter(
            test=request.data.get('test_id')).all()
        serializer = TestBlockQuestionsSerializer(test_block, many=True)
        # заполняем массив question_id айдишниками вопросов в нужном тесте (через каждый test_block)
        # Не отправляет ответы для вопросов с вводом текста и числа
        for item in serializer.data:
            for item2 in item['questions']:
                if item2["answerType"] == "one_choice" or item2["answerType"] == "multi_choice":
                    question_choice_id.append(item2["id"])
                else:
                    question_without_choice_id.append(item2["id"])

        answers_choice = Answer.objects.filter(
            question__in=question_choice_id).all()
        answers_without_choice = Answer.objects.filter(
            question__in=question_without_choice_id).all()
        serializer2 = AnswersWithoutFlagSerializer(answers_choice, many=True)
        serializer3 = AnswersIdSerializer(answers_without_choice, many=True)
        all_data = (serializer.data, serializer2.data, serializer3.data)
        return JsonResponse(all_data, safe=False)


@ api_view(['POST'])
# For prod use IsAuthenticated . AllowAny using for Debug
@ permission_classes([AllowAny])
# @ensure_csrf_cookie
def test_post(request):
    """
    List all code snippets, or create a new snippet.
    """
    # TODO controll transactios
    if request.method == 'POST':
        user = UserProfile.objects.get(id=request.user.id)
        right_answers = 0
        wrong_answers = 0
        true_questions_simple = []
        false_questions_simple = []
        true_questions_multi = []
        false_questions_multi = []
        true_questions_text = []
        false_questions_text = []
        test = Test.objects.get(
            id=request.data.get("test_id"))
        status = ''
        points_to_complete = test.pointsToComplete
        print(points_to_complete)

        ######################
        # SIMPLE QUESTION
        # ###############
        request_answers_simple = request.data.get("answers_simple")
        if request_answers_simple:
            answers_simple = Answer.objects.filter(
                id__in=request_answers_simple).values("isCorrect", "question")
            for answer_simple in answers_simple:
                if answer_simple.get("isCorrect"):
                    true_questions_simple.append(
                        answer_simple.get("question"))
                    right_answers += 1
                else:
                    false_questions_simple.append(
                        answer_simple.get("question"))
                    wrong_answers += 1
            print(true_questions_simple)

        ######################
        # MULTI QUESTION
        # ###############
        request_answers_multi = request.data.get("answers_multi")
        if request_answers_multi:
            request_answers_multi_questions = [
                a.get("question_id") for a in request_answers_multi
            ]
            true_answers_multi = Answer.objects.filter(
                question__in=request_answers_multi_questions).filter(isCorrect=True).values("id", "isCorrect", "question")
            print("true multi")
            print(true_answers_multi)
            print("Req multi")
            print(request_answers_multi)
            for request_answer_multi in request_answers_multi:
                true_answers_array = []
                for true_answer_multi in true_answers_multi:
                    if true_answer_multi.get("question") == request_answer_multi.get("question_id"):
                        true_answers_array.append(
                            str(true_answer_multi.get("id")))
                if true_answers_array == request_answer_multi.get("answer_id"):
                    true_questions_multi.append(
                        request_answer_multi.get("question_id"))
                    right_answers += 1
                else:
                    false_questions_multi.append(
                        request_answer_multi.get("question_id"))
                    wrong_answers += 1
                true_answers_array.clear()
            print(true_questions_multi)

        ######################
        # TEXT QUESTION
        # ###############
        request_answers_text = request.data.get("answers_text")
        print("req text")
        print(request_answers_text)
        if request_answers_text:
            request_answers_text_questions = [
                a.get("question_id") for a in request_answers_text
            ]
            print("request_answers_text_questions")
            print(request_answers_text_questions)
            true_answers_text = Answer.objects.filter(
                question__in=request_answers_text_questions).filter(isCorrect=True).values("id", "isCorrect", "question", "text")
            for request_answer_text in request_answers_text:
                true_answer = None
                for true_answer_text in true_answers_text:
                    if true_answer_text.get("question") == request_answer_text.get("question_id"):
                        true_answer = str(true_answer_text.get("text"))
                print(true_answer + '  ' +
                      str(request_answer_text.get("answer_text")))
                if true_answer == str(request_answer_text.get("answer_text")):
                    true_questions_text.append(
                        request_answer_text.get("question_id"))
                    right_answers += 1
                else:
                    false_questions_text.append(
                        request_answer_text.get("question_id"))
                    wrong_answers += 1
                true_answer = None
            print("Text true")
            print(true_answers_text)
            print(true_questions_text)

        print(right_answers)

        if points_to_complete <= right_answers:
            status = "Выполнен"
        else:
            status = "Провален"

        testUser = TestUser(test=test, user=user, status=status,
                            rightAnswersCount=right_answers, points=right_answers)
        testUser.save()
        print(testUser)
        for true_question_simple in true_questions_simple:
            testUserAnswer = TestUserAnswer(
                testUser=testUser, question_id=true_question_simple, isCorrect=True)
            testUserAnswer.save()
        for false_question_simple in false_questions_simple:
            testUserAnswer = TestUserAnswer(
                testUser=testUser, question_id=false_question_simple, isCorrect=False)
            testUserAnswer.save()
        for true_question_multi in true_questions_multi:
            testUserAnswer = TestUserAnswer(
                testUser=testUser, question_id=true_question_multi, isCorrect=True)
            testUserAnswer.save()
        for false_question_multi in false_questions_multi:
            testUserAnswer = TestUserAnswer(
                testUser=testUser, question_id=false_question_multi, isCorrect=False)
            testUserAnswer.save()
        for true_question_text in true_questions_text:
            testUserAnswer = TestUserAnswer(
                testUser=testUser, question_id=true_question_text, isCorrect=True)
            testUserAnswer.save()
        for false_question_text in false_questions_text:
            testUserAnswer = TestUserAnswer(
                testUser=testUser, question_id=false_question_text, isCorrect=False)
            testUserAnswer.save()

        user.money += right_answers*2000
        user.energy += right_answers*10000
        user.save()
        response = {
            "money": right_answers*2000,
            "energy": right_answers*10000,
            "right_answers": right_answers,
            "total_questions": right_answers+wrong_answers
        }
        return Response(data=response)


@ api_view(['GET', 'PUT'])
# For prod use IsAuthenticated . AllowAny using for Debug
@ permission_classes([AllowAny])
# @ensure_csrf_cookie
def shop(request):
    """
    List all code snippets, or create a new snippet.
    """
    # Выводит товары которые есть в наличии и их стоимость
    if request.method == 'GET':
        products = RequirementsToBuyProduct.objects.filter(
            product__count=1).all().prefetch_related('product')
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


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_daily_tasks(request):
    if request.method == 'GET':
        user = UserProfile.objects.get(id=request.user.id)
        tasks = Task.objects.all().filter(taskType="daily").exclude(
            ~Q(parent=None)).exclude(
            ~Q(weekly=None)).filter(division=user.division)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_weekly_tasks(request):
    if request.method == 'GET':
        user = UserProfile.objects.get(id=request.user.id)
        weeklyTasks = WeeklyTask.objects.all().filter(division=user.division)
        serializer = WeeklyTaskSerializer(weeklyTasks, many=True)
        for weeklyTask in serializer.data:
            subTasks = Task.objects.all().filter(weekly=weeklyTask['id'])
            subSerializer = TaskSerializer(subTasks, many=True)
            weeklyTask['subTasks'] = subSerializer.data
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_quests(request):
    if request.method == 'GET':

        user = UserProfile.objects.get(id=request.user.id)
        quests = Task.objects.all().filter(taskType="quest").exclude(
            ~Q(parent=None)).exclude(
            ~Q(weekly=None)).filter(division=user.division)
        serializer = TaskSerializer(quests, many=True)
        for quest in serializer.data:
            subTasks = Task.objects.all().filter(parent=quest['id'])
            subSerializer = TaskSerializer(subTasks, many=True)
            quest['subTasks'] = subSerializer.data
        return Response(serializer.data)


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
