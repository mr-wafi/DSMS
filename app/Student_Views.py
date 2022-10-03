from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# @login_required(login_url='/')
# def HOME(request):
#     context = {}

#     return render(request, 'Student/home.html', context)

@login_required(login_url='/')
def HOME(request):
    student_obj = Student.objects.get(admin=request.user.id)
    total_attendance = Attendance_Report.objects.filter(
        student_id=student_obj).count()
    attendance_present = Attendance_Report.objects.filter(
        student_id=student_obj).count()
    attendance_absent = Attendance_Report.objects.filter(
        student_id=student_obj).count()

    course_obj = Course.objects.get(id=student_obj.course_id.id)
    total_subjects = Subject.objects.filter(course_id=course_obj).count()

    subject_name = []
    data_present = []
    data_absent = []
    subject_data = Subject.objects.filter(course_id=student_obj.course_id)
    for subject in subject_data:
        attendance = Attendance.objects.filter(subject_id=subject.id)
        attendance_present_count = Attendance_Report.objects.filter(
            attendance_id__in=attendance, student_id=student_obj.id).count()
        attendance_absent_count = Attendance_Report.objects.filter(
            attendance_id__in=attendance, student_id=student_obj.id).count()
        subject_name.append(subject.name)
        data_present.append(attendance_present_count)
        data_absent.append(attendance_absent_count)

    context = {
        "total_attendance": total_attendance,
        "attendance_present": attendance_present,
        "attendance_absent": attendance_absent,
        "total_subjects": total_subjects,
        "subject_name": subject_name,
        "data_present": data_present,
        "data_absent": data_absent
    }
    return render(request, 'Student/home.html', context)


@login_required(login_url='/')
def Notification(request):
    student = Student.objects.filter(admin=request.user.id)

    for i in student:
        student_id = i.id  # type: ignore

        notification = Student_Notification.objects.filter(
            student_id=student_id)

    context = {
        'notification': notification,  # type: ignore
    }

    return render(request, 'Student/notification.html', context)


@login_required(login_url='/')
def Mark_As_Seen(request, status):
    notification = Student_Notification.objects.get(id=status)
    notification.status = 1
    notification.save()  # type: ignore
    messages.success(request, 'Notification updated successfully')
    return redirect('student_notification')


@login_required(login_url='/')
def STUDENT_APPLY_LEAVE(request):
    Sleave = Student.objects.filter(admin=request.user.id)
    for i in Sleave:
        Sid = i.id  # type: ignore
        sStudent = Student_Leave.objects.filter(student_id=Sid).order_by('-id')
 ##########################################################
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        leave_date = request.POST.get('leave_date')
        message = request.POST.get('message')

        student = Student.objects.get(admin_id=student_id)

        Student_Leave.objects.create(
            student_id=student,
            date=leave_date,
            message=message
        ).save()
        messages.success(request, 'Leave request sent successfully')
        return redirect('student_apply_leave')
    context = {
        'sStudent': sStudent  # type: ignore
    }

    return render(request, 'Student/leave_apply.html', context)


def FEEDBACK(request):
    student_id = Student.objects.get(admin=request.user.id)

    stu_feedback = Student_Feedback.objects.filter(student_id=student_id)

    if request.method == 'POST':
        feedback = request.POST.get('feedback')

        student = Student.objects.get(admin=request.user.id)

        feedBack = Student_Feedback(
            student_id=student,
            feedback=feedback,
            feedback_replay=''
        )
        feedBack.save()
        messages.success(request, 'Feedback sent successfully!!!')
        return redirect('student_feedback')

    context = {
        'stu_feedback': stu_feedback
    }

    return render(request, 'Student/student_feedback.html', context)


def VIEW_ATTENDANCE(request):
    student = Student.objects.get(admin=request.user.id)
    subjects = Subject.objects.filter(course_id=student.course_id)
    action = request.GET.get('action')

    get_subject = None
    attendance_report = None
    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            get_subject = Subject.objects.get(id=subject_id)

            attendance_report = Attendance_Report.objects.filter(
                student_id=student, attendance_id__subject_id=subject_id)

    context = {
        'subjects': subjects,
        'action': action,
        'get_subject': get_subject,
        'attendance_report': attendance_report,
    }
    return render(request, 'Student/view_attendance.html', context)


def VIEW_RESULT(request):
    mark = None
    student = Student.objects.get(admin=request.user.id)
    result = Student_Result.objects.filter(student_id=student)

    for i in result:
        assignment_mark = i.assignment_mark
        exam_mark = i.exam_mark

        mark = assignment_mark + exam_mark

    context = {
        'result': result,
        'mark': mark,
    }

    return render(request, 'Student/view_result.html', context)
