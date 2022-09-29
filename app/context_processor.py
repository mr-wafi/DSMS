# from .models import Staff_Notification, Staff


# def notification_renderer(request):
#     staff = Staff.objects.filter(admin=request.user.id)

#     for i in staff:
#         staff_id = i.id

#         staff_notification = Staff_Notification.objects.filter(
#             staff_id=staff_id, status=0)[0:3]

#     return {
#         'staff_notification': staff_notification,  # type: ignore
#     }
