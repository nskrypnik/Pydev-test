
from django.contrib.auth.models import User 
from django.db.models import Model, CharField, TextField, ForeignKey, DateField, TextField, PositiveIntegerField 
from datetime import datetime

# Create your models here.

class Assignee(Model):
    "Use this to assign person to be responsible for task"
    user = ForeignKey(User)

class AbstractTask(Model):
    
    class Meta:
        abstract = True
    
    title = CharField(max_length=128, blank=False, null=False) # I use explicit setting for some parameters for self documenting of code
    description = TextField(null=True, default=None, blank=True)
    create_date = DateField(default = datetime.now(), null=False) # Create date
    start_date = DateField(default = datetime.now(), null=False)
    duration = PositiveIntegerField(null=False) # Duration of tasks in days
    done_percentage = PositiveIntegerField(null=False)
    assignee = ForeignKey(Assignee, null=True) # May be we want to have some tasks without person who is responsible for it 
    
class Project(AbstractTask):
    '''
    Project model, but according to picture it may be and project phase.
    Anyway we inherit it from Task model cause it's close to it
    
    '''
    parent = ForeignKey('self')
    
class Task(AbstractTask):
    
    project = ForeignKey(Project)