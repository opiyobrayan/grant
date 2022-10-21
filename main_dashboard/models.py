
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse

# Create your models here.

class Grant(models.Model):

    THEMATIC_CHOIECES=(
        ('SRHR','SRHR'),
        ('HIV/TB','HIV/TB'),
        ('WLPR','WLPR'),
        ('SILU','SILU'),
        ('H&G','H&G')    
    )

            
    
    FREQUENCY=(
        ('Annual','Annual'),
        ('Bi-annual','Bi-annual'),    
    )
    CURRENCY=(
        ('USD','USD'),
        ('Ksh','Ksh'),   
    )

    # thematic_area=MultiSelectField(choices=THEMATIC_CHOIECES)
    thematic_area=models.CharField('Choose Thematic',choices=THEMATIC_CHOIECES,max_length=100)
    donor=models.CharField('Donor',max_length=200,blank=True,null=True)
    project_name=models.CharField('Project Name',max_length=200)
    log=models.ImageField(null=False,blank=False)
    info=RichTextUploadingField(blank=True,null=True)
    # person_responsible=MultiSelectField(PERSON_RESPONSIBLE,max_choices=3,max_length=10)
    person_responsible=models.CharField('Choose Persons',max_length=100 ,default='Jesica')

    # frequency=MultiSelectField(choices=FREQUENCY,max_choices=2,max_length=10)
    frequency=models.CharField('Choose Persons',choices=FREQUENCY,max_length=100)
    project_start=models.DateField()
    project_end=models.DateField()
    value=models.IntegerField(blank=True,null=True)
    currency=models.CharField('Choose Currency',max_length=100,choices=CURRENCY,blank=True,null=True)

    def __str__(self):
        return self.project_name

    
class Post(models.Model):
    title=models.CharField('Title',max_length=200)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body=RichTextUploadingField(blank=True, null=True)
    body2=RichTextUploadingField(blank=True, null=True,config_name='special')

    def __str__(self):

        return self.title + ' | '+str(self.author)

class ThematicMember(models.Model):
    name=models.CharField('Name',max_length=200)
    position= models.CharField('Position',max_length=200)

    def __str__(self):
        return self.name


class Thematic(models.Model):
    thematic=models.CharField('Name of Thematic',max_length=200)
    members=models.ManyToManyField(ThematicMember)  #  extension of table ThematicMember

    
    def __str__(self):
        return self.thematic
          
class ActivityType(models.Model):
    activity_type=models.CharField('Activity Type',max_length=200)
    
    def __str__(self):
        return self.activity_type


class Activity(models.Model):
    thematic=models.ForeignKey(Thematic,on_delete=models.CASCADE) 
    grant=models.ForeignKey(Grant,on_delete=models.CASCADE)            # Extension of class Grant
    activity_name=models.CharField('Activity Name',max_length=200) 
    activity_type=models.ForeignKey(ActivityType,on_delete=models.CASCADE) # extension of class Activity_Type
    venue=models.CharField('Venue',max_length=200)  # Extension of class Locaton
    activity_id=models.CharField('activity id',max_length=200)
    date_start=models.DateTimeField()
    date_end=models.DateTimeField()
    def __str__(self):
        return self.activity_name

    def save(self,*args,**kwargs):
        super().save(*args, **kwargs)
        today = date.today()
        time_now = today.strftime("%Y%m%d")
        total_dur= self.date_end-self.date_start
        dur_now=int(time_now)-int(self.date_start.strftime("%Y%m%d"))
        return str(dur_now) + "/"+ str(total_dur)


class Participant(models.Model):
    year=models.CharField('Year',max_length=100,blank=True,null=True)
    month=models.CharField('Month',max_length=100,blank=True,null=True)
    name=models.CharField('Name',max_length=200)
    gender=models.CharField('Gender',max_length=100,blank=True,null=True)
    county=models.CharField('County',max_length=100,blank=True,null=True)
    subcounty=models.CharField('Subcounty',max_length=100,blank=True,null=True)
    proffesion=models.CharField('Proffesion',max_length=100,blank=True,null=True)
    title=models.CharField('Title',max_length=100,blank=True,null=True)
    organization=models.CharField('Organization',max_length=200,blank=True,null=True)
    phone=models.CharField('Phone',max_length=100,blank=True,null=True)
    email=models.EmailField('Email',max_length=100,blank=True,null=True)
    age=models.CharField('Age',max_length=100,blank=True,null=True)
    groups=models.CharField('Groups/Stakeholders',max_length=200,blank=True,null=True)
    thematic=models.CharField('Thematic',max_length=200,blank=True,null=True)
    donor=models.CharField('Donor/Sponsered',max_length=200,blank=True,null=True)
    project=models.CharField('Project',max_length=200,blank=True,null=True)
    activity_name=models.CharField(max_length=200,blank=True,null=True)
    activity_type=models.CharField(max_length=200,blank=True,null=True)
    date=models.CharField(max_length=200,blank=True,null=True)
    start_date=models.CharField(max_length=200,blank=True,null=True)
    end_date=models.CharField(max_length=200,blank=True,null=True)
    duration=models.CharField(max_length=200,blank=True,null=True)
    venue=models.CharField(max_length=200,blank=True,null=True)
    activity_county=models.CharField(max_length=200,blank=True,null=True)
    activity_subcounty=models.CharField(max_length=200,blank=True,null=True)
    organizer=models.CharField(max_length=200,blank=True,null=True)
    budget=models.CharField(max_length=200,blank=True,null=True)
    actual=models.CharField(max_length=200,blank=True,null=True)
   
    def __str__(self):

        return self.name


        

        
