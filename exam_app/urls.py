from django.urls import path
from .views import register_user, login_user, apply_for_courseC, approve_courseC, reject_courseC, apply_for_thesis1, approve_thesis1, assign_grade_thesis1, check_status_thesis1

urlpatterns = [
    # Login - register APIs
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    # APIs for exams: qualifying, thesis-1, thesis-2. SOTA, Defence
    path('apply-for-thesis1/', apply_for_thesis1, name='apply-for-thesis-1'),
    path('approve-thesis1/', approve_thesis1, name='approve-thesis1'),
    path('assign-grade-thesis1/', assign_grade_thesis1, name='assign-grade-thesis1'),
    path('check-status-thesis1/', check_status_thesis1, name='check-status-thesis1'),
    # APIs for Courses: Say just two courses C and D
    ## I have tested apply-courseC, need to test approve-courseC and reject-courseC
    ## Need to add the the other two courseC related APIs. These are just backend, so no need to recompile and find the ABI.
    path('apply-courseC/', apply_for_courseC, name='apply-courseC'),
    path('approve-courseC/', approve_courseC, name='approve-courseC'),
    path('reject-courseC/',reject_courseC, name='reject-courseC'),
]

#########################################################
#########################################################

# from django.urls import path
# from .views import register_user, login_user, apply_for_exam, approve_requests, check_status

# urlpatterns = [
#     # path('register/', register_user, name='register'),
#     # path('login/', login_user, name='login'),
#     # Add more API URLs as needed
#     path('register/', register_user, name='register'),
#     path('login/', login_user, name='login'),
#     path('apply-for-exam/', apply_for_exam, name='apply-for-exam'),
#     path('approve-requests/', approve_requests, name='approve-requests'),
#     path('check-status/', check_status, name='check-status'),
# ]

