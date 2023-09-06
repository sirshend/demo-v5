from django.urls import path
from .views import register_user, login_user, student_checklist_todo, generate_transcript_till_now, apply_for_courseC, approve_courseC, reject_courseC, assign_grade_courseC, get_student_grade_courseC, get_student_application_courseC, apply_for_courseD, approve_courseD, reject_courseD, assign_grade_courseD, get_student_grade_courseD, get_student_application_courseD, apply_for_qual, approve_qual, assign_grade_qual, check_status_qual, get_grade_qual, apply_for_thesis1, approve_thesis1, add_extra_thesis1_advisor, assign_grade_thesis1, check_status_thesis1, get_grade_thesis1, apply_for_thesis2, approve_thesis2, assign_grade_thesis2, check_status_thesis2, get_grade_thesis2, apply_for_sota, approve_sota, add_extra_sota_advisor, assign_grade_sota, check_status_sota, get_grade_sota, apply_for_defence, approve_defence, add_extra_defence_advisor, assign_grade_defence, check_status_defence, get_grade_defence, apply_for_monitoring, approve_monitoring, comment_student, check_status_monitoring, read_comment

urlpatterns = [
    # Login - register APIs
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    # APIs for seeing the timeline or checklist for the student, can be called anytime to get an overview.
    # APIs for generating transcripts of the progress made so far, this can also be called anytime
    path('student-checklist-TO-DO/', student_checklist_todo, name='student-checklist-TO-DO'),
    path('generate-transcript-till-now',generate_transcript_till_now, name='generate-transcript-till-now'),
    ################### APIs for Courses: Say just two courses C and D are there now ##########################################################
    ######## Need to add the the other two courseC related APIs. These are just backend, so no need to recompile and fetch the ABI.
    ##################### Course C (this is also a pre-req of Course D) #####################################
    #########################################################################################################
    path('apply-courseC/', apply_for_courseC, name='apply-courseC'),
    path('approve-courseC/', approve_courseC, name='approve-courseC'),
    path('reject-courseC/',reject_courseC, name='reject-courseC'),
    path('assign-grade-courseC/', assign_grade_courseC, name='assign-grade-courseC'),
    path('get-student-grade-courseC/',get_student_grade_courseC, name='get-student-grade-courseC'),
    path('get-student-application-status-courseC/',get_student_application_courseC,name='get-student-application-status-courseC'),
    #################### Course D  (their credits will determine whether you can take part in qualifying exams or not ) ###########
    ###############################################################################################################################
    path('apply-courseD/', apply_for_courseD, name='apply-courseD'),
    path('approve-courseD/', approve_courseD, name='approve-courseD'),
    path('reject-courseD/',reject_courseD, name='reject-courseD'),
    path('assign-grade-courseD/', assign_grade_courseD, name='assign-grade-courseD'),
    path('get-student-grade-courseD/',get_student_grade_courseD, name='get-student-grade-courseD'),
    path('get-student-application-status-courseD/',get_student_application_courseD,name='get-student-application-status-courseD'),
    ###################### Qualifying exam #############################################################################
    #################### can appear for qualifying exam iff you have done minimum 20 course creidts ####################
    path('apply-for-qual/', apply_for_qual, name='apply-for-qual'),
    path('approve-qual/', approve_qual, name='approve-qual'),
    path('assign-grade-qual/', assign_grade_qual, name='assign-grade-qual'),
    path('check-status-qual/', check_status_qual, name='check-status-qual'),
    path('get-grade-qual/',get_grade_qual,name='get-grade-qual'),
    ###################### thesis - 1 (first credits of thesis work) ################################################
    ################### can apply for thesis-1 iff you have passed the qualifying exam ##############################
    path('apply-for-thesis1/', apply_for_thesis1, name='apply-for-thesis-1'),
    path('approve-thesis1/', approve_thesis1, name='approve-thesis1'),
    path('add-extra-thesis1-advisor/',add_extra_thesis1_advisor,name='add-extra-thesis1-advisor'),
    path('assign-grade-thesis1/', assign_grade_thesis1, name='assign-grade-thesis1'),
    path('check-status-thesis1/', check_status_thesis1, name='check-status-thesis1'),
    path('get-grade-thesis1/',get_grade_thesis1,name='get-grade-thesis1'),
    ###################### thesis - 2 (second credits of thesis work) ######################################
    ################### can apply for thesis-2 iff you have completed thesis-1  ############################
    ############## Thesis 2 must have the same set of advisors as thesis 1 #################################
    ################ So need have the functionality/API for an extra thesis advisor here ###################
    path('apply-for-thesis2/', apply_for_thesis2, name='apply-for-thesis-2'),
    path('approve-thesis2/', approve_thesis2, name='approve-thesis2'),
    path('assign-grade-thesis2/', assign_grade_thesis2, name='assign-grade-thesis2'),
    path('check-status-thesis2/', check_status_thesis2, name='check-status-thesis2'),
    path('get-grade-thesis2/',get_grade_thesis2,name='get-grade-thesis2'),
   ###############################################################################################################################
   ######################## SOTA .. can be done anytime after quals (even before thesis credits are over) ########################
   ####################### SOTA professors' committee should have atleast all the thesis advisers as well ########################
   ################### Some extra profs can also be added to SOTA committee by thesis adviser ####################################
   ###############################################################################################################################
   path('apply-for-sota/', apply_for_sota, name='apply-for-sota'),
   path('approve-sota/', approve_sota, name='approve-sota'),
   path('add-extra-sota-advisor/',add_extra_sota_advisor,name='add-extra-sota-advisor'),
   path('assign-grade-sota/', assign_grade_sota, name='assign-grade-sota'),
   path('check-status-sota/', check_status_sota, name='check-status-sota'),
   path('get-grade-sota/',get_grade_sota,name='get-grade-sota'),
   ######################## Defence .. can be done anytime after both SOTA and thesis credits are OVER ########################
   ####################### Defence committee should have atleast all the thesis advisers as well ########################
   ################### Some extra profs can also be added to Defence committee by thesis adviser ####################################
   ###############################################################################################################################
   path('apply-for-defence/', apply_for_defence, name='apply-for-defence'),
   path('approve-defence/', approve_defence, name='approve-defence'),
   path('add-extra-defence-advisor/',add_extra_defence_advisor,name='add-extra-defence-advisor'),
   path('assign-grade-defence/', assign_grade_defence, name='assign-grade-defence'),
   path('check-status-defence/', check_status_defence, name='check-status-defence'),
   path('get-grade-defence/',get_grade_defence,name='get-grade-defence'),
   ###################### Monitoring committee###############################################
   path('apply-for-monitoring/',apply_for_monitoring, name='apply-for-monitoring'),
   path('approve-monitoring/',approve_monitoring, name='approve-monitoring'),
   path('comment-student/',comment_student,name='comment-student'),
   path('check-status-monitoring/',check_status_monitoring,name='check-status-monitoring'), 
   path('read-comment/',read_comment,name='read-comment')
]

#########################################################
#########################################################


