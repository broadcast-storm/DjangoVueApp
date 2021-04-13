from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, Task, WeeklyTask, Division, JobPosition, Team, Question, QuestionTheme, Test, TestBlock
from django.db import models
from django.urls import resolve


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
    list_display = ('email', 'username', 'name', 'surname', 'last_login', 'userType')
    search_fields = ('email', 'name', 'surname')
    readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = ()
    fieldsets = ()
    list_filter = ('division', "jobPosition")
    fields = ('username', 'email',
              ('name', 'surname', "patronymic"),
              "birthDate",
              ("userType", "jobPosition", "division"),
              "description", "photo",
              ("money", "health", "energy"),
              ("level", "quality", "productivity"),
              ("competitionCount", "winCompetitionCount"),
              "last_login", "date_joined")


class SubTask(admin.StackedInline):
    model = Task
    extra = 0
    max_num = 3
    fields = (
        'taskType',
        'title',
        'description',
        'isTeamTask',
        ('money',
         'health',
         'energy'),
        'tags'
    )


class TaskAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

    inlines = [SubTask]
    list_display = ('title', 'taskType', 'subTasksCount', 'parent', 'weekly', 'isTeamTask', 'tag_list')
    list_display_links = ('title', 'parent', 'weekly')
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


class WeeklyTaskAdmin(admin.ModelAdmin):
    inlines = [TaskInline]

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

    list_display = ('title', 'taskType', 'subTasksCount', 'isTeamTask', 'tag_list')
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


class QuestionAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

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

class TestUserInline(admin.StackedInline):
    extra = 0
    # max_num = 10
    model = Test.users.through
    fields = (
        ('user',
         'status',),
        ('rightAnswersCount',
         'completeTime',
         'points',
         'hasLeftTest',)
    )
    readonly_fields = ('rightAnswersCount', 'completeTime')

class TestBlockInline(admin.StackedInline):
    extra = 0
    # max_num = 10
    model = TestBlock
            
    fieldsets = (
        (None, {
            'fields': (
            ('questionTheme',
            'questionsCount',
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
    inlines = [TestBlockInline,TestUserInline]

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
            'isInterview',
            'canSeeSpentTime',
            'canSeeTestClosing',
        )
    }),)

    filter_horizontal = ()
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(QuestionTheme, QuestionThemeAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Division, DivisionAdmin)
admin.site.register(JobPosition, JobPositionAdmin)
admin.site.register(WeeklyTask, WeeklyTaskAdmin)
