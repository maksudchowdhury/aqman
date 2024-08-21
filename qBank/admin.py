from django.contrib import admin
from .models import * #importing all models from models.py of this app

##############################################  Custom user admin panel  ##############################################

from django.contrib.auth.admin import UserAdmin #for custom user admin
class memberAdmin(UserAdmin):
    list_display = ('email','username','inst_emp_id','date_joined','last_login','is_admin','is_staff','is_active')
    search_fields = ('email','username','inst_emp_id')
    readonly_fields = ('member_id','date_joined','last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ('email',)
admin.site.register(member,memberAdmin) #registering custom user model with custom user admin

##############################################  ++++++++++++++++++++  ##############################################

class otpAdmin(admin.ModelAdmin):
  list_display = ('otp_id','member_email','date_time','expire_time','otp_status','purpose','otp_code')

class questionAdmin(admin.ModelAdmin):
   list_display=('question_title','submitter_id','submission_date')
admin.site.register(exam_info)
admin.site.register(otp_table,otpAdmin)
admin.site.register(question,questionAdmin)
admin.site.register(exam_question_history)
admin.site.register(fileUploads)