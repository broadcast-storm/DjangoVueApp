from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.CharField(max_length=1000)
    picture = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class JobPosition(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.title


class UserType(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.title


class Division(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.title


class Profile(models.Model):
    jobPosition_id = models.ForeignKey(JobPosition, on_delete=models.CASCADE)
    userType_id = models.ForeignKey(UserType, on_delete=models.CASCADE)
    division_id = models.ForeignKey(Division, on_delete=models.CASCADE)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    surname = models.CharField(max_length=100, blank=True)
    patronymic = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=200, blank=True)
    email = models.EmailField()
    photo = models.ImageField()
    level = models.IntegerField(default=0)
    money = models.IntegerField(default=0)
    health = models.IntegerField(default=0)
    energy = models.IntegerField(default=0)
    quality = models.FloatField(default=0.0)
    productivity = models.FloatField(default=0.0)
    competitionCount = models.IntegerField(default=0)
    winCompetitionCount = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

class Statistics(models.Model):
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)

    level = models.IntegerField(default=0)
    quality = models.FloatField(default=0.0)
    productivity = models.FloatField(default=0.0)
    completedTests = models.IntegerField(default=0)
    completedTasks = models.IntegerField(default=0)
    completedQuests = models.IntegerField(default=0)
    achievements = models.IntegerField(default=0)
    competitions = models.IntegerField(default=0)
    competitionWins = models.IntegerField(default=0)

    def __str__(self):
        return self.id

class Reward(models.Model):
    money = models.IntegerField(default=0)
    health = models.IntegerField(default=0)
    energy = models.IntegerField(default=0)

    def __str__(self):
        return self.id


class TaskType(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.title


class Task(models.Model):
    taskType_id = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    parentTask_id = models.ForeignKey('self', models.SET_NULL,
                                      blank=True,
                                      null=True, )
    reward_id = models.ForeignKey(Reward, on_delete=models.CASCADE)

    title = models.CharField(max_length=120)
    description = models.CharField(max_length=1000)
    isTeamTask = models.BooleanField(default=False)
    isHavingSubtask = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class MainQuest(models.Model):
    reward_id = models.ForeignKey(Reward, on_delete=models.CASCADE)
    tasks = models.ManyToManyField(Task, through='MainQuestTree', through_fields=('mainQuest_id', 'task_id'), )

    title = models.CharField(max_length=120)
    description = models.CharField(max_length=1000)
    deadline = models.IntegerField(default=0)
    accessLevel = models.IntegerField(default=0)
    taskCount = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class MainQuestTree(models.Model):
    mainQuest_id = models.ForeignKey(MainQuest, on_delete=models.CASCADE)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='task_id')
    parentTask = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='parentTask')
    childTask = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='childTask')

    treeLevel = models.IntegerField(default=0)
    treePosition = models.IntegerField(default=0)

    def __str__(self):
        return self.mainQuest_id


class TaskTypeQuest(models.Model):
    task_id = models.OneToOneField(Task, on_delete=models.CASCADE)
    accessLevel = models.IntegerField(default=0)

    def __str__(self):
        return self.task_id


class TaskTypeDaily(models.Model):
    task_id = models.OneToOneField(Task, on_delete=models.CASCADE)
    deadline = models.IntegerField(default=0)

    def __str__(self):
        return self.task_id
