import jwt
from datetime import datetime

from django.utils.timezone import make_aware

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

from . import serializers

from . import models

from django.http import HttpResponse, JsonResponse


class JobPositionViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.JobPositionSerializer
    queryset = models.JobPosition.objects.all()


class DivisionViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DivisionSerializer
    queryset = models.Division.objects.all()


class QuestionThemeViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = serializers.QuestionThemeSerializer
    queryset = models.QuestionTheme.objects.all()


class UserProfileViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

    def get_permissions(self):
        if self.action == 'retrieve' or self.action == 'update':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.UserGetListSerializer
        elif self.action == 'retrieve':
            return serializers.UserGetSerializer
        elif self.action == 'update':
            return serializers.UserProfileSerializer
        else:
            return serializers.EmptySerializer


@api_view(['GET', 'PUT'])
# For prod use IsAuthenticated . AllowAny using for Debug
@permission_classes([AllowAny])
# @ensure_csrf_cookie
def update_user_money_energy(request):
    if request.method == 'GET':
        serializer = serializers.UserProfileSerializer(id=request.user.id)
        return Response(serializer.data)

    if request.method == 'PUT':
        user = models.UserProfile.objects.get(id=request.user.id)
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
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all().filter(count__gt=0)


class TestsViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = serializers.TestsSerializer
    queryset = models.Test.objects.all()


class TestUserViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = serializers.TestUserSerializer
    queryset = models.TestUser.objects.all()


class TestBlockViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = serializers.TestBlockSerializer
    queryset = models.TestBlock.objects.all()


class QuestionsViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = serializers.QuestionsSerializer
    queryset = models.Question.objects.all()


class AnswersViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = serializers.AnswersSerializer
    queryset = models.Answer.objects.all()


class AchievementViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.AchievementSerializer
    queryset = models.Achievement.objects.all()


class RequirenmentToGetAchieveViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = serializers.RequirenmentToGetAchieveSerializer
    queryset = models.RequirenmentToGetAchieve.objects.all()


class AchieveRequirenmentStatusViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = serializers.AchieveRequirenmentStatusSerializer
    queryset = models.AchieveRequirenmentStatus.objects.all()


class AchievementUserStatusViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = serializers.AchievementUserStatusSerializer
    queryset = models.AchievementUserStatus.objects.all()


@api_view(['GET'])
# For prod use IsAuthenticated . AllowAny using for Debug
@permission_classes([AllowAny])
# @ensure_csrf_cookie
def competition_possible_enemies(request):
    if request.user.id is None:
        return Response(data="You should be authorized")
    # получаем уровень пользователя
    user_level = models.UserProfile.objects.get(id=request.user.id).level
    # находим пользователей у которых уровень отличен на +-3 и исключаем пользователя, запрашивающего данные
    possible_enemies = models.UserProfile.objects.filter(level__range=[user_level-3, user_level+3]).exclude(id=request.user.id)
    data = serializers.UserProfileSerializer(possible_enemies, many=True).data
    return Response(data)


@api_view(['GET'])
# For prod use IsAuthenticated . AllowAny using for Debug
@permission_classes([AllowAny])
# @ensure_csrf_cookie
def competition_user_data(request):
    if request.user.id is None:
        return Response(data="You should be authorized")
    # находим пользователя по id
    user = models.UserProfile.objects.get(id=request.user.id)
    data = serializers.UserProfileForCompetitionSerializer(user).data
    return Response(data)


@api_view(['POST', 'GET'])
# For prod use IsAuthenticated . AllowAny using for Debug
@permission_classes([AllowAny])
# @ensure_csrf_cookie
def competition_request(request):
    """
    Get запрос возвращает все соревнования

    Post создает запись в таблице CompetitionRequest. Возвращает строку "done" если все хорошо, либо строку с ошибкой
    Требует receiver_id в body- id человека которому отправляют запрос
    Требует title в body - название соревнования
    """
    if request.method == 'GET':
        cr = models.CompetitionRequest.objects.all()
        serializer = serializers.CompetitionRequestSerializer(cr, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        if request.data.get("receiver_id") is None:
            return Response(data="Please give receiver id in body")
        if request.user.id is None:
            return Response(data="You should be authorized")
        if request.data.get("receiver_id") == request.user.id:
            return Response(data="You can't create competition for yourself")
        if request.data.get("title") is None:
            return Response(data="Please give title in body")
        # получаем отправителя и получателя
        sender = models.UserProfile.objects.get(id=request.user.id)
        receiver = models.UserProfile.objects.get(id=request.data.get("receiver_id"))
        # создаем запрос на соревнование
        cr = models.CompetitionRequest(sender=sender, receiver=receiver, title=request.data.get("title"))
        cr.save()
        # создаем уведомление получателю
        un = models.UserNotification(user=receiver, message="У вас есть новый запрос на соревнование",
                                     title="Соревнования")
        un.save()
        return Response(data="Done")


@api_view(['POST'])
# For prod use IsAuthenticated . AllowAny using for Debug
@permission_classes([AllowAny])
# @ensure_csrf_cookie
def start_competition(request):
    """
    Post создает запись в таблице Competition, меняет статус в таблице CompetitionRequest.
    Возвращает строку "done" если все хорошо, либо строку с ошибкой
    Требует receiver_answer в body, Значения могут быть: "ACCEPTED", "DISCARDED" - ответ пользователя
    Требует competition_id в body - id соревнования
    Требует notification_id в body - id уведомления
    """
    if request.method == 'POST':
        if request.data.get("receiver_answer") is None:
            return Response(data="Please give receiver answer in body")
        if request.data.get("competition_id") is None:
            return Response(data="Please give competition id in body")
        ##########
        # на случай если дедлайн можно будет двигать. По дефолту дедлайн после принятия 30 дней
        # if request.data.get("deadline") is None:
        #     return Response(data="Please give deadline in unix timestamp in body")
        # deadline = make_aware(datetime.fromtimestamp(request.data.get("deadline")))
        ##########
        # берем наш запрос на соревнования и меняем его статус
        cr = models.CompetitionRequest.objects.get(id=request.data.get("competition_id"))
        cr.status = request.data.get("receiver_answer")
        cr.save()
        # создет соревнование если приняли CompetitionRequest
        if request.data.get("receiver_answer") == "ACCEPTED":
            c = models.Competition(request=cr)
            c.save()
        return Response(data="done")


@api_view(['GET','POST'])
# For prod use IsAuthenticated . AllowAny using for Debug
@permission_classes([AllowAny])
# @ensure_csrf_cookie
def notification(request):
    """
    Get запрос возвращает все непросмотренные уведомления у текущего пользователя

    Post меняет статус в таблице UserNotification.
    Возвращает строку "done" если все хорошо, либо строку с ошибкой
    Требует notification_id в body - id уведомления
    """
    if request.method == 'GET':
        user = models.UserProfile.objects.get(id=request.user.id)
        un = models.UserNotification.objects.filter(user=user, status="NOT VIEWED").all()
        serializer = serializers.UserNotificationSerializer(un, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        if request.data.get("notification_id") is None:
            return Response(data="Please give notification id in body")
        # Меняем статус уведомления
        un = models.UserNotification.objects.get(id=request.data.get("notification_id"))
        un.status = "VIEWED"
        un.save()
        return Response(data="done")


@api_view(['GET'])
# For prod use IsAuthenticated . AllowAny using for Debug
@permission_classes([AllowAny])
# @ensure_csrf_cookie
def competition(request):
    """
    Get запрос возвращает все соревнования
    """
    if request.method == 'GET':
        c = models.Competition.objects.all()
        serializer = serializers.CompetitionSerializer(c, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
# For prod use IsAuthenticated . AllowAny using for Debug
@permission_classes([AllowAny])
# @ensure_csrf_cookie
def userFilterForCompetition(request):
    # ??????????????????????????????????????????????????????????
    # Возвращает все тесты которые не решил текущий пользователь????????????
    # ??????????????????????????????????????????????????????????
    if request.method == 'GET':
        tests = models.Test.objects.exclude(users=request.user.id).all()
        serializer = serializers.TestsSerializer(tests, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
# For prod use IsAuthenticated . AllowAny using for Debug
@permission_classes([AllowAny])
# @ensure_csrf_cookie
def unresolved_test(request):
    """
    Get запрос возвращает все тесты без пользователей
    """
    ##################
    # serializer без user
    ##################
    if request.method == 'GET':
        tests = models.Test.objects.exclude(users=request.user.id).all()
        serializer = serializers.TestsWithoutUsersSerializer(tests, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
# For prod use IsAuthenticated . AllowAny using for Debug
@permission_classes([AllowAny])
# @ensure_csrf_cookie
def users_select(request):
    """
    Поиск будет case sensetive будут искаться подстроки в строке
    Get запрос возвращает 10 пользователей
    Возможна фильтрация по имени, необходимо передать name
    После передачи имени можно передать фамилию surname
    """
    if request.method == 'GET':
        if request.data.get('name', '') and request.data.get('surname', ''):
            # user = UserProfile.objects.filter(name__icontains=request.data.get('name'), surname__icontains=request.data.get('surname')).order_by('-rating').all()[:10]
            user = models.UserProfile.objects.exclude(id=request.user.id).filter(
                name__icontains=request.data.get('name'),
                surname__icontains=request.data.get('surname')).all()[:10]
        elif request.data.get('name', ''):
            user = models.UserProfile.objects.exclude(id=request.user.id).filter(
                name__contains=request.data.get('name')).all()[:10]
            # user = UserProfile.objects.filter(name__icontains=request.data.get('name')).order_by('-rating').all()[:10]
        else:
            user = models.UserProfile.objects.exclude(id=request.user.id).all()[:10]
            # user = UserProfile.objects.order_by('-rating').all()[:10]
        serializer = serializers.UserCompetitionSerializer(user, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
# For prod use IsAuthenticated . AllowAny using for Debug
@permission_classes([IsAuthenticated, ])
# @ensure_csrf_cookie
def test_questions(request):
    """
    Возвращает впоросы у определенного теста и ответы без подсвечивания правильного, если вопросы без вариантов ответа,
    тогда ответ не отправяется. требует переменную test_id в которую нужно записать id у теста
    """
    if request.method == 'GET':
        question_choice_id = []
        question_without_choice_id = []
        # all_data это массив первый элемент которого тестблок внутри которого вопросы второй элемент массива это ответы
        all_data = []
        test_block = models.TestBlock.objects.filter(
            test_id=request.query_params.get('test_id')).all()
        test_info = models.Test.objects.get(
            id=request.query_params.get('test_id'))

        serializer_test = serializers.TestsWithoutUsersSerializer(test_info, many=False)

        serializer = serializers.TestBlockQuestionsSerializer(test_block, many=True)
        # заполняем массив question_id айдишниками вопросов в нужном тесте (через каждый test_block)
        # Не отправляет ответы для вопросов с вводом текста и числа
        for item in serializer.data:
            for item2 in item['questions']:
                if item2["answerType"] == "one_choice" or item2["answerType"] == "multi_choice":
                    question_choice_id.append(item2["id"])
                else:
                    question_without_choice_id.append(item2["id"])

        answers_choice = models.Answer.objects.filter(
            question__in=question_choice_id).all()
        answers_without_choice = models.Answer.objects.filter(
            question__in=question_without_choice_id).all()
        serializer2 = serializers.AnswersWithoutFlagSerializer(answers_choice, many=True)
        serializer3 = serializers.AnswersIdSerializer(answers_without_choice, many=True)
        all_data = {'testBlocks': serializer.data, 'answerOptions': serializer2.data, 'answerIds': serializer3.data,
                    'testInfo': serializer_test.data}
        return JsonResponse(all_data, safe=False)


@api_view(['POST'])
# For prod use IsAuthenticated . AllowAny using for Debug
@permission_classes([IsAuthenticated, ])
# @ensure_csrf_cookie
def test_post(request):
    """
    Post запрос который завершает тест, засчитывает ответы, добавляет выигранные деньги, энергию
    Требует answers_simple список c id ответов
    Требует answers_multi список списков с id ответов
    Требует answers_text текстовый ответ
    """
    # TODO controll transactios
    if request.method == 'POST':
        user = models.UserProfile.objects.get(id=request.user.id)
        right_answers = 0
        wrong_answers = 0
        true_questions_simple = []
        false_questions_simple = []
        true_questions_multi = []
        false_questions_multi = []
        true_questions_text = []
        false_questions_text = []
        test = models.Test.objects.get(
            id=request.data.get("test_id"))
        status = ''
        points_to_complete = test.pointsToComplete
        print(points_to_complete)  # это ещё нужно?

        ######################
        # SIMPLE QUESTION
        # ###############
        request_answers_simple = request.data.get("answers_simple")
        if request_answers_simple:
            answers_simple = models.Answer.objects.filter(
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
            true_answers_multi = models.Answer.objects.filter(
                question__in=request_answers_multi_questions).filter(isCorrect=True).values("id", "isCorrect",
                                                                                            "question")
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

        ######################
        # TEXT QUESTION
        # ###############
        request_answers_text = request.data.get("answers_text")
        if request_answers_text:
            request_answers_text_questions = [
                a.get("question_id") for a in request_answers_text
            ]
            true_answers_text = models.Answer.objects.filter(
                question__in=request_answers_text_questions).filter(isCorrect=True).values("id", "isCorrect",
                                                                                           "question", "text")
            for request_answer_text in request_answers_text:
                true_answer = None
                for true_answer_text in true_answers_text:
                    if true_answer_text.get("question") == request_answer_text.get("question_id"):
                        true_answer = str(true_answer_text.get("text"))
                if true_answer == str(request_answer_text.get("answer_text")):
                    true_questions_text.append(
                        request_answer_text.get("question_id"))
                    right_answers += 1
                else:
                    false_questions_text.append(
                        request_answer_text.get("question_id"))
                    wrong_answers += 1
                true_answer = None
        if points_to_complete <= right_answers:
            status = "Выполнен"
        else:
            status = "Провален"

        testUser = models.TestUser(test=test, user=user, status=status,
                                   rightAnswersCount=right_answers, points=right_answers)
        testUser.save()
        for true_question_simple in true_questions_simple:
            testUserAnswer = models.TestUserAnswer(
                testUser=testUser, question_id=true_question_simple, isCorrect=True)
            testUserAnswer.save()
        for false_question_simple in false_questions_simple:
            testUserAnswer = models.TestUserAnswer(
                testUser=testUser, question_id=false_question_simple, isCorrect=False)
            testUserAnswer.save()
        for true_question_multi in true_questions_multi:
            testUserAnswer = models.TestUserAnswer(
                testUser=testUser, question_id=true_question_multi, isCorrect=True)
            testUserAnswer.save()
        for false_question_multi in false_questions_multi:
            testUserAnswer = models.TestUserAnswer(
                testUser=testUser, question_id=false_question_multi, isCorrect=False)
            testUserAnswer.save()
        for true_question_text in true_questions_text:
            testUserAnswer = models.TestUserAnswer(
                testUser=testUser, question_id=true_question_text, isCorrect=True)
            testUserAnswer.save()
        for false_question_text in false_questions_text:
            testUserAnswer = models.TestUserAnswer(
                testUser=testUser, question_id=false_question_text, isCorrect=False)
            testUserAnswer.save()

        user.money += right_answers * 2000
        user.energy += right_answers * 10000
        user.save()
        response = {
            "money": right_answers * 2000,
            "energy": right_answers * 10000,
            "right_answers": right_answers,
            "total_questions": right_answers + wrong_answers,
            "status": status
        }
        return Response(data=response)


@api_view(['GET', 'PUT'])
# For prod use IsAuthenticated . AllowAny using for Debug
@permission_classes([IsAuthenticated, ])
# @ensure_csrf_cookie
def shop(request):
    """
    GET запрос - выводит товары которые есть в наличии и их стоимость
    POST запрос требует переменную массив ids в которой прописаны id товаров на покупку
    """
    # Выводит товары которые есть в наличии и их стоимость
    if request.method == 'GET':
        products = models.RequirementsToBuyProduct.objects.filter(
            product__count=1).all().prefetch_related('product')
        serializer = serializers.RequirementsToBuyProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)

    # TODO controll transactios
    if request.method == 'PUT':
        summary_cost = 0
        user = models.UserProfile.objects.get(id=request.user.id)
        products_req = models.RequirementsToBuyProduct.objects.filter(
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
        products = models.Product.objects.all()
        p = models.Purchase(user=request.user)
        p.save()
        p.products.set(products)
        for product in products:
            product.count -= 1
            product.save()
        return Response(data="Done")


class StatisticsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    serializer_class = serializers.StatisticsSerializer
    queryset = models.Statistics.objects.all()


class TeamsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TeamSerializer
    queryset = models.Team.objects.all()


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TaskSerializer
    queryset = models.Task.objects.all()


@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def get_daily_tasks(request):
    if request.method == 'GET':
        user = models.UserProfile.objects.get(id=request.user.id)
        tasks = models.Task.objects.all().filter(taskType="daily").exclude(
            ~Q(parent=None)).exclude(
            ~Q(weekly=None)).filter(division=user.division)
        serializer = serializers.TaskSerializer(tasks, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_weekly_tasks(request):
    if request.method == 'GET':
        user = models.UserProfile.objects.get(id=request.user.id)
        weeklyTasks = models.WeeklyTask.objects.all().filter(division=user.division)
        serializer = serializers.WeeklyTaskSerializer(weeklyTasks, many=True)
        for weeklyTask in serializer.data:
            subTasks = models.Task.objects.all().filter(weekly=weeklyTask['id'])
            subSerializer = serializers.TaskSerializer(subTasks, many=True)
            weeklyTask['subTasks'] = subSerializer.data
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_quests(request):
    if request.method == 'GET':
        user = models.UserProfile.objects.get(id=request.user.id)
        quests = models.MainQuest.objects.all().filter(division=user.division)
        active_quests = [x for x in quests if x.is_active is True]
        quest_serializer = serializers.QuestSerializer(active_quests, many=True)
        tasks_user_status = models.TaskUserStatus.objects.all().filter(user_id=user.id)
        for quest in quest_serializer.data:  # прогоняем каждый квест
            tree_tasks = models.MainQuestTree.objects.all().filter(mainQuest=quest['id'])  # Берём дерево
            tree_tasks_serializer = serializers.QuestTreeSerializer(tree_tasks, many=True)
            quest['tree'] = tree_tasks_serializer.data
            tasks = models.Task.objects.filter(id__in=[task_tree.task.id for task_tree in tree_tasks])
            serializer = serializers.TaskSerializer(tasks, many=True)
            quest['tasks'] = serializer.data
            for task in serializer.data:
                sub_tasks = models.Task.objects.all().filter(parent=task['id'])
                sub_tasks_serializer = serializers.TaskSerializer(sub_tasks, many=True)
                task['subTasks'] = sub_tasks_serializer.data
                task_status = tasks_user_status.filter(task_id=task['id'])
                task_status_serializer = serializers.TaskUserStatusSerializer(task_status, many=True)
                task['status'] = task_status_serializer.data
        return Response(quest_serializer.data)


class WeeklyTaskViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.WeeklyTaskSerializer
    queryset = models.WeeklyTask.objects.all()


class TaskUserStatusViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TaskUserStatusSerializer
    queryset = models.TaskUserStatus.objects.all()


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
