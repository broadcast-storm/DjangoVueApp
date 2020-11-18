from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, Task, WeeklyTask


# Register your models here.


class UserProfileAdmin(UserAdmin):
    list_display = ('email', 'username', 'name', 'surname', 'last_login', 'userType')
    search_fields = ('email', 'name', 'surname')
    readonly_fields = ('date_joined', 'last_login', 'username', 'email')
    filter_horizontal = ()
    fieldsets = ()
    list_filter = ()
    fields = ('username', 'email',
              ('name', 'surname', "patronymic"),
              "birthDate",
              ("userType", "jobPosition_id", "division_id"),
              "description", "photo",
              ("money", "health", "energy"),
              ("level", "quality", "productivity"),
              ("competitionCount", "winCompetitionCount"),
              "last_login", "date_joined")


class SubTask(admin.StackedInline):
    model = Task
    extra = 1
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
    fields = (
        'taskType',
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


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(WeeklyTask, WeeklyTaskAdmin)
