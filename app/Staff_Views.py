from django.shortcuts import redirect, render
from .models import Attendance, Attendance_Report, CustomUser, Session_Year, Staff_Feedback, Staff_Notification, Staff, Staff_leave, Student, Student_Result, Subject
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def HOME(request):
    context = {}

    return render(request, 'Staff/home.html', context)


@login_required(login_url='/')
def Notification(request):
    staff = Staff.objects.filter(admin=request.user.id)

    for i in staff:
        staff_id = i.id  # type: ignore

        notification = Staff_Notification.objects.filter(staff_id=staff_id)

    context = {
        'notification': notification,  # type: ignore
    }

    return render(request, 'Staff/notification.html', context)


@login_required(login_url='/')
def Mark_As_Seen(request, status):
    notification = Staff_Notification.objects.get(id=status)
    notification.status = 1
    notification.save()  # type: ignore
    messages.success(request, 'Notification updated successfully')
    return redirect('notification')


@login_required(login_url='/')
def STAFF_APPLY_LEAVE(request):
    Sleave = Staff.objects.filter(admin=request.user.id)
    for i in Sleave:
        Sid = i.id  # type: ignore
        sStaff = Staff_leave.objects.filter(staff_id=Sid).order_by('-id')
 ##########################################################
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        leave_date = request.POST.get('leave_date')
        message = request.POST.get('message')

        staff = Staff.objects.get(admin_id=staff_id)

        print(staff_id, staff)

        Staff_leave.objects.create(
            staff_id=staff,
            date=leave_date,
            message=message
        ).save()
        messages.success(request, 'Leave request sent successfully')
        return redirect('staff_apply_leave')
    context = {
        'sStaff': sStaff  # type: ignore
    }

    return render(request, 'Staff/leave_apply.html', context)


def FEEDBACK(request):
    staff_id = Staff.objects.get(admin=request.user.id)

    Staff_feedback = Staff_Feedback.objects.filter(staff_id=staff_id)

    if request.method == 'POST':
        feedback = request.POST.get('feedback')

        staff = Staff.objects.get(admin=request.user.id)

        feedBack = Staff_Feedback(
            staff_id=staff,
            feedback=feedback,
            feedback_replay=''
        )
        feedBack.save()
        messages.success(request, 'Feedback sent successfully!!!')
        return redirect('feedback')

    context = {
        'Staff_feedback': Staff_feedback
    }

    return render(request, 'Staff/staff_feedback.html', context)


def STAFF_TAKE_ATTENDANCE(request):
    staff_id = Staff.objects.get(admin=request.user.id)
    subject = Subject.objects.filter(staff_id=staff_id)
    session_year = Session_Year.objects.all()
    action = request.GET.get('action')

    get_subject = None
    get_session_year = None
    students = None

    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')

            get_subject = Subject.objects.get(id=subject_id)
            get_session_year = Session_Year.objects.get(id=session_year_id)

            subject = Subject.objects.filter(id=subject_id)
            for i in subject:
                student_id = i.course_id.id  # type:ignore
                students = Student.objects.filter(course_id=student_id)

    context = {
        'subject': subject,
        'session_year': session_year,
        'get_subject': get_subject,
        'get_session_year': get_session_year,
        'action': action,
        'students': students
    }

    return render(request, 'Staff/take_attendance.html', context)


def STAFF_SAVE_ATTENDANCE(request):
    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        session_year_id = request.POST.get('session_year_id')
        attendance_date = request.POST.get('attendance_date')
        students_id = request.POST.getlist('students_id')

        get_subject = Subject.objects.get(id=subject_id)
        get_session_year = Session_Year.objects.get(id=session_year_id)

        attendance = Attendance(
            subject_id=get_subject,
            session_year_id=get_session_year,
            attendance_data=attendance_date
        )
        attendance.save()

        for i in students_id:
            stud_id = i
            int_stud = int(stud_id)

            p_students = Student.objects.get(id=int_stud)
            attendance_report = Attendance_Report(
                student_id=p_students,
                attendance_id=attendance,
            )
            attendance_report.save()
    messages.success(request, 'Attendance Done successfully!!!')
    return redirect('staff_take_attendance')


def STAFF_VIEW_ATTENDANCE(request):
    staff_id = Staff.objects.get(admin=request.user.id)

    subject = Subject.objects.filter(staff_id=staff_id)
    session_year = Session_Year.objects.all()
    action = request.GET.get('action')

    get_subject = None
    get_session_year = None
    attendance_date = None
    attendance_report = None

    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')
            attendance_date = request.POST.get('attendance_date')

            get_subject = Subject.objects.get(id=subject_id)
            get_session_year = Session_Year.objects.get(id=session_year_id)

            attendance = Attendance.objects.filter(
                subject_id=get_subject, attendance_data=attendance_date)

            for i in attendance:
                attendance_id = i.id  # type:ignore
                attendance_report = Attendance_Report.objects.filter(
                    attendance_id=attendance_id)

    context = {
        'subject': subject,
        'session_year': session_year,
        'action': action,
        'get_subject': get_subject,
        'get_session_year': get_session_year,
        'attendance_date': attendance_date,
        'attendance_report': attendance_report,
    }
    return render(request, 'Staff/view_attendance.html', context)


def STAFF_ADD_RESULT(request):
    staff = Staff.objects.get(admin=request.user.id)

    subjects = Subject.objects.filter(staff_id=staff)
    session_year = Session_Year.objects.all()
    action = request.GET.get('action')
    get_subject = None
    get_session = None
    students = None
    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')

            get_subject = Subject.objects.get(id=subject_id)
            get_session = Session_Year.objects.get(id=session_year_id)

            subjects = Subject.objects.filter(id=subject_id)
            for i in subjects:
                student_id = i.course_id.id  # type:ignore
                students = Student.objects.filter(course_id=student_id)

    context = {
        'subjects': subjects,
        'session_year': session_year,
        'action': action,
        'get_subject': get_subject,
        'get_session': get_session,
        'students': students,
    }

    return render(request, 'Staff/add_staff_result.html', context)


def STAFF_SAVE_RESULT(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        session_year_id = request.POST.get('session_year_id')
        student_id = request.POST.get('student_id')
        assignment_mark = request.POST.get('assignment_mark')
        exam_mark = request.POST.get('exam_mark')

        get_student = Student.objects.get(admin=student_id)
        get_subject = Subject.objects.get(id=subject_id)

        check_exists = Student_Result.objects.filter(
            subject_id=get_subject, student_id=get_student).exists()
        if check_exists:
            result = Student_Result.objects.get(
                subject_id=get_subject, student_id=get_student)
            result.assignment_mark = assignment_mark
            result.exam_mark = exam_mark
            result.save()
            messages.success(request, 'Result Updated Successfully!!')
            return redirect('add_staff_result')
        else:
            result = Student_Result(
                student_id=get_student,
                subject_id=get_subject,
                assignment_mark=assignment_mark,
                exam_mark=exam_mark
            )
            result.save()
            messages.success(request, 'Result Added Successfully!!!')
            return redirect('add_staff_result')

    context = {}

    return render(request, 'Staff/add_staff_result.html', context)
