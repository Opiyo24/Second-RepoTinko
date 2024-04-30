from django.contrib.auth.models import User
from django.db import models
from team.models import Team

# Create your models here.
class Comment(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)

        
    def __str__(self):
        return self.comment
    
    def number_of_comments(self):
        return self.comments.count()


class Client(models.Model):
    name = models.CharField(max_length =200)
    team = models.ForeignKey(Team, related_name='clients',on_delete= models.CASCADE)
    comments = models.ManyToManyField(Comment, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Todolist(models.Model):
    client = models.ForeignKey(Client, related_name='todolists', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    comments = models.ManyToManyField(Comment, blank=True)
    created_by = models.ForeignKey(User, related_name='todolists', on_delete=models.CASCADE)
    changed_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name