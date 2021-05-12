from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from taggit.managers import TaggableManager


# Create your models here.

##############################################
# ПОЛЬЗОВАТЕЛИ И КОМАНДЫ
##############################################

class JobPosition(models.Model):
    title = models.CharField(max_length=120, verbose_name="Название должности", unique=True)
    description = models.TextField(verbose_name="Описание трудовых обязанностей")

    class Meta:
        verbose_name = "должность"
        verbose_name_plural = "должности"

    def __str__(self):
        return self.title


class Division(models.Model):
    title = models.CharField(max_length=120, verbose_name="Подразделение", unique=True)
    description = models.TextField(verbose_name="Описание подразделения сотрудников")

    class Meta:
        verbose_name = "подразделение"
        verbose_name_plural = "подразделения"

    def __str__(self):
        return self.title


class UserProfileManager(BaseUserManager):
    def create_user(self, email, username, name, surname, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an username')
        if not name:
            raise ValueError('Users must have an name')
        if not surname:
            raise ValueError('Users must have an surname')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            surname=surname,
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, name, surname, password=None):

        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            surname=surname,
            name=name,
        )
        user.is_admin = True
        user.userType = 'admin'
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser):
    ADMIN = 'admin'
    EXPERT = 'expert'
    EMPLOYEE = 'employee'
    GAMEMASTER = 'gamemaster'
    USER_TYPE_CHOICES = (
        (ADMIN, 'Администратор'),
        (EXPERT, 'Эксперт'),
        (EMPLOYEE, 'Сотрудник'),
        (GAMEMASTER, 'Гейм-мастер'),
    )

    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="Зарегистрировался")
    last_login = models.DateTimeField(auto_now=True, verbose_name="Был в сети")
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'surname']

    objects = UserProfileManager()

    # IDs

    jobPosition = models.ForeignKey(JobPosition, on_delete=models.CASCADE,
                                    null=True, blank=True, verbose_name="Должность")
    division = models.ForeignKey(Division, on_delete=models.CASCADE,
                                 null=True, blank=True, verbose_name="Подразделение")
    # IDs

    userType = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default=EMPLOYEE,
                                verbose_name="Тип пользователя")
    name = models.CharField(max_length=100, blank=True, verbose_name="Имя")
    surname = models.CharField(max_length=100, blank=True, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=100, blank=True, null=True, verbose_name="Отчество")
    birthDate = models.DateField(blank=True, null=True, verbose_name="Дата рождения")
    description = models.TextField(max_length=200, blank=True, null=True, verbose_name="О себе")
    photo = models.ImageField(verbose_name="Фото", blank=True, null=True, )
    level = models.IntegerField(default=0, verbose_name="Уровень")

    money = models.IntegerField(default=0, verbose_name="Кол-во Валюты")
    health = models.IntegerField(default=0, verbose_name="Кол-во HP")
    energy = models.IntegerField(default=0, verbose_name="Кол-во Энергии")

    quality = models.FloatField(default=0.0, verbose_name="Качество")
    productivity = models.FloatField(default=0.0, verbose_name="Продуктивность")

    competitionCount = models.IntegerField(default=0, verbose_name="Кол-во соревнований")
    winCompetitionCount = models.IntegerField(default=0, verbose_name="Кол-во выиграных соревнований")

    # def completedTests(self, instance):
    #     self.statistics.completedTests
    # def completedTasks(self, instance):
    #     self.statistics.completedTasks
    # def completedQuests(self, instance):
    #     self.statistics.completedQuests
    # def achievements(self, instance):
    #     self.statistics.achievements

    # completedTests = property(completedTests)

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    def __str__(self):
        return self.name + ' ' + self.surname

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Statistics(models.Model):
    # IDs

    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, verbose_name="Пользователь", related_name="statistics")

    # IDs

    level = models.IntegerField(default=0, verbose_name="Уровень")
    quality = models.FloatField(default=0.0, verbose_name="Качество")
    productivity = models.FloatField(default=0.0, verbose_name="Продуктивность")
    completedTests = models.IntegerField(default=0, verbose_name="Кол-во выполненых тестов")
    completedTasks = models.IntegerField(default=0, verbose_name="Кол-во выполненых задач")
    completedQuests = models.IntegerField(default=0, verbose_name="Кол-во выполненых квестов")
    achievements = models.IntegerField(default=0, verbose_name="Кол-во ачивок")
    competitions = models.IntegerField(default=0, verbose_name="Кол-во соревнований")
    competitionWins = models.IntegerField(default=0, verbose_name="Кол-во выиграных соревнований")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время сбора статистики")

    class Meta:
        verbose_name = "статистика пользователя"
        verbose_name_plural = "статистика пользователей"

    def __str__(self):
        return str(self.id)


class Team(models.Model):
    # IDs

    users = models.ManyToManyField(UserProfile, through='TeamMember',
                                   through_fields=('team', 'user'))
    division = models.ForeignKey(Division, on_delete=models.CASCADE, verbose_name="Подразделение", )

    # IDs

    title = models.CharField(max_length=120, verbose_name="Название команды")
    description = models.TextField(verbose_name="Описание команды")
    maxUsersCount = models.IntegerField(default=5, verbose_name="Максимальное кол-во участников")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "команда"
        verbose_name_plural = "команды"


class TeamMember(models.Model):
    LEADER = 'leader'
    MEMBER = 'member'
    LEF_TEAM = 'left_team'
    MEMBER_TYPE_CHOICES = (
        (LEADER, 'Лидер команды'),
        (MEMBER, 'Обычный участник'),
        (LEF_TEAM, 'Ушел из команды'),
    )
    # IDs

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="Пользователь", )
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name="Команда", )

    # IDs

    memberType = models.CharField(max_length=20, choices=MEMBER_TYPE_CHOICES,
                                  default=MEMBER, verbose_name="Тип участника")

    joined_at = models.DateTimeField(auto_now_add=True)
    leftTeam_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


##############################################
# ЗАДАЧИ И КВЕСТЫ
##############################################

class WeeklyTask(models.Model):
    DAILY = 'daily'
    QUEST = 'quest'
    TASK_TYPE_CHOICES = (
        (DAILY, 'Ежедневное задание'),
        (QUEST, 'Квест'),
    )

    EASY = 'easy'
    MEDIUM = 'medium'
    HARD = 'hard'
    DIFFICULTY_TYPE_CHOICES = (
        (EASY, 'Легко'),
        (MEDIUM, 'Средне'),
        (HARD, 'Сложно'),
    )

    # IDs

    division = models.ForeignKey(Division, on_delete=models.CASCADE, verbose_name="Подразделение", )

    # IDs

    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_TYPE_CHOICES,
                                  default=EASY, verbose_name="Сложность")
    taskType = models.CharField(max_length=20, choices=TASK_TYPE_CHOICES, default=DAILY, verbose_name="Тип задания")
    title = models.CharField(max_length=200, unique=True, verbose_name="Название задания")
    description = models.TextField(verbose_name="Описание задания")
    subTasksCount = models.IntegerField(default=0, verbose_name="Кол-во доп заданий")
    isTeamTask = models.BooleanField(default=False, verbose_name="Групповое задание")
    tags = TaggableManager()

    accessLevel = models.IntegerField(blank=True, null=True)
    deadline = models.IntegerField(blank=True, null=True)

    money = models.IntegerField(default=0, verbose_name="Валюта")
    health = models.IntegerField(default=0, verbose_name="HP")
    energy = models.IntegerField(default=0, verbose_name="Энергия")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "еженедельное задание"
        verbose_name_plural = "еженедельные задания"


class WeeklyTaskUserStatus(models.Model):
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'
    TASK_STATUS_CHOICES = (
        (IN_PROGRESS, 'В процессе выполнения'),
        (COMPLETED, 'Выполнено'),
    )
    # IDs

    weeklyTask = models.ForeignKey(WeeklyTask, on_delete=models.CASCADE, verbose_name="Задача", )
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="Пользователь", )

    # IDs

    subTasksCount = models.IntegerField(default=0, verbose_name="Кол-во доп задач")
    subTasksCompletedCount = models.IntegerField(default=0, verbose_name="Кол-во выполненных доп задач")
    status = models.CharField(max_length=20, choices=TASK_STATUS_CHOICES, default=IN_PROGRESS,
                              verbose_name="Статус выполнения", )
    started_at = models.DateTimeField(auto_now_add=True, verbose_name="Задача начата", )
    done_at = models.DateTimeField(null=True, blank=True, verbose_name="Задача выполнена", )

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "статус задания отдельного пользователя"
        verbose_name_plural = "статусы заданий отдельного пользователя"


class Task(models.Model):
    DAILY = 'daily'
    QUEST = 'quest'
    TASK_TYPE_CHOICES = (
        (DAILY, 'Ежедневное задание'),
        (QUEST, 'Квест'),
    )

    EASY = 'easy'
    MEDIUM = 'medium'
    HARD = 'hard'
    DIFFICULTY_TYPE_CHOICES = (
        (EASY, 'Легко'),
        (MEDIUM, 'Средне'),
        (HARD, 'Сложно'),
    )

    # IDs

    weekly = models.OneToOneField(WeeklyTask, on_delete=models.CASCADE, blank=True, null=True,
                                  verbose_name='Еженедельное', )
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True,
                               verbose_name='Основное', )
    users = models.ManyToManyField(UserProfile, through='TaskUserStatus', through_fields=('task', 'user'), )

    division = models.ForeignKey(Division, on_delete=models.CASCADE, verbose_name="Подразделение", )

    # IDs

    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_TYPE_CHOICES,
                                  default=EASY, verbose_name="Сложность")
    taskType = models.CharField(max_length=20, choices=TASK_TYPE_CHOICES, default=DAILY, verbose_name="Тип задания")
    title = models.CharField(max_length=200, unique=True, verbose_name="Название задания")
    description = models.TextField(verbose_name="Описание задания")
    subTasksCount = models.IntegerField(default=0, verbose_name="Кол-во доп заданий")
    isTeamTask = models.BooleanField(default=False, verbose_name="Групповое задание")
    tags = TaggableManager()

    accessLevel = models.IntegerField(blank=True, null=True)
    deadline = models.IntegerField(blank=True, null=True)

    money = models.IntegerField(default=0, verbose_name="Валюта")
    health = models.IntegerField(default=0, verbose_name="HP")
    energy = models.IntegerField(default=0, verbose_name="Энергия")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    class Meta:
        verbose_name = "задание"
        verbose_name_plural = "задания"

    def __str__(self):
        return self.title


class TaskUserStatus(models.Model):
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'
    TASK_STATUS_CHOICES = (
        (IN_PROGRESS, 'В процессе выполнения'),
        (COMPLETED, 'Выполнено'),
    )
    # IDs

    task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name="Задача", )
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="Пользователь", )

    # IDs

    subTasksCount = models.IntegerField(default=0, verbose_name="Кол-во доп задач")
    subTasksCompletedCount = models.IntegerField(default=0, verbose_name="Кол-во выполненных доп задач")
    status = models.CharField(max_length=20, choices=TASK_STATUS_CHOICES, default=IN_PROGRESS,
                              verbose_name="Статус выполнения", )
    started_at = models.DateTimeField(auto_now_add=True, verbose_name="Задача начата", )
    done_at = models.DateTimeField(null=True, blank=True, verbose_name="Задача выполнена", )

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "статус задания отдельного пользователя"
        verbose_name_plural = "статусы заданий отдельного пользователя"


class MainQuest(models.Model):
    EASY = 'easy'
    MEDIUM = 'medium'
    HARD = 'hard'
    DIFFICULTY_TYPE_CHOICES = (
        (EASY, 'Легко'),
        (MEDIUM, 'Средне'),
        (HARD, 'Сложно'),
    )

    # IDs

    division = models.ForeignKey(Division, on_delete=models.CASCADE, verbose_name="Подразделение", )
    tasks = models.ManyToManyField(Task, through='MainQuestTree', through_fields=('mainQuest', 'task'), )
    users = models.ManyToManyField(UserProfile, through='MainQuestStatus', through_fields=('mainQuest', 'user'), )

    # IDs

    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_TYPE_CHOICES,
                                  default=EASY, verbose_name="Сложность")
    title = models.CharField(max_length=120)
    description = models.TextField()
    deadline = models.IntegerField(default=0)
    accessLevel = models.IntegerField(default=0)
    tasksCount = models.IntegerField(default=0)

    money = models.IntegerField(default=0, verbose_name="Валюта")
    health = models.IntegerField(default=0, verbose_name="HP")
    energy = models.IntegerField(default=0, verbose_name="Энергия")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "основной квест"
        verbose_name_plural = "основные квесты"


class MainQuestTree(models.Model):
    # IDs

    mainQuest = models.ForeignKey(MainQuest, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, )
    parentTask = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='parentTask')
    childTask = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='childTask')

    # IDs

    treeLevel = models.IntegerField(default=0)
    treePosition = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "дерево основной квест"
        verbose_name_plural = "деревья основных квестов"


class MainQuestStatus(models.Model):
    INPROGRESS = 'inprogress'
    COMPLETED = 'completed'
    QUEST_STATUS_CHOICES = (
        (INPROGRESS, 'В процессе выполнения'),
        (COMPLETED, 'Выполнено'),
    )
    # IDs

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="Пользователь", )
    mainQuest = models.ForeignKey(MainQuest, on_delete=models.CASCADE, verbose_name="Основной квест", )

    # IDs

    status = models.CharField(max_length=20, choices=QUEST_STATUS_CHOICES, default=INPROGRESS,
                              verbose_name="Статус выполнения", )
    completeTime = models.DateTimeField(blank=True, null=True, )
    started_at = models.DateTimeField(auto_now_add=True)
    done_at = models.DateTimeField(blank=True, null=True, )

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "статус основного квеста пользователя"
        verbose_name_plural = "статусы основных квестов пользователей"


##############################################
# СОРЕВНОВАНИЯ
##############################################

class Competition(models.Model):
    # IDs

    users = models.ManyToManyField(UserProfile)
    winner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='winner')

    # IDs

    title = models.CharField(max_length=120)
    isCompleted = models.BooleanField(default=False)
    deadline = models.DateTimeField(blank=True, null=True)

    levelCriterion = models.IntegerField(default=0, verbose_name="Требуемый уровень")
    qualityCriterion = models.FloatField(default=0.0, verbose_name="Треюуемое качество")
    productivityCriterion = models.FloatField(default=0.0, verbose_name="Требуемая продуктивность")

    money = models.IntegerField(default=0, verbose_name="Валюта")
    health = models.IntegerField(default=0, verbose_name="HP")
    energy = models.IntegerField(default=0, verbose_name="Энергия")

    created_at = models.DateTimeField(auto_now_add=True)
    done_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "соревнование"
        verbose_name_plural = "соревнования"


##############################################
# ДОСТИЖЕНИЯ
##############################################

class Achievement(models.Model):
    # IDs

    users = models.ManyToManyField(UserProfile, through='AchievementUserStatus',
                                   through_fields=('achievement', 'user'))

    # IDs

    title = models.CharField(max_length=120, verbose_name="Название ачивки")
    description = models.TextField(verbose_name="Описание ачивки")
    image = models.ImageField(verbose_name="Картинка ачивки")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "достижение"
        verbose_name_plural = "достижения"


class AchievementUserStatus(models.Model):
    # IDs

    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE, verbose_name="Ачивка")
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="Пользователь", )

    # IDs

    completed_at = models.DateTimeField(auto_now_add=True, verbose_name="Время получения")

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "статус получения достижения"
        verbose_name_plural = "статусы получения достижений"


class RequirenmentToGetAchieve(models.Model):
    # IDs

    users = models.ManyToManyField(UserProfile, through='AchieveRequirenmentStatus',
                                   through_fields=('requirenmentToGetAchieve', 'user'))
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE, verbose_name="Ачивка")

    completedAchievement = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True,
                                             verbose_name='Выполенная другая ачивка', )
    completedTask = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name="Выполненная задача",
                                      blank=True, null=True, )
    completedWeeklyTask = models.ForeignKey(WeeklyTask, on_delete=models.CASCADE,
                                            verbose_name="Выполненная еженедельная задача",
                                            blank=True, null=True, )
    completedMainQuest = models.ForeignKey(MainQuest, on_delete=models.CASCADE,
                                           verbose_name="Выполненный основной квест",
                                           blank=True, null=True, )
    completedTest = models.ForeignKey('Test', on_delete=models.CASCADE,
                                      verbose_name="Выполненный тест",
                                      blank=True, null=True, )

    # IDs

    completeTime = models.DateTimeField(blank=True, null=True, verbose_name="Время на выполнение")

    level = models.IntegerField(default=0, verbose_name="Требуемый уровень")
    quality = models.FloatField(default=0.0, verbose_name="Треюуемое качество")
    productivity = models.FloatField(default=0.0, verbose_name="Требуемая продуктивность")
    competitionsCount = models.IntegerField(default=0, verbose_name="Кол-во соревнований")
    competitionWinsCount = models.IntegerField(default=0, verbose_name="Кол-во выиграных соревнований")

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "требование для получения достижения"
        verbose_name_plural = "требования для получения достижений"


class AchieveRequirenmentStatus(models.Model):
    # IDs

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="Пользователь", )
    requirenmentToGetAchieve = models.ForeignKey(RequirenmentToGetAchieve, on_delete=models.CASCADE,
                                                 verbose_name="Требование для получения ачивки")

    # IDs

    completeTime = models.DateTimeField(blank=True, null=True, verbose_name="Время на выполнение")
    isCompleted = models.BooleanField(default=False)
    level = models.IntegerField(default=0, verbose_name="Прогресс уровня")
    quality = models.FloatField(default=0.0, verbose_name="Прогресс качества")
    productivity = models.FloatField(default=0.0, verbose_name="Прогресс продуктивности")
    competitionsCount = models.IntegerField(default=0, verbose_name="Кол-во соревнований")
    competitionWinsCount = models.IntegerField(default=0, verbose_name="Кол-во выиграных соревнований")

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "статус получения достижения пользователем"
        verbose_name_plural = "статусы получения достижений пользователями"


##############################################
# ВОПРОСЫ И ТЕСТЫ
##############################################


class QuestionTheme(models.Model):
    title = models.CharField(max_length=120, verbose_name="Название тематики")
    description = models.TextField(verbose_name="Описание тематики")

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "тематика вопроса"
        verbose_name_plural = "тематики вопросов"


class Question(models.Model):
    EASY = 'easy'
    MEDIUM = 'medium'
    HARD = 'hard'
    DIFFICULTY_TYPE_CHOICES = (
        (EASY, 'Легко'),
        (MEDIUM, 'Средне'),
        (HARD, 'Сложно'),
    )

    ONE_CHOICE = 'one_choice'
    MULTI_CHOICE = 'multi_choice'
    ENTER_NUMBER = 'enter_number'
    ENTER_TEXT = 'enter_text'
    ANSWER_TYPE_CHOICES = (
        (ONE_CHOICE, '1 выбор'),
        (MULTI_CHOICE, 'Мультивыбор'),
        (ENTER_NUMBER, 'Ввод числа'),
        (ENTER_TEXT, 'Ввод текста'),
    )
    # IDs

    questionTheme = models.ForeignKey(QuestionTheme, on_delete=models.CASCADE, verbose_name="Тематика", )

    # IDs

    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_TYPE_CHOICES,
                                  default=EASY, verbose_name="Сложность")
    answerType = models.CharField(max_length=20, choices=ANSWER_TYPE_CHOICES,
                                  default=ONE_CHOICE, verbose_name="Тип ответа")

    title = models.CharField(max_length=120, verbose_name="Вопрос")
    description = models.TextField(verbose_name="Описание вопроса", blank=True, null=True)
    image = models.ImageField(verbose_name="Картинка для вопроса", blank=True, null=True)
    tags = TaggableManager()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "вопрос"
        verbose_name_plural = "вопросы"


class Answer(models.Model):
    # IDs

    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Вопрос")

    # IDs

    text = models.CharField(max_length=120, verbose_name="Ответ", )
    description = models.TextField(verbose_name="Доп описание ответа", blank=True, null=True)
    image = models.ImageField(verbose_name="Картинка, дополняющая ответ", blank=True, null=True)
    isCorrect = models.BooleanField(default=False, verbose_name="Правильный ответ")

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "ответ"
        verbose_name_plural = "ответы"


class Test(models.Model):
    # IDs

    users = models.ManyToManyField(UserProfile, through='TestUser',
                                   through_fields=('test', 'user'))

    # IDs

    title = models.CharField(max_length=120, verbose_name="Название теста")
    description = models.TextField(verbose_name="Описание теста")
    pointsToComplete = models.IntegerField(default=10, verbose_name="Кол-во баллов для зачета")

    canLeave = models.BooleanField(default=True, verbose_name="Можно покидать страницу теста")
    canSkip = models.BooleanField(default=True, verbose_name="Можно пропускать вопросы")
    showAnswers = models.BooleanField(default=True, verbose_name="Показывать ответы в конце теста")

    isInterview = models.BooleanField(default=False, verbose_name="Тест для собеседования")
    canSeeSpentTime = models.BooleanField(default=False, verbose_name="Просмотр затраченного времени")
    canSeeTestClosing = models.BooleanField(default=False, verbose_name="Просмотр закрытия теста")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "тест"
        verbose_name_plural = "тесты"

class TestBlock(models.Model):

    # IDs

    questionTheme = models.ForeignKey(QuestionTheme, on_delete=models.CASCADE, verbose_name="Тематика")

    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name="Тест", )
    questions = models.ManyToManyField(Question, verbose_name="",default=None)
    
    # IDs

    questionsCount = models.IntegerField(default=3, verbose_name="Кол-во вопросов")
    blockWeight = models.FloatField(default=0.0, verbose_name="Вес блока")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "тестовый блок"
        verbose_name_plural = "тестовые блоки"

class TestUser(models.Model):
    STARTED = 'started'
    FAILED = 'failed'
    DONE = 'done'
    STATUS_TYPE_CHOICES = (
        (STARTED, 'Начат'),
        (FAILED, 'Провален'),
        (DONE, 'Выполнен'),
    )

    # IDs

    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name="Тест", )
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="Пользователь", )
    answers = models.ManyToManyField(Question, through='TestUserAnswer',
                                     through_fields=('testUser', 'question'), verbose_name="Ответы")

    # IDs

    status = models.CharField(max_length=20, choices=STATUS_TYPE_CHOICES,
                              default=STARTED, verbose_name="Статус")
    rightAnswersCount = models.IntegerField(default=0, verbose_name="Кол-во правильных ответов")
    completeTime = models.DateTimeField(blank=True, null=True, verbose_name="Время выполнения")
    points = models.IntegerField(default=0, verbose_name="Кол-во набранных баллов")
    hasLeftTest = models.BooleanField(default=False, verbose_name="Покидал страницу теста")

    started_at = models.DateTimeField(auto_now_add=True, verbose_name="Время старта теста")
    done_at = models.DateTimeField(blank=True, null=True, verbose_name="Покидал окончания теста")

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"


class TestUserAnswer(models.Model):
    # IDs

    testUser = models.ForeignKey(TestUser, on_delete=models.CASCADE, verbose_name="Тест, начатый пользователем")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Вопрос")

    # IDs

    text = models.CharField(max_length=120, verbose_name="Текст ответа")
    isCorrect = models.BooleanField(default=False, verbose_name="Ответ правильный")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    def __str__(self):
        return str(self.text)

    class Meta:
        verbose_name = "ответ пользователя"
        verbose_name_plural = "ответы пользователей"


##############################################
# ТРЕБОВАНИЯ
##############################################


class RequirementsToGetAccess(models.Model):
    # IDs

    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name="Тест", blank=True, null=True, )
    task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name="Задача", blank=True, null=True, )
    weeklyTask = models.ForeignKey(WeeklyTask, on_delete=models.CASCADE, verbose_name="Еженедельная задача",
                                   blank=True, null=True, )
    mainQuest = models.ForeignKey(MainQuest, on_delete=models.CASCADE, verbose_name="Основной квест",
                                  blank=True, null=True, )
    completedTest = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name="Выполненный тест", blank=True,
                                      null=True, related_name='completedTest')
    completedTask = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name="Выполненная задача", blank=True,
                                      null=True, related_name='completedTask')
    completedWeeklyTask = models.ForeignKey(Task, on_delete=models.CASCADE,
                                            verbose_name="Выполненная еженедельная задача", blank=True,
                                            null=True, related_name='completedWeeklyTask')
    completedMainQuest = models.ForeignKey(MainQuest, on_delete=models.CASCADE,
                                           verbose_name="Выполненный основной квест",
                                           blank=True, null=True, related_name='completedMainQuest')

    # IDs

    level = models.IntegerField(default=0, verbose_name="Требуемый уровень")
    quality = models.FloatField(default=0.0, verbose_name="Требуемое качество")
    productivity = models.FloatField(default=0.0, verbose_name="Требуемая продуктивность")

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "требование для получения доступа"
        verbose_name_plural = "требования для получения доступа"


class RequirementsToComplete(models.Model):
    # IDs

    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name="Тест", blank=True, null=True, )
    task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name="Задача", blank=True, null=True, )
    mainQuest = models.ForeignKey(MainQuest, on_delete=models.CASCADE, verbose_name="Основной квест",
                                  blank=True, null=True, )
    weeklyTask = models.ForeignKey(WeeklyTask, on_delete=models.CASCADE, verbose_name="Еженедельная задача",
                                   blank=True, null=True, )
    doneTest = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name="Выполненный тест", blank=True,
                                 null=True, related_name='doneTest')
    doneTask = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name="Выполненная задача", blank=True,
                                 null=True, related_name='doneTask')
    doneMainQuest = models.ForeignKey(MainQuest, on_delete=models.CASCADE,
                                      verbose_name="Выполненный основной квест",
                                      blank=True, null=True, related_name='doneMainQuest')
    doneWeeklyTask = models.ForeignKey(Task, on_delete=models.CASCADE,
                                       verbose_name="Выполненная еженедельная задача", blank=True,
                                       null=True, related_name='doneWeeklyTask')

    # IDs

    level = models.IntegerField(default=0, verbose_name="Требуемый уровень")
    quality = models.FloatField(default=0.0, verbose_name="Требуемое качество")
    productivity = models.FloatField(default=0.0, verbose_name="Требуемая продуктивность")

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "требование для выполнения"
        verbose_name_plural = "требования для выполнения"


##############################################
# ТОВАРЫ
##############################################

class ProductCategory(models.Model):
    title = models.CharField(max_length=120, verbose_name="Название товара")
    description = models.TextField(verbose_name="Описание товара")

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "категория товара"
        verbose_name_plural = "категории товаров"


class Product(models.Model):
    # IDs

    productCategory = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name="Категория товара")

    # IDs

    title = models.CharField(max_length=120, verbose_name="Название товара")
    description = models.TextField(verbose_name="Описание товара")
    count = models.IntegerField(default=0, verbose_name="Кол-во товара")
    photo = models.ImageField(verbose_name="Фото товара")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"


class RequirementsToBuyProduct(models.Model):
    # IDs

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Категория товара")
    completedTest = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name="Тест", blank=True, null=True, )
    completedTask = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name="Задача", blank=True, null=True, )
    completedWeeklyTask = models.ForeignKey(WeeklyTask, on_delete=models.CASCADE, verbose_name="Еженедельная задача",
                                            blank=True, null=True, )
    completedMainQuest = models.ForeignKey(MainQuest, on_delete=models.CASCADE, verbose_name="Основной квест",
                                           blank=True, null=True, )

    # IDs

    level = models.IntegerField(default=0, verbose_name="Требуемый уровень")
    quality = models.FloatField(default=0.0, verbose_name="Требуемое качество")
    productivity = models.FloatField(default=0.0, verbose_name="Требуемая продуктивность")

    money = models.IntegerField(default=0, verbose_name="Кол-во Валюты")
    health = models.IntegerField(default=0, verbose_name="Кол-во HP")
    energy = models.IntegerField(default=0, verbose_name="Кол-во Энергии")

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "требование для получения товара"
        verbose_name_plural = "требования для получения товаров"


class CategoryClothes(models.Model):
    S = 's'
    M = 'm'
    XL = 'xl'
    SIZE_TYPE_CHOICES = (
        (S, 'S'),
        (M, 'M'),
        (XL, 'XL'),
    )

    MALE = 'male'
    FEMALE = 'female'
    ALL = 'all'
    GENDER_CHOICES = (
        (MALE, 'мужское'),
        (FEMALE, 'женское'),
        (ALL, 'для всех'),
    )

    TSHIRT = 'tshirt'
    SWEATER = 'sweater'
    JEANS = 'jeans'
    CAP = 'cap'
    CLOTHES_TYPE_CHOICES = (
        (TSHIRT, 'футболка'),
        (SWEATER, 'свитер'),
        (JEANS, 'джинсы'),
        (CAP, 'кепка'),
    )
    # IDs

    product = models.OneToOneField(Product, on_delete=models.CASCADE, verbose_name="Товар")

    # IDs

    size = models.CharField(max_length=20, choices=SIZE_TYPE_CHOICES,
                            default=S, verbose_name="Размер")
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES,
                              default=MALE, verbose_name="Пол")
    clothesType = models.CharField(max_length=20, choices=CLOTHES_TYPE_CHOICES,
                                   default=TSHIRT, verbose_name="Тип одежды")
    color = models.CharField(max_length=7, verbose_name="Цвет")

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "описание товара - одежды"
        verbose_name_plural = "описания товаров - одежды"

    class Purchase(models.Model):
        PENDING = 'pending'
        PAID = 'paid'
        EXPECTS = 'expects'
        RECEIVED = 'received'
        PURCHASE_STATUS_CHOICES = (
            (PENDING, 'оформляется'),
            (PAID, 'оплачен'),
            (EXPECTS, 'оможно забрать'),
            (RECEIVED, 'получен'),
        )
        # IDs

        user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="Пользователь")
        products = models.ManyToManyField(Product, verbose_name="Товары")

        # IDs

        productCount = models.IntegerField(default=0, verbose_name="Кол-во покупаемых товаров")
        status = models.CharField(max_length=20, choices=PURCHASE_STATUS_CHOICES,
                                  default=PENDING, verbose_name="Размер")

        def __str__(self):
            return str(self.id)

    class Meta:
        verbose_name = "покупка"
        verbose_name_plural = "покупки"
