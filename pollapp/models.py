from django.db import models
from users.models import MyUser
from django.utils import timezone

class Poll(models.Model):
    question = models.TextField()
    option_one = models.CharField(max_length=30)
    option_two = models.CharField(max_length=30)
    option_three = models.CharField(max_length=30)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)
    name = models.ForeignKey('users.MyUser', null=True, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add= True)


    class Meta:
        indexes = [
            models.Index(fields=['name', 'created_on'])
            ]

    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count