from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from .models import UserProfile, MainQuest, Task, WeeklyTask, Division, JobPosition, Team, \
    MainQuest, Question, QuestionTheme, Test, TestUser, TestUserAnswer, TestBlock, Achievement, \
    RequirenmentToGetAchieve, Product, RequirementsToBuyProduct, ProductCategory, Answer, TaskUserStatus, \
    MainQuestStatus, MainQuestTree
from django.db import models
from django.db.models import Q
from django import forms
from django.urls import resolve
from django.utils.safestring import mark_safe


from django.contrib.admin import ModelAdmin, TabularInline
# from .models import Category, Product, ProductSliderImage


# class AdminCategory(ModelAdmin):
#     search_fields = ['title']
#     list_display = ['title', 'active']
#     list_filter = ('active',)
#
#
# class AdminProduct(ModelAdmin):
#     search_fields = ['title']
#     list_display = ['title', 'active']
#     list_filter = ('active', 'parent')

# Register your models here.

class DivisionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)
    fieldsets = ((None, {
        'fields': (
            'title',
            'description',
        )
    }),)
    filter_horizontal = ()


class TeamInline(admin.StackedInline):
    extra = 0
    max_num = 10
    model = Team.users.through
    fields = (
        ('user',
         'memberType',),
        ('joined_at',
         'leftTeam_at')
    )
    readonly_fields = ('joined_at', 'leftTeam_at')


class TeamAdmin(admin.ModelAdmin):
    inlines = [TeamInline, ]
    list_display = ('title', 'description', 'division')
    search_fields = ('title',)
    fieldsets = ((None, {
        'fields': (
            'title',
            'description',
            'division',
            'maxUsersCount',

        )
    }),)
    filter_horizontal = ()
    readonly_fields = ('created_at', 'updated_at')


class JobPositionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)
    fieldsets = ((None, {
        'fields': (
            'title',
            'description',
        )
    }),)
    filter_horizontal = ()


class UserProfileAdmin(UserAdmin):
    list_display = ('email', 'username', 'name',
                    'surname', 'last_login', 'userType')
    search_fields = ('email', 'name', 'surname')
    readonly_fields = ('date_joined', 'last_login',
                       'competitionCount', 'winCompetitionCount')
    filter_horizontal = ()
    fieldsets = ()
    list_filter = ('division', "jobPosition")
    fields = ('username', 'email',
              ('surname', 'name', "patronymic"),
              "birthDate",
              ("userType", "jobPosition", "division"),
              "description", "photo",
              ("money", "health", "energy"),
              ("level", "quality", "productivity"),
              #   ("completedTests", "completedTasks", "completedQuests"),
              #   ("achievements"),
              ("competitionCount", "winCompetitionCount"),
              "last_login", "date_joined")


class SubTask(admin.StackedInline):
    model = Task
    extra = 0
    max_num = 3
    fields = (
        'title',
        'description',
        'isTeamTask',
        'deadline',
        ('money',
         'health',
         'energy'),
        'tags'
    )


class TaskAdmin(admin.ModelAdmin):
    # category = 'testy'

    def get_queryset(self, request):
        return super().get_queryset(request).exclude(
            ~Q(parent=None)).exclude(
            ~Q(weekly=None)).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())
    tag_list.short_description = "Теги"

    inlines = [SubTask]
    list_display = ('title', 'taskType', 'subTasksCount',
                    'isTeamTask', 'tag_list')
    list_display_links = ('title',)
    search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at')
    filter_horizontal = ()
    list_filter = ('tags',)
    fieldsets = ((None, {
        'fields': (
            'taskType',
            "division",
            'title',
            'description',
            'isTeamTask',
            'deadline',
            ('money',
             'health',
             'energy'),
            'tags',
            'subTasksCount'
        )
    }),)


class TaskInline(admin.StackedInline):
    model = Task
    can_delete = False
    extra = 0
    max_num = 3
    fields = (
        "division",
        'title',
        'description',
        'isTeamTask',
        ('money',
         'health',
         'energy'),
        'tags',
        'subTasksCount'
    )


class WeeklyTaskAdmin(admin.ModelAdmin):

    inlines = [TaskInline]

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())
    tag_list.short_description = "Теги"

    list_display = ('title', 'subTasksCount',
                    'isTeamTask', 'tag_list')
    list_filter = ('tags',)
    search_fields = ('title',)
    fieldsets = ((None, {
        'fields': (
            'taskType',
            "division",
            'title',
            'description',
            'isTeamTask',
            ('money',
             'health',
             'energy'),
            'tags',
            'subTasksCount'
        )
    }),)
    readonly_fields = ('created_at', 'updated_at')
    filter_horizontal = ()


class TasksInline(admin.StackedInline):
    extra = 0
    model = MainQuest.tasks.through
    fields = (
        ('task',
         'parentTask',
         'childTask')
    )


class MainQuestAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'accessLevel', 'time_left', 'is_active')
    search_fields = ('title',)
    fieldsets = ((None, {
        'fields': (
            'division',
            'difficulty',
            'title',
            'description',
            'deadline',
            'accessLevel',
            # 'tasks'
        )
    }), (None, {
        'fields': (
            ('created_at',
             'updated_at'),
        )
    }))
    inlines = [TasksInline, ]
    list_filter = ('title', 'accessLevel')
    filter_horizontal = ()
    readonly_fields = ('created_at', 'updated_at')


class AnswerAdmin(admin.ModelAdmin):
    search_fields = ('text',)
    list_display = ('text', 'question',  'isCorrect',)

    fieldsets = (
        (None, {
            'fields': (
                'question',
                'text',
                ('description', 'image',),
                'isCorrect'
            )

        }),
    )


class AnswerInline(admin.StackedInline):
    model = Answer
    can_delete = False
    extra = 0
    max_num = 4
    fields = (
        'text',
        ('description', 'image',),
        'isCorrect'
    )


class QuestionAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())
    tag_list.short_description = "Теги"

    inlines = [AnswerInline, ]
    list_display = ('title', 'description', 'questionTheme', 'tag_list')
    search_fields = ('title',)
    fieldsets = ((None, {
        'fields': (
            ('questionTheme',
             'difficulty'),
            'title',
            'description',
            'image',
            'tags',
            'answerType'

        )
    }),)
    list_filter = ('tags',)
    filter_horizontal = ()
    readonly_fields = ('created_at', 'updated_at')


class QuestionThemeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)
    fieldsets = ((None, {
        'fields': (
            'title',
            'description',
        )
    }),)
    filter_horizontal = ()


class TestBlockInlineForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TestBlockInlineForm, self).__init__(*args, **kwargs)
        if 'instance' in kwargs:
            self.errors  # Без этого почему-то не работает вызов ошибки "Выберите вопросы по теме"
            self.fields['questions'].queryset = Question.objects.filter(
                questionTheme=QuestionTheme.objects.get(id=self['questionTheme'].value()))
            self.fields['questions'].help_text = 'Пользуйтесь Ctrl (Command) и Shift. Чтобы отобразились вопросы другой тематики, поменяйте тематику и попробуйте сохранить.'
            # Можно заменить виджет, например, на multiwidget

    def clean_questions(self):
        data = self.cleaned_data['questions']
        data_theme = self.cleaned_data['questionTheme']

        for quest in data:
            if quest.questionTheme != data_theme:
                raise forms.ValidationError('Выберите вопросы по теме')

        return data

    class Meta:
        model = TestBlock
        fields = '__all__'


class TestBlockInline(admin.StackedInline):
    extra = 0
    model = TestBlock
    form = TestBlockInlineForm
    fieldsets = (
        (None, {
            'fields': (
                ('questionTheme',
                 'blockWeight',),
                ('created_at',
                 'updated_at',))

        }),
        ('Вопросы', {
            'classes': ('collapse',),
            'fields': ('questions',),
        }),
    )
    readonly_fields = ('created_at', 'updated_at')


class TestAdmin(admin.ModelAdmin):
    inlines = [TestBlockInline, ]

    list_display = ('title', 'description')

    search_fields = ('title',)
    fieldsets = ((None, {
        'fields': (
            'title',
            'description',
            'pointsToComplete',
            'canLeave',
            'canSkip',
            'showAnswers',
            'canSeeSpentTime',
            'canSeeTestClosing',
        )
    }),)

    filter_horizontal = ()
    readonly_fields = ('created_at', 'updated_at')


class TestUserAdmin(admin.ModelAdmin):

    list_display = ('id', 'test', 'user', 'status')

    fieldsets = ((None, {
        'fields': (
            'status',
            'rightAnswersCount',
            'points',
        )
    }),)

    filter_horizontal = ()


class TestUserAnswerAdmin(admin.ModelAdmin):

    list_display = ('id', 'testUser', 'question', 'text', 'isCorrect')

    fieldsets = ((None, {
        'fields': (
            'testUser', 'question', 'text',
            'isCorrect',
        )
    }),)

    filter_horizontal = ()


class RequirenmentToGetAchieveInline(admin.StackedInline):
    model = RequirenmentToGetAchieve
    extra = 1

    fields = (
        ('completedAchievement',
         'completedTask',
         'completedWeeklyTask',
         'completedMainQuest',
         'completedTest',),
        ('completeTime',),
        ('level',
         'quality',
         'productivity',
         'competitionsCount',
         'competitionWinsCount',),
    )


class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'get_image')

    inlines = (RequirenmentToGetAchieveInline,)

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="75">')
        else:
            return 'Фото не установлено'

    get_image.short_description = 'Фото'


class RequirementsToBuyProductInline(admin.TabularInline):
    model = RequirementsToBuyProduct
    fields = ('level', 'money',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'get_image', 'count')

    inlines = (RequirementsToBuyProductInline, )

    def get_image(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return 'Фото не установлено'

    get_image.short_description = 'Фото'


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


class MyAdminSite(admin.AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = 'ЮMoney.Геймификация'

    # Text to put in each page's <h1> (and above login form).
    site_header = 'Геймификация'

    # Text to put at the top of the admin index page.
    index_title = 'Панель администрирования'

    def get_app_list(self, request):
        app_dict = self._build_app_dict(request)
        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())
        return app_list


admin.site = MyAdminSite()

admin.site.register(WeeklyTask, WeeklyTaskAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(MainQuest, MainQuestAdmin)

admin.site.register(TaskUserStatus)
admin.site.register(MainQuestStatus)
admin.site.register(MainQuestTree)

admin.site.register(Test, TestAdmin)
admin.site.register(TestUser, TestUserAdmin)
admin.site.register(TestUserAnswer, TestUserAnswerAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(QuestionTheme, QuestionThemeAdmin)

admin.site.register(Achievement, AchievementAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Division, DivisionAdmin)
admin.site.register(JobPosition, JobPositionAdmin)
admin.site.register(Team, TeamAdmin)
