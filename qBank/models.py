from datetime import datetime, timedelta
from django.utils import timezone as djTimeZone
from pytz import timezone
from django.conf import settings
from django.db import models
# from django_quill.fields import QuillField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager # for custom user model
import random, string
import uuid

zone=timezone(settings.TIME_ZONE)
expiration_time=datetime.now(zone)+ timedelta(seconds=120)

def genID():
	a=''.join(random.choice(string.ascii_letters) for _ in range(8))
	b=''.join(str(random.randint(0, 9)) for _ in range(8))
	return a+b


##############################################  Custom user model & manager  ##############################################
# after writing the custom user model
# check settings.py for AUTH_USER_MODEL and customBackend settings
# check admin.py for custom user admin

class memberManager(BaseUserManager):                  # must define create_user and create_superuser   
    
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError('Email is required')
        if not username:
            raise ValueError('Username is required')
        user=self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.is_active=True
        user.is_staff=True
        user.is_admin=False
        user.is_superuser=False
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,username,password=None):
        if not email:
            raise ValueError('Email is required')
        if not username:
            raise ValueError('Username is required')
        
        user=self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.is_active=True
        user.is_staff=True
        user.is_admin=True
        user.is_superuser=True
        user.save(using=self._db)
        return user


class member(AbstractBaseUser):
    # member_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    member_id=models.AutoField(primary_key=True)
    # member_id=models.CharField(primary_key=True, max_length=100, default=genID, editable=False)
    inst_emp_id=models.CharField(max_length=100)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    username=models.CharField(max_length=100, unique=True)
    email=models.EmailField(max_length=100, unique=True)
    password=models.CharField(max_length=300) 
    role=models.CharField(max_length=100) # submitter, manager
    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now=True)

    objects=memberManager()                             # must have object in model
    is_admin=models.BooleanField(default=False)         # must have column in database
    is_active=models.BooleanField(default=True)         # must have column in database
    is_staff=models.BooleanField(default=False)         # must have column in database
    is_superuser=models.BooleanField(default=False)     # must have column in database
    USERNAME_FIELD='email'                              # must have field in model
    REQUIRED_FIELDS=['username']                        # must have field in model

    def __str__(self):                                  # method to return username of object
        return str(self.member_id)
    def has_perm(self,perm,obj=None):                   # must be overwritten in model
        return self.is_admin
    def has_module_perms(self,app_label):               # must be overwritten in model
        return True
    def getUserID(self):
        return self.member_id

##############################################  ++++++++++++++++++++  ##############################################



class exam_info(models.Model):
    # exam_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    exam_id=models.AutoField(primary_key=True)
    exam_title=models.CharField(max_length=100)
    exam_date=models.DateTimeField(auto_now_add=True)
    

class otp_table(models.Model):
    # otp_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    otp_id=models.AutoField(primary_key=True)
    date_time=models.DateTimeField(auto_now=True)
    expire_time=models.DateTimeField(default=expiration_time)
    otp_status=models.CharField(max_length=100, default="active")
    purpose=models.CharField(max_length=100, default="multiple")
    member_email=models.EmailField(max_length=256)
    otp_code=models.CharField(max_length=8)
    

    def __str__(self):
        return str(self.member_email)


class question(models.Model):
    # question_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # question_id=models.AutoField(primary_key=True)
    question_id=models.CharField(primary_key=True, max_length=100, default=genID, editable=False)
    submitter_id=models.ForeignKey(member, on_delete=models.PROTECT)

    question_title=models.TextField(null=False, default="No title submitted")

    module_no=models.IntegerField(null=False, default=0)
    chapter_no=models.IntegerField(null=False, default=0)
    topic_no=models.IntegerField(null=False, default=0)
    sub_topic_no=models.IntegerField(null=False, default=0)

    question_text=models.TextField()

    choice_1=models.TextField(null=False, default="No choice submitted")
    choice_2=models.TextField(null=False, default="No choice submitted")
    choice_3=models.TextField(null=False, default="No choice submitted")
    choice_4=models.TextField(null=False, default="No choice submitted")
    answer=models.TextField(default="No answer submitted",null=False)
    
    question_status=models.CharField(max_length=100, default="pending")
    submission_date=models.DateTimeField(auto_now_add=True)
    
    

class exam_question_history(models.Model):
    # history_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    history_id=models.AutoField(primary_key=True)
    question_id=models.ForeignKey(question, on_delete=models.PROTECT)
    exam_id=models.ForeignKey(exam_info, on_delete=models.PROTECT)


class fileUploads(models.Model):
    id=models.AutoField(primary_key=True)
    doc=models.FileField(upload_to="images/",blank=True)
