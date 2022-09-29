from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages


@login_required(login_url='/')
def HOME(request):
    student = Student.objects.count()
    staff = Staff.objects.count()
    course = Course.objects.count()
    subject = Subject.objects.count()
    student_male = Student.objects.filter(gender='Male').count()
    student_female = Student.objects.filter(gender='Female').count()
    context = {
        'student': student,
        'staff': staff,
        'course': course,
        'subject': subject,
        'student_male': student_male,
        'student_female': student_female,
    }
    return render(request, 'Hod/home.html', context)


@login_required(login_url='/')
def Add_Student(request):
    course = Course.objects.all()
    Syear = Session_Year.objects.all()
    STOD = Student.objects.all()

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'This Email Already Exist')
            return redirect('add_student')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'This Username Already Exist')
            return redirect('add_student')

        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type=3
            )
            user.set_password(password)
            user.save()

            cor_id = Course.objects.get(id=course_id)
            session_year = Session_Year.objects.get(id=session_year_id)

            student = Student(
                admin=user,
                address=address,
                session_year_id=session_year,
                course_id=cor_id,
                gender=gender,
            )
            student.save()
            messages.success(request, 'Student Added Successfully!')
            return redirect('add_student')

    context = {
        'course': course,
        'Syear': Syear,
        'STOD': STOD,

    }
    return render(request, 'Hod/add_student.html', context)


@login_required(login_url='/')
def Edit_Student(request, id):

    if request.method == "POST":
        # student_id = request.POST.get('student_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')

        user = CustomUser.objects.get(id=id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        if password != None and password != '':
            user.set_password(password)
        if profile_pic != None and profile_pic != '':
            user.profile_pic = profile_pic
        user.save()

        student = Student.objects.get(admin=id)

        student.address = address
        student.gender = gender
        course = Course.objects.get(id=course_id)
        student.course_id = course
        session_year = Session_Year.objects.get(id=session_year_id)
        student.session_year_id = session_year
        student.save()
        messages.success(request, 'Student Updated Successfully!')
        return redirect('add_student')

    return render(request, 'Hod/add_student.html')


@login_required(login_url='/')
def Delete_Student(request, id):
    CustomUser.objects.filter(id=id).delete()
    messages.success(request, 'Student Deleted Successfully')
    return redirect('add_student')

########################################################################

# STAFF START


@login_required(login_url='/')
def Add_Staff(request):
    staff = Staff.objects.all()

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'This Email Already Exist')
            return redirect('add_staff')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'This Username Already Exist')
            return redirect('add_staff')

        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type=2
            )
            user.set_password(password)
            user.save()
            staff = Staff(
                admin=user,
                address=address,
                gender=gender,
            )
            staff.save()
            messages.success(request, 'Staff Added Successfully!')
            return redirect('add_staff')

    context = {
        'staff': staff,
    }
    return render(request, 'Hod/add_staff.html', context)


@login_required(login_url='/')
def Edit_Staff(request, id):
    if request.method == "POST":
        # student_id = request.POST.get('student_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        user = CustomUser.objects.get(id=id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        if password != None and password != '':
            user.set_password(password)
        if profile_pic != None and profile_pic != '':
            user.profile_pic = profile_pic
        user.save()

        staff = Staff.objects.get(admin=id)

        staff.address = address
        staff.gender = gender
        staff.save()
        messages.success(request, 'Staff Updated Successfully!')
        return redirect('add_staff')

    return render(request, 'Hod/edit_staff.html')


@login_required(login_url='/')
def Delete_Staff(request, id):
    CustomUser.objects.filter(id=id).delete()
    messages.success(request, 'Staff Deleted Successfully')
    return redirect('add_staff')


@login_required(login_url='/')
def Add_Course(request):
    course = Course.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        Course.objects.create(
            name=name,
        ).save()

        messages.success(request, 'Course Added Successfully!')
        return redirect('add_course')
    context = {
        'course': course,
    }
    return render(request, 'Hod/add_course.html', context)


@login_required(login_url='/')
def Edit_Course(request, id):

    course = Course.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        Course.objects.filter(id=id).update(
            name=name,
        )
        messages.success(request, 'Course Updated Successfully!')
        return redirect('add_course')
    context = {
        'course': course,
    }
    return render(request, 'Hod/add_course.html', context)


@login_required(login_url='/')
def Delete_Course(request, id):
    Course.objects.filter(id=id).delete()
    messages.success(request, 'Course Deleted Successfully')
    return redirect('add_course')


@login_required(login_url='/')
def Add_Subject(request):
    subject = Subject.objects.all()
    courses = Course.objects.all()
    staffs = Staff.objects.all()

    if request.method == "POST":
        subject_name = request.POST.get('name')
        course_id = request.POST.get('course')
        staff_id = request.POST.get('staff')

        course = Course.objects.get(id=course_id)
        staff = Staff.objects.get(id=staff_id)

        Subject.objects.create(
            name=subject_name,
            course_id=course,
            staff=staff
        ).save()
        messages.success(request, 'Staff Added Successfully!')
        return redirect('add_subject')

    context = {
        'courses': courses,
        'staffs': staffs,
        'subject': subject
    }
    return render(request, 'Hod/add_subject.html', context)


@login_required(login_url='/')
def Edit_Subject(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        subject_name = request.POST.get('name')
        course_id = request.POST.get('course')
        staff_id = request.POST.get('staff')

        course = Course.objects.get(id=course_id)
        staff = Staff.objects.get(id=staff_id)

        subject = Subject(
            id=subject_id,
            name=subject_name,
            course=course,
            staff=staff
        )
        subject.save()
        messages.success(request, 'Staff Updated Successfully!')
        return redirect('add_subject')
    return render(request, 'Hod/add_subject.html')


@login_required(login_url='/')
def Delete_Subject(request, id):
    Subject.objects.filter(id=id).delete()
    messages.success(request, 'Subject Deleted Successfully')
    return render(request, 'Hod/add_subject.html')


@login_required(login_url='/')
def Add_Session(request):
    session_year = Session_Year.objects.all()
    if request.method == "POST":
        session_start_year = request.POST.get('session_start_year')
        session_end_year = request.POST.get('session_end_year')

        Session = Session_Year(
            session_start=session_start_year,
            session_end=session_end_year,
        )
        Session.save()

        messages.success(request, 'Session Added Successfully!')
        return redirect('add_session')
    context = {
        'session_year': session_year,
    }
    return render(request, 'Hod/add_session.html', context)


@login_required(login_url='/')
def Edit_Session(request, id):
    if request.method == "POST":
        session_start_year = request.POST.get('session_start_year')
        session_end_year = request.POST.get('session_end_year')

        Session_Year.objects.filter(id=id).update(
            session_start=session_start_year,
            session_end=session_end_year,
        )
        messages.success(request, 'Session Updated Successfully!')
        return redirect('add_session')
    return render(request, 'Hod/add_session.html')


@login_required(login_url='/')
def Delete_Session(request, id):
    Session_Year.objects.filter(id=id).delete()
    messages.success(request, 'Session Deleted Successfully')
    return redirect('add_session')


@login_required(login_url='/')
def Send_Staff_Notification(request):
    staff = Staff.objects.all()
    Notification = Staff_Notification.objects.all().order_by('-id')[0:5]

    context = {
        'staff': staff,
        'Notification': Notification

    }
    return render(request, 'Hod/staff_notification.html', context)


@login_required(login_url='/')
def Save_Staff_Notification(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        message = request.POST.get('message')

        staff = Staff.objects.get(admin=staff_id)
        notification = Staff_Notification(
            staff_id=staff,
            message=message,
        )
        notification.save()
        messages.success(
            request, f"Notification Sent Successfully")
        return redirect('send_staff_noti')

    return render(request, 'Hod/staff_notification.html')


@login_required(login_url='/')
def STAFF_LEAVE_REQUESTS(request):
    Sleave = Staff_leave.objects.all()
    context = {'Sleave': Sleave}

    return render(request, 'Hod/staff_leave_requests.html', context)


@login_required(login_url='/')
def STATUS_APPROVED(request, id):
    approve = Staff_leave.objects.get(id=id)
    approve.status = 1
    approve.save()
    messages.success(request, 'Approved Successfully!')
    return redirect('staff_leave_requests')


@login_required(login_url='/')
def STATUS_DISAPPROVED(request, id):
    approve = Staff_leave.objects.get(id=id)
    approve.status = 2
    approve.save()
    messages.success(request, 'Disapproved Successfully!')
    return redirect('staff_leave_requests')


@login_required(login_url='/')
def ALL_STAFF_FEEDBACKS(request):
    staff_feedback = Staff_Feedback.objects.all()
    context = {
        'staff_feedback': staff_feedback
    }

    return render(request, 'Hod/hod_staff_feedback.html', context)


@login_required(login_url='/')
def UPDATE_STAFF_FEEDBACKS(request, id):
    staff_feedback = Staff_Feedback.objects.all()

    if request.method == 'POST':
        feedback_replay = request.POST.get('feedback_replay')

        Staff_Feedback.objects.filter(id=id).update(
            feedback_replay=feedback_replay
        )
        messages.success(request, 'Hod Replied Successfully!!')
        return redirect('all_staff_feedbacks')

    context = {
        'staff_feedback': staff_feedback
    }

    return render(request, 'Hod/hod_staff_feedback.html', context)


@login_required(login_url='/')
def Send_Student_Notification(request):
    student = Student.objects.all()
    Notification = Student_Notification.objects.all().order_by('-id')[0:5]

    context = {
        'student': student,
        'Notification': Notification

    }
    return render(request, 'Hod/student_notification.html', context)


@login_required(login_url='/')
def Save_Student_Notification(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        message = request.POST.get('message')

        student = Student.objects.get(admin=student_id)
        notification = Student_Notification(
            student_id=student,
            message=message,
        )
        notification.save()
        messages.success(
            request, f"Notification Sent Successfully")
        return redirect('send_student_noti')

    return render(request, 'Hod/student_notification.html')


@login_required(login_url='/')
def STUDENT_LEAVE_REQUESTS(request):
    Sleave = Student_Leave.objects.all()
    context = {'Sleave': Sleave}

    return render(request, 'Hod/student_leave_requests.html', context)


@login_required(login_url='/')
def STUDENT_STATUS_APPROVED(request, id):
    approve = Student_Leave.objects.get(id=id)
    approve.status = 1
    approve.save()
    messages.success(request, 'Approved Successfully!')
    return redirect('student_leave_requests')


@login_required(login_url='/')
def STUDENT_STATUS_DISAPPROVED(request, id):
    approve = Student_Leave.objects.get(id=id)
    approve.status = 2
    approve.save()
    messages.success(request, 'Disapproved Successfully!')
    return redirect('student_leave_requests')


@login_required(login_url='/')
def ALL_STUDENT_FEEDBACKS(request):
    student_feedback = Student_Feedback.objects.all()
    context = {
        'student_feedback': student_feedback
    }

    return render(request, 'Hod/hod_student_feedback.html', context)


@login_required(login_url='/')
def UPDATE_STUDENT_FEEDBACKS(request, id):
    student_feedback = Student_Feedback.objects.all()

    if request.method == 'POST':
        feedback_replay = request.POST.get('feedback_replay')

        Student_Feedback.objects.filter(id=id).update(
            feedback_replay=feedback_replay
        )
        messages.success(request, 'Hod Replied Successfully!!')
        return redirect('all_student_feedbacks')

    context = {
        'student_feedback': student_feedback
    }

    return render(request, 'Hod/hod_student_feedback.html', context)


def VIEW_ATTENDANCE(request):

    subject = Subject.objects.all()
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

    return render(request, 'Hod/view_attendance.html', context)
