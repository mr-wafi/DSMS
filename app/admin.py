from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class UserModel(UserAdmin):
    list_display = ['username', 'user_type']


admin.site.register(CustomUser, UserModel)
admin.site.register([Course, Session_Year, Student, Staff,
                    Subject, Staff_Notification, Staff_leave,
                    Staff_Feedback, Student_Notification,
                    Student_Leave, Student_Feedback,
                    Attendance, Attendance_Report, Student_Result
                     ])
