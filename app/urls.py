from django.urls import path
from . import Hod_Views, views, Staff_Views, Student_Views

urlpatterns = [
    path('base', views.BASE, name='base'),

    # Login
    path('', views.Login, name="Login"),
    path('doLogin', views.doLogin, name="doLogin"),  # type: ignore
    path('doLogout', views.doLogout, name="doLogout"),
    path('profile', views.PROFILE, name='profile'),
    path('profile/update', views.PROFILE_UPDATE, name='update_profile'),


    # path('check_username', views.check_username, name='check_username'),
    path('check_email_exist/', Hod_Views.check_email_exist,
         name="check_email_exist"),
    path('check_username_exist/', Hod_Views.check_username_exist,
         name="check_username_exist"),


    # HOD
    path('Hod/home', Hod_Views.HOME, name="Hod_home"),

    # HOD STUDENT
    path('Hod/Student/Add', Hod_Views.Add_Student, name='add_student'),
    path('Hod/Student/Edit/<int:id>', Hod_Views.Edit_Student, name='edit_student'),
    path('Hod/Student/Delete/<int:id>',
         Hod_Views.Delete_Student, name='delete_student'),

    # HOD STAFF
    path('Hod/Staff/Add', Hod_Views.Add_Staff, name='add_staff'),
    path('Hod/Staff/Edit/<int:id>', Hod_Views.Edit_Staff, name='edit_staff'),
    path('Hod/Staff/Delete/<int:id>',
         Hod_Views.Delete_Staff, name='delete_staff'),

    # HOD COURSE
    path('Hod/Course/Add', Hod_Views.Add_Course, name='add_course'),
    path('Hod/Course/Edit/<int:id>', Hod_Views.Edit_Course, name='edit_course'),
    path('Hod/Course/Delete/<int:id>',
         Hod_Views.Delete_Course, name='delete_course'),

    # HOD SUBJECT
    path('Hod/Subject/Add', Hod_Views.Add_Subject, name='add_subject'),
    path('Hod/Subject/Edit', Hod_Views.Edit_Subject, name='edit_subject'),
    path('Hod/Subject/Delete/<int:id>',
         Hod_Views.Delete_Subject, name='delete_subject'),

    # HOD SUBJECT
    path('Hod/Session/Add', Hod_Views.Add_Session, name='add_session'),
    path('Hod/Session/Edit/<int:id>', Hod_Views.Edit_Session, name='edit_session'),
    path('Hod/Session/Delete/<int:id>',
         Hod_Views.Delete_Session, name='delete_session'),


    # HOD STAFF NOTI
    path('Hod/Staff/Send_Staff_Notification',
         Hod_Views.Send_Staff_Notification, name='send_staff_noti'),

    path('Hod/Staff/Save_Staff_Notification',
         Hod_Views.Save_Staff_Notification, name='save_staff_notification'),

    path('Hod/Staff/staff_leave_requests',
         Hod_Views.STAFF_LEAVE_REQUESTS, name='staff_leave_requests'),

    path('Hod/Staff/status_approved/<int:id>', Hod_Views.STATUS_APPROVED,
         name='status_approved'),

    path('Hod/Staff/status_disapproved/<int:id>', Hod_Views.STATUS_DISAPPROVED,
         name='status_disapproved'),

    path('Hod/Staff/staff_feedbacks',
         Hod_Views.ALL_STAFF_FEEDBACKS, name='all_staff_feedbacks'),

    path('Hod/Staff/update_staff_feedbacks/<int:id>',
         Hod_Views.UPDATE_STAFF_FEEDBACKS, name='update_staff_feedback'),

    path('Hod/Student/Send_Student_Notification',
         Hod_Views.Send_Student_Notification, name='send_student_noti'),

    path('Hod/Student/Save_Student_Notification',
         Hod_Views.Save_Student_Notification, name='save_student_notification'),

    path('Hod/Student/student_leave_requests',
         Hod_Views.STUDENT_LEAVE_REQUESTS, name='student_leave_requests'),

    path('Hod/Student/status_approved/<int:id>', Hod_Views.STUDENT_STATUS_APPROVED,
         name='student_status_approved'),

    path('Hod/Student/status_disapproved/<int:id>', Hod_Views.STUDENT_STATUS_DISAPPROVED,
         name='student_status_disapproved'),

    path('Hod/Student/student_feedbacks',
         Hod_Views.ALL_STUDENT_FEEDBACKS, name='all_student_feedbacks'),

    path('Hod/Student/update_student_feedbacks/<int:id>',
         Hod_Views.UPDATE_STUDENT_FEEDBACKS, name='update_student_feedback'),
    path('Hod/View_attendance', Hod_Views.VIEW_ATTENDANCE, name='view_attendance'),



    # STAFF START
    path('Staff/home', Staff_Views.HOME, name='staff_home'),
    path('Staff/Notification',
         Staff_Views.Notification, name='notification'),
    path('Staff/Mark_As_Seen/<str:status>',
         Staff_Views.Mark_As_Seen, name='mark_as_seen'),

    path('Staff/Staff_Apply_Leave', Staff_Views.STAFF_APPLY_LEAVE,
         name='staff_apply_leave'),
    path('Staff/feedback', Staff_Views.FEEDBACK, name='feedback'),

    path('Staff/staff_take_attendance',
         Staff_Views.STAFF_TAKE_ATTENDANCE, name='staff_take_attendance'),

    path('Staff/staff_save_attendance',
         Staff_Views.STAFF_SAVE_ATTENDANCE, name='staff_save_attendance'),

    path('Staff/staff_view_attendance',
         Staff_Views.STAFF_VIEW_ATTENDANCE, name='staff_view_attendance'),

    path('Staff/Add/Result', Staff_Views.STAFF_ADD_RESULT, name='add_staff_result'),
    path('Staff/Save/Result', Staff_Views.STAFF_SAVE_RESULT,
         name='staff_save_result'),


    # STUDENT STARTS
    path('Student/home', Student_Views.HOME, name='student_home'),
    path('Student/Notification',
         Student_Views.Notification, name='student_notification'),
    path('Student/Student_Mark_As_Seen/<str:status>',
         Student_Views.Mark_As_Seen, name='student_mark_as_seen'),
    path('Student/Student_Apply_Leave', Student_Views.STUDENT_APPLY_LEAVE,
         name='student_apply_leave'),
    path('Student/feedback', Student_Views.FEEDBACK, name='student_feedback'),

    path('Student/View_Attendance', Student_Views.VIEW_ATTENDANCE,
         name='student_view_attendance'),
    path('Student/View_Result',
         Student_Views.VIEW_RESULT, name='view_result'),
]
