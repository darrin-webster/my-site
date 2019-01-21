# im port models od django database
import datetime

from django.db import models
from django.utils import timezone

# class qeustion
class Question(models.Model):
	#form field for question; a character field not to exceed 200 chars
    question_text = models.CharField(max_length=200)
    # Logs date when published
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)    

# class choice
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


# The code is straightforward. Each model is represented by a class that subclasses django.db.models.Model. 
# Each model has a number of class variables, each of which represents a database field in the model.

# Each field is represented by an instance of a Field class – e.g., CharField for character fields and 
# DateTimeField for datetimes. This tells Django what type of data each field holds.
