from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Todo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    todo_detail = models.CharField(max_length=100)
    created_time = models.DateTimeField(blank=False)
    priority = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)]
     )
    
    def __str__(self) -> str:
        return self.todo_detail
    
    