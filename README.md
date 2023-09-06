In each of shells, first do
cd .. (go to the previous level ```exam_blockchains``` for activating the virtual env)
source v1/bin/activate
cd exam_approval_backend
Once all work is done, deactivate the virtual-env with ```deactivate```

MySQL and mongod, mongosh are immaterial now. 
I have removed any mysql dependency. 
And mongo is running remotely. So no headaches about these stuffs anymore. Nice!!
<!-- sudo mongod --dbpath .
mongosh
sudo brew services start mongodb-community
While stopping:
exit from mongosh shell by pressing Ctrl+C twice
Ctrl+C from mongod.
sudo brew services stop mongodb-community

mysql.server start
sudo brew services start mysql
mysql -u root -p (and not ```mysql -u sirshendu -p 271828``` or any combination of sirshendu and/or 271828, like ```mysql -u sirshendu -p```  or ```mysql -u root -271828```)
While stopping:
```exit``` from the shell after ```mysql -u root -p```
sudo brew services stop mysql
mysql.server stop -->
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoic3R1MjA1IiwiZXhwIjoxNjk0NTk2OTU0fQ.ZzGHBMszBkUrEXhZW4b5TbMYbFJfu8IpWv-7zTETP44
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjIwNSIsImV4cCI6MTY5NDU5NzAwMn0.JynZMdogAR51TsCDW3kQzyieMKt0jHvDdQV88exzXtE

in exam_approval_backend with virtualenv on, use
python manage.py migrate
python manage.py runserver

urlpatterns = [
    # Login - register APIs
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    {
    "name": "stu1118" ,
    "role": "student" ,
    "password": "12345",
    "email": "stu1118@gmail.com"
    }
    {
    "name": "prof1118" ,
    "role": "professor" ,
    "password": "12345",
    "email": "prof1118@gmail.com"
    }
    {
    "name": "prof1119" ,
    "role": "professor" ,
    "password": "12345",
    "email": "prof1119@gmail.com"
    }
    {
    "name": "stu1118" ,
    "password": "12345",
    }
    {
    "name": "prof1118" ,
    "password": "12345",
    }
    {
    "name": "prof1119" ,
    "password": "12345",
    }
    # APIs for seeing the timeline or checklist for the student, can be called anytime to get an overview.
    # APIs for generating transcripts of the progress made so far, this can also be called anytime
    path('student-checklist-TO-DO/', student_checklist_todo, name='student-checklist-TO-DO'),
    path('generate-transcript-till-now',generate_transcript_till_now, name='generate-transcript-till-now'),
    {
    "name": "stu200",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoic3R1MjAwIiwiZXhwIjoxNjk0NTc2NTgwfQ._eJuMhw2P9SZ8qp_6BJJ9kRhiiYFKbuKSYVHuWPWJJQ"
    }
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
    apply
    {
    "name": "stu200",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoic3R1MjAwIiwiZXhwIjoxNjk0NTc2NTgwfQ._eJuMhw2P9SZ8qp_6BJJ9kRhiiYFKbuKSYVHuWPWJJQ",
    "course-prof": ["prof200"]
    }
    approve
    {
    "name": "prof200",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjIwMCIsImV4cCI6MTY5NDU3NjYwMX0.r3Y0omfEHvCSWcfZpzIPfWEyCIyn5ojffxdzK_siwUA",
    "student": ["stu200"]
    }
    assign grade
    {
    "name": "prof200",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjIwMCIsImV4cCI6MTY5NDU3NjYwMX0.r3Y0omfEHvCSWcfZpzIPfWEyCIyn5ojffxdzK_siwUA",
    "student": ["stu200"],
    "grade": "B"
    }
    reject course c or d
    {
    "name": "prof200",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjIwMCIsImV4cCI6MTY5NDU3NjYwMX0.r3Y0omfEHvCSWcfZpzIPfWEyCIyn5ojffxdzK_siwUA",
    "student": ["stu200"]
    }
    get student grade course c or D
    {
    "name": "stu200"
    }
    get student applicaation status
    {
    "name": "stu200"
    }
    ###################### Qualifying exam #############################################################################
    #################### can appear for qualifying exam iff you have done minimum 20 course creidts ####################
    path('apply-for-qual/', apply_for_qual, name='apply-for-qual'),
    path('approve-qual/', approve_qual, name='approve-qual'),
    path('assign-grade-qual/', assign_grade_qual, name='assign-grade-qual'),
    path('check-status-qual/', check_status_qual, name='check-status-qual'),
    path('get-grade-qual/',get_grade_qual,name='get-grade-qual'),
    apply for qual
    {
    "name": "stu200",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoic3R1MjAwIiwiZXhwIjoxNjk0NTc2NTgwfQ._eJuMhw2P9SZ8qp_6BJJ9kRhiiYFKbuKSYVHuWPWJJQ",
    "prof": ["prof200"]
    }
    approve qual
    {
    "name": "prof200",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjIwMCIsImV4cCI6MTY5NDU3NjYwMX0.r3Y0omfEHvCSWcfZpzIPfWEyCIyn5ojffxdzK_siwUA",
    "student": ["stu200"]
    }
    assign grade qual
    {
    "name": "prof200",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjIwMCIsImV4cCI6MTY5NDU3NjYwMX0.r3Y0omfEHvCSWcfZpzIPfWEyCIyn5ojffxdzK_siwUA",
    "student": ["stu200"],
    "grade": "S"
    }
    check status qual 
    {
    "name": "stu200",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoic3R1MjAwIiwiZXhwIjoxNjk0NTc2NTgwfQ._eJuMhw2P9SZ8qp_6BJJ9kRhiiYFKbuKSYVHuWPWJJQ"
    }
    get grade qual 
    {
    "name": "stu200"
    }
    ###################### thesis - 1 (first credits of thesis work) ################################################
    ################### can apply for thesis-1 iff you have passed the qualifying exam ##############################
    path('apply-for-thesis1/', apply_for_thesis1, name='apply-for-thesis-1'),
    {
    "name": "stu200",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoic3R1MjAwIiwiZXhwIjoxNjk0NTc2NTgwfQ._eJuMhw2P9SZ8qp_6BJJ9kRhiiYFKbuKSYVHuWPWJJQ",
    "profs_guides": ["prof200"]
    }
    path('approve-thesis1/', approve_thesis1, name='approve-thesis1'),
    {
    "name": "prof200",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjIwMCIsImV4cCI6MTY5NDU3NjYwMX0.r3Y0omfEHvCSWcfZpzIPfWEyCIyn5ojffxdzK_siwUA",
    "student": ["stu200"]
    }
    path('add-extra-thesis1-advisor/',add_extra_thesis1_advisor,name='add-extra-thesis1-advisor'),
    {
    "name": "prof1116",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjExMTYiLCJleHAiOjE2OTQ1MDQ4Mzl9.MnEAXFgUWv9lhHOdjsAyqkdhlBc7ib3p-graL4AQ-x8",
    "student": ["stu1116"],
    "extra_thesis_advisor":"prof1117"
}
    path('assign-grade-thesis1/', assign_grade_thesis1, name='assign-grade-thesis1'),
    {
    "name": "prof200",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjIwMCIsImV4cCI6MTY5NDU3NjYwMX0.r3Y0omfEHvCSWcfZpzIPfWEyCIyn5ojffxdzK_siwUA",
    "student": ["stu200"],
    "grade": "S"
    }
    path('check-status-thesis1/', check_status_thesis1, name='check-status-thesis1'),
    {
    "name": "stu200",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoic3R1MjAwIiwiZXhwIjoxNjk0NTc2NTgwfQ._eJuMhw2P9SZ8qp_6BJJ9kRhiiYFKbuKSYVHuWPWJJQ"
    }
    path('get-grade-thesis1/',get_grade_thesis1,name='get-grade-thesis1')
    {
    "name": "stu200"
    }
    ###################### thesis - 2 (second credits of thesis work) ######################################
    ################### can apply for thesis-2 iff you have completed thesis-1  ############################
    ############## Thesis 2 must have the same set of advisors as thesis 1 #################################
    ################ So need have the functionality/API for an extra thesis advisor here ###################
    path('apply-for-thesis2/', apply_for_thesis2, name='apply-for-thesis-2'),
    {
    "name": "stu200",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoic3R1MjAwIiwiZXhwIjoxNjk0NTc2NTgwfQ._eJuMhw2P9SZ8qp_6BJJ9kRhiiYFKbuKSYVHuWPWJJQ"
    }
    path('approve-thesis2/', approve_thesis2, name='approve-thesis2'),
    {
    "name": "prof200",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjIwMCIsImV4cCI6MTY5NDU3NjYwMX0.r3Y0omfEHvCSWcfZpzIPfWEyCIyn5ojffxdzK_siwUA",
    "student": ["stu200"]
    }
    path('assign-grade-thesis2/', assign_grade_thesis2, name='assign-grade-thesis2'),
    {
    "name": "prof200",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjIwMCIsImV4cCI6MTY5NDU3NjYwMX0.r3Y0omfEHvCSWcfZpzIPfWEyCIyn5ojffxdzK_siwUA",
    "student": ["stu200"],
    "grade": "S"
    }
    path('check-status-thesis2/', check_status_thesis2, name='check-status-thesis2'),
    {
    "name": "stu200",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoic3R1MjAwIiwiZXhwIjoxNjk0NTc2NTgwfQ._eJuMhw2P9SZ8qp_6BJJ9kRhiiYFKbuKSYVHuWPWJJQ"
    }
    path('get-grade-thesis2/',get_grade_thesis2,name='get-grade-thesis2'),
    {
    "name": "stu200"
    }
   ###############################################################################################################################
   ######################## SOTA .. can be done anytime after quals (even before thesis credits are over) ########################
   ####################### SOTA professors' committee should have atleast all the thesis advisers as well ########################
   ################### Some extra profs can also be added to SOTA committee by thesis adviser ####################################
   ###############################################################################################################################
   path('apply-for-sota/', apply_for_sota, name='apply-for-sota'),
   {
    "name": "stu200",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoic3R1MjAwIiwiZXhwIjoxNjk0NTc2NTgwfQ._eJuMhw2P9SZ8qp_6BJJ9kRhiiYFKbuKSYVHuWPWJJQ"
    }
   path('approve-sota/', approve_sota, name='approve-sota'),
   {
    "name": "prof200",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjIwMCIsImV4cCI6MTY5NDU3NjYwMX0.r3Y0omfEHvCSWcfZpzIPfWEyCIyn5ojffxdzK_siwUA",
    "student": ["stu200"]
    }
   path('add-extra-sota-advisor/',add_extra_sota_advisor,name='add-extra-sota-advisor'),
   {
    "name": "prof200",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjIwMCIsImV4cCI6MTY5NDU3NjYwMX0.r3Y0omfEHvCSWcfZpzIPfWEyCIyn5ojffxdzK_siwUA",
    "student": ["stu200"],
    "extra_sota_advisor":"prof201"
    }
   path('assign-grade-sota/', assign_grade_sota, name='assign-grade-sota'),
   {
    "name": "prof200",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjIwMCIsImV4cCI6MTY5NDU3NjYwMX0.r3Y0omfEHvCSWcfZpzIPfWEyCIyn5ojffxdzK_siwUA",
    "student": ["stu200"],
    "grade": "S"
    }
   path('check-status-sota/', check_status_sota, name='check-status-sota'),
   {
    "name": "stu200",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoic3R1MjAwIiwiZXhwIjoxNjk0NTc2NTgwfQ._eJuMhw2P9SZ8qp_6BJJ9kRhiiYFKbuKSYVHuWPWJJQ"
    }
   path('get-grade-sota/',get_grade_sota,name='get-grade-sota'),
   {
    "name": "stu200"
    }
   ######################## Defence .. can be done anytime after both SOTA and thesis credits are OVER ########################
   ####################### Defence committee should have atleast all the thesis advisers as well ########################
   ################### Some extra profs can also be added to Defence committee by thesis adviser ####################################
   ###############################################################################################################################
   path('apply-for-defence/', apply_for_defence, name='apply-for-defence'),
   {
    "name": "stu200",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoic3R1MjAwIiwiZXhwIjoxNjk0NTc2NTgwfQ._eJuMhw2P9SZ8qp_6BJJ9kRhiiYFKbuKSYVHuWPWJJQ"
    }
   path('approve-defence/', approve_defence, name='approve-defence'),
   {
    "name": "prof200",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjIwMCIsImV4cCI6MTY5NDU3NjYwMX0.r3Y0omfEHvCSWcfZpzIPfWEyCIyn5ojffxdzK_siwUA",
    "student": ["stu200"]
    }
   path('add-extra-defence-advisor/',add_extra_defence_advisor,name='add-extra-defence-advisor'),
   {
    "name": "prof200",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjIwMCIsImV4cCI6MTY5NDU3NjYwMX0.r3Y0omfEHvCSWcfZpzIPfWEyCIyn5ojffxdzK_siwUA",
    "student": ["stu200"],
    "extra_defence_advisor":"prof201"
    }
   path('assign-grade-defence/', assign_grade_defence, name='assign-grade-defence'),
   {
    "name": "prof200",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjIwMCIsImV4cCI6MTY5NDU3NjYwMX0.r3Y0omfEHvCSWcfZpzIPfWEyCIyn5ojffxdzK_siwUA",
    "student": ["stu200"],
    "grade": "S"
    }
   path('check-status-defence/', check_status_defence, name='check-status-defence'),
   {
    "name": "stu200",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoic3R1MjAwIiwiZXhwIjoxNjk0NTc2NTgwfQ._eJuMhw2P9SZ8qp_6BJJ9kRhiiYFKbuKSYVHuWPWJJQ"
    }
   path('get-grade-defence/',get_grade_defence,name='get-grade-defence')
   {
    "name": "stu200"
   }
]
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoic3R1MjA1IiwiZXhwIjoxNjk0NTk2OTU0fQ.ZzGHBMszBkUrEXhZW4b5TbMYbFJfu8IpWv-7zTETP44
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjIwNSIsImV4cCI6MTY5NDU5NzAwMn0.JynZMdogAR51TsCDW3kQzyieMKt0jHvDdQV88exzXtE
path('apply-for-monitoring/',apply_for_monitoring, name='apply-for-monitoring'),
{
    "name": "stu205",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoic3R1MjA1IiwiZXhwIjoxNjk0NTk2OTU0fQ.ZzGHBMszBkUrEXhZW4b5TbMYbFJfu8IpWv-7zTETP44,
    "profs": ["prof205"]
    }
   path('approve-monitoring/',approve_monitoring, name='approve-monitoring'),
    {
    "name": "prof205",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjIwNSIsImV4cCI6MTY5NDU5NzAwMn0.JynZMdogAR51TsCDW3kQzyieMKt0jHvDdQV88exzXtE",
    "student": ["stu205"]
    }
   path('comment-student/',comment_student,name='comment-student'),
   {
    "name": "prof205",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjIwNSIsImV4cCI6MTY5NDU5NzAwMn0.JynZMdogAR51TsCDW3kQzyieMKt0jHvDdQV88exzXtE",
    "student": ["stu205"],
    "comment": "good job. Nicely done!!"
    }
   path('check-status-monitoring/',check_status_monitoring,name='check-status-monitoring'), 
   {
    "name": "stu205",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoic3R1MjA1IiwiZXhwIjoxNjk0NTk2OTU0fQ.ZzGHBMszBkUrEXhZW4b5TbMYbFJfu8IpWv-7zTETP44"
    }
   path('read-comment/',read_comment,name='read-comment')
    {
    "name": "prof205",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjIwNSIsImV4cCI6MTY5NDU5NzAwMn0.JynZMdogAR51TsCDW3kQzyieMKt0jHvDdQV88exzXtE",
    "student":"stu205"
    }
Local testing of the APIs
===========================
 Student (always increase student number by 2, so we have a close extra prof)
register 
{
    "name": "stu1118" ,
    "role": "student" ,
    "password": "12345",
    "email": "stu1118@gmail.com"
}
login
{
    "name":  "stu1118",
    "password": "12345"
}

{
    "message": "User login successfully",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoic3R1MTExOCIsImV4cCI6MTY5NDUxMjg5Mn0.EIyUihYrWipJYhsLeL5UaSRqXiiYBTwQ86sRYWtHjvA"
}

{
    "name": "stu1118",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoic3R1MTExOCIsImV4cCI6MTY5NDUxMjg5Mn0.EIyUihYrWipJYhsLeL5UaSRqXiiYBTwQ86sRYWtHjvA",
    "course-prof": ["prof1118"]
}
for thesis-1
{
    "name": "stu1116",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoic3R1MTExOCIsImV4cCI6MTY5NDUxMjg5Mn0.EIyUihYrWipJYhsLeL5UaSRqXiiYBTwQ86sRYWtHjvA",
    "partners": ["prof1118"]
}
{
    "name": "stu200",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoic3R1MjAwIiwiZXhwIjoxNjk0NTc2NTgwfQ._eJuMhw2P9SZ8qp_6BJJ9kRhiiYFKbuKSYVHuWPWJJQ",
    "course-prof": ["prof200"]
}
for thesis-2, sota, defence, status checks 
{
    "name": "stu1118",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoic3R1MTExOCIsImV4cCI6MTY5NDUxMjg5Mn0.EIyUihYrWipJYhsLeL5UaSRqXiiYBTwQ86sRYWtHjvA"
}
 Teacher

 teacher 1

register 
{
    "name": "prof1118" ,
    "role": "professor" ,
    "password": "12345",
    "email": "prof1118@gmail.com"
}
login
{
    "name":  "prof1116",
    "password": "12345"
}
{
    "message": "User login successfully",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjExMTYiLCJleHAiOjE2OTQ1MDQ4Mzl9.MnEAXFgUWv9lhHOdjsAyqkdhlBc7ib3p-graL4AQ-x8"
}

{
    "name": "prof1116",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjExMTYiLCJleHAiOjE2OTQ1MDQ4Mzl9.MnEAXFgUWv9lhHOdjsAyqkdhlBc7ib3p-graL4AQ-x8",
    "students": ["stu1116"]
}

{
    "name": "prof1116",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjExMTYiLCJleHAiOjE2OTQ1MDQ4Mzl9.MnEAXFgUWv9lhHOdjsAyqkdhlBc7ib3p-graL4AQ-x8",
    "students": ["stu1116"],
    "grade": "A"
}
{
    "name": "prof1116",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjExMTYiLCJleHAiOjE2OTQ1MDQ4Mzl9.MnEAXFgUWv9lhHOdjsAyqkdhlBc7ib3p-graL4AQ-x8",
    "students": ["stu1116"],
    "extra_thesis_advisor":"prof1117"
}
 teacher 2

 register 
{
    "name": "prof1119" ,
    "role": "professor" ,
    "password": "12345",
    "email": "prof1119@gmail.com"
}
 login
{
    "name":  "prof1117",
    "password": "12345"
}
{
    "message": "User login successfully",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjExMTciLCJleHAiOjE2OTQ1MDQ3OTV9.VazaJKQaSsJ-QoaIcy_5KzvRj83n3qSZ3bHWEhPGzag"
}
{
    "name": "prof1117",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjExMTciLCJleHAiOjE2OTQ1MDQ3OTV9.VazaJKQaSsJ-QoaIcy_5KzvRj83n3qSZ3bHWEhPGzag",
    "students": ["stu1116"]
}
{
    "name": "prof1117",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjExMTciLCJleHAiOjE2OTQ1MDQ3OTV9.VazaJKQaSsJ-QoaIcy_5KzvRj83n3qSZ3bHWEhPGzag",
    "students": ["stu1116"],
    "grade": "S"
}
########################### Course types ###############################################
z1
{
    "name": "stu1113" ,
    "role": "student" ,
    "password": "12345",
    "email": "stu1113@gmail.com"
}
{
    "message": "User registered successfully",
    "private_key": "96314b41e51561690f4f3a6f812f3bf18b69ed565a8614f2aabefec9c7af0183"
}
{
    "name":  "stu1113",
    "password": "12345"
}
{
    "message": "User login successfully",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoic3R1MTExMyIsImV4cCI6MTY5NDM3NjMxOH0.tsp0sJxQdcz_Wph6QtnsTeQYVqRCmZk4_3nujcqHiDs"
}
{
    "name": "stu1113",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoic3R1MTExMyIsImV4cCI6MTY5NDM3NjMxOH0.tsp0sJxQdcz_Wph6QtnsTeQYVqRCmZk4_3nujcqHiDs",
    "course-prof": ["prof1113"]
}
{
    "name": "stu1113",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoic3R1MTExMyIsImV4cCI6MTY5NDM3NjMxOH0.tsp0sJxQdcz_Wph6QtnsTeQYVqRCmZk4_3nujcqHiDs",
    "partners": ["prof1113"]
}
z2
{
    "name": "prof1113" ,
    "role": "professor" ,
    "password": "12345",
    "email": "prof1113@gmail.com"
}
{
    "message": "User registered successfully",
    "private_key": "eea011f28b5ee3011f3e1482844663889300191ea88973299a61d7db7f2e161f"
}
{
    "name":  "prof1113",
    "password": "12345"
}
{
    "message": "User login successfully",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjExMTMiLCJleHAiOjE2OTQzNzYzODZ9.S2ceTdDj0H1q-fod2tp2HI93LzrFr5P4TUZo2hGGaYY"
}
Approve/reject course-C request by prof (format should be the same)
{
    "name": "prof1113",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjExMTMiLCJleHAiOjE2OTQzNzYzODZ9.S2ceTdDj0H1q-fod2tp2HI93LzrFr5P4TUZo2hGGaYY",
    "students": ["stu1113"]
}
Giving a grade to the student // note these grades better be A, B, C, D, E, F etc. these are not supposed to be S/X(those are for thesis types)
{
    "name": "prof1113",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjExMTMiLCJleHAiOjE2OTQzNzYzODZ9.S2ceTdDj0H1q-fod2tp2HI93LzrFr5P4TUZo2hGGaYY",
    "students": ["stu1113"],
    "grade": "A"
}
{
    "name": "prof1113",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjExMTMiLCJleHAiOjE2OTQzNzYzODZ9.S2ceTdDj0H1q-fod2tp2HI93LzrFr5P4TUZo2hGGaYY",
    "students": ["stu1113"],
    "extra_thesis_advisor":"prof111"
##################################### Thesis/Exam types ################################
z1
{
    "name": "stu4" ,
    "role": "student" ,
    "password": "12345",
    "email": "stu4@gmail.com"
}
{
    "message": "User registered successfully",
    "private_key": "96314b41e51561690f4f3a6f812f3bf18b69ed565a8614f2aabefec9c7af0183"
}
{
    "name":  "stu4",
    "password": "12345"
}
{
    "message": "User login successfully",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoic3R1NCIsImV4cCI6MTY5NDM0MDA3OX0.zEVAZYH045PW35INnehSH2dNOig4IwxwxaXGyGTdgjg"
}
{
    "name": "stu4",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoic3R1NCIsImV4cCI6MTY5NDM0MDA3OX0.zEVAZYH045PW35INnehSH2dNOig4IwxwxaXGyGTdgjg",
    "partners": ["prof111", "prof222"]
}

{
    "name": "stu4",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoic3R1NCIsImV4cCI6MTY5NDM0MDA3OX0.zEVAZYH045PW35INnehSH2dNOig4IwxwxaXGyGTdgjg"
}
######################################
z2
{
    "name": "prof111" ,
    "role": "professor" ,
    "password": "12345",
    "email": "prof111@gmail.com"
}
{
    "message": "User registered successfully",
    "private_key": "eea011f28b5ee3011f3e1482844663889300191ea88973299a61d7db7f2e161f"
}
{
    "name":  "prof111",
    "password": "12345"
}
{
    "message": "User login successfully",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjExMSIsImV4cCI6MTY5NDM0MDIyOX0.ZxDS1iWJUkxHZ35EXKvl1vXJwe8Ws2US_KzQ2H7BqHI"
}

{
    "name": "prof111",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjExMSIsImV4cCI6MTY5NDM0MDIyOX0.ZxDS1iWJUkxHZ35EXKvl1vXJwe8Ws2US_KzQ2H7BqHI",
    "students": ["stu4"],
    "grade": "S"
}


######################################
z3
{
    "name": "prof222" ,
    "role": "professor" ,
    "password": "12345",
    "email": "prof222@gmail.com"
}
{
    "message": "User registered successfully",
    "private_key": "137e979ad121dc95154755fd5da6b2c46ca9fea53f30b030c7a958e817003b94"
}
{
    "name":  "prof222",
    "password": "12345"
}
{
    "message": "User login successfully",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjIyMiIsImV4cCI6MTY5NDM0MDMzNH0.5POEoERvKsxGAfV_DNrm-uAy-eCsCgK7KhX9qFIdqPQ"
}
{
    "name": "prof222",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjIyMiIsImV4cCI6MTY5NDM0MDMzNH0.5POEoERvKsxGAfV_DNrm-uAy-eCsCgK7KhX9qFIdqPQ",
    "students": ["stu4"]
}
##########################################
##########################################
127.0.0.1:8000/api/register
{
    "name": "d" ,
    "role": "student" ,
    "password": "12345",
    "email": "abcd@gmail.com"
}
{
    "name": "s1" ,
    "role": "student" ,
    "password": "12345",
    "email": "s1@gmail.com"
}
{
    "name": "p1" ,
    "role": "professor" ,
    "password": "12345",
    "email": "p1@gmail.com"
}

{
    "name": "e" ,
    "role": "professor" ,
    "password": "12345",
    "email": "bbcd@gmail.com"
}


127.0.0.1:8000/api/login
{
    "name":  ,
    "password":
}


127.0.0.1:8000/api/apply-for-exam:

{
    "name": ,
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiYzIiLCJleHAiOjE2OTI2ODgzMzN9.RrEqiG9JbkSmah5GodyZd7NZ3-jYb7-5ItjrXYh413Y",
    "partners": "pro1"
}

{
    "name": "s1",
    "token": "",
    "partners": "p1"
}
##################### students and partners must/may be lists or arrays
127.0.0.1:8000/api/approve-requests
{
    "name": "p1",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicDIiLCJleHAiOjE2OTI3Nzg5ODN9.FwwaB913RI__dNKZ6fPF7Wd7GHIwggWmWUWwcLqnY9c",
    "students": ["s1"]
}

{
"name": "p1",
"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicDEiLCJleHAiOjE2OTI3ODA0NjB9.B43P2_ORfNGmI1atXs-pZv6IduZB3t96plHmWDT3qo0",
"students": ["s2"]
}

{
"name": "p2",
"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicDIiLCJleHAiOjE2OTI3ODA1NjB9.aLVLpVffyjmrWEu4Vm-2MOpTbaN9tgP3_Ns1UqDSpzI",
"students": ["s2"]
}

http://127.0.0.1:8000/api/check-status/

{
    "name": "s2",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiczIiLCJleHAiOjE2OTI3ODAxNzB9.6OXWlyi4puFxcqS_hdZVtjh4_e9Taskn42FJYfnfrHY"
}




########################################
####################### the blockchain terminal commands #############
For each of the ```let jdbcshsdb = dnvjf .. .``` statements, we immediately get undefined. But if we just type the variable(without any print command) in next line, we get the details of the operation

contract-v2 git:(main) ✗ ganache-cli or ganache cli(the cli needs to be started .. find the command for this)
contracts-v2/contracts git:(main) ✗ npx solc --abi School.sol -o build (don't use npm)
contract-v2 git:(main) ✗ npx truffle compile
contract-v2 git:(main) ✗ npx truffle migrate
contract-v2 git:(main) ✗ truffle console
truffle(development)> let instance = await School.deployed()
truffle(development)> instance
truffle(development)>  let accounts = await web3.eth.getAccounts()
truffle(development)> accounts
truffle(development)> let teachers = [ accounts[6], accounts[7] ]
truffle(development)> teachers
truffle(development)> await instance.requestApproval(teachers, {from:accounts[0]})
truffle(development)> let student1= accounts[0]
truffle(development)> let teacher1= accounts[6]
truffle(development)> await instance.approveRequest(student1, {from: teacher1})
truffle(development)> await instance.approveRequest(student1, {from: accounts[7]})



###################### OUTPUTS  ###########################
contract-v2 git:(main) ✗ npx truffle compile

Compiling your contracts...
===========================
> Everything is up to date, there is nothing to compile.
➜  contract-v2 git:(main) ✗ npx truffle migrate

Compiling your contracts...
===========================
> Everything is up to date, there is nothing to compile.


Starting migrations...
======================
> Network name:    'development'
> Network id:      1692260164118
> Block gas limit: 30000000 (0x1c9c380)


2_deploy_contracts.js
=====================

   Deploying 'School'
   ------------------
   > transaction hash:    0x2c69936be9b4fbfbdc91b8ecfd7cbe26a6bd3299c6d023e6f9d3bf7eada6087f
   > Blocks: 0            Seconds: 0
   > contract address:    0x89E165FC0F1A78366F68bCf917f20E219296D0Df
   > block number:        1
   > block timestamp:     1692260183
   > account:             0xF0EcE28B1FA3f9779a09c3E1b418ECB8565b5962
   > balance:             999.998145407125
   > gas used:            549509 (0x86285)
   > gas price:           3.375 gwei
   > value sent:          0 ETH
   > total cost:          0.001854592875 ETH

   > Saving artifacts
   -------------------------------------
   > Total cost:      0.001854592875 ETH

Summary
=======
> Total deployments:   1
> Final cost:          0.001854592875 ETH


➜  contract-v2 git:(main) ✗ truffle console
truffle(development)>  let accounts = await web3.eth.getAccounts()
undefined
truffle(development)> accounts
[
  '0xF0EcE28B1FA3f9779a09c3E1b418ECB8565b5962',
  '0x20C69C4dC0d6e6A94b64a79eef665A2fA8a4F377',
  '0x8d3B0257a49Cf5f1bb2f22CedEFAabcb7EE2DAa3',
  '0xBEeC6F0b4bcCda940462f00713a4D7305e4Facfc',
  '0x2947d88a0dD184B28F438eAc37bf4cD90D737B25',
  '0x3AdaC7A3AFeaD3e19911e1A57b70E0A27cB986Da',
  '0xBE96d50A7bEDb082035aaFe3c35b710aa1d2bEea',
  '0x1C662d41B2c37A67D9bfd90663595A608CD9686f',
  '0xf1653ec5930E54CaC567705B251986815a333168',
  '0xb6904c74F40ecE5a57bcd3172badcd9402e512F8'
]
truffle(development)> let teachers = [ accounts[6], accounts[7] ]
undefined
truffle(development)> teachers
[
  '0xBE96d50A7bEDb082035aaFe3c35b710aa1d2bEea',
  '0x1C662d41B2c37A67D9bfd90663595A608CD9686f'
]

truffle(development)> await instance.requestApproval(teachers, {from:accounts[0]})
{
  tx: '0x38b81d3544f643b797716aee654b4f53827168a041b6a049694db8703e0d499a',
  receipt: {
    transactionHash: '0x38b81d3544f643b797716aee654b4f53827168a041b6a049694db8703e0d499a',
    transactionIndex: 0,
    blockNumber: 6,
    blockHash: '0x3c1a2a0d680a202743ec9d0ec46777f30c4cc6d9a9586356c287f3f9dd79d0b6',
    from: '0xf0ece28b1fa3f9779a09c3e1b418ecb8565b5962',
    to: '0x97717a1fd7403a0fa71a3aa6aa6f4095f5284301',
    cumulativeGasUsed: 93088,
    gasUsed: 93088,
    contractAddress: null,
    logs: [ [Object] ],
    logsBloom: '0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000008000000000000800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000080000000000000000000000000000000000080000000000000000000000002000000000000000000000000000100000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000020000000000000000000100000000000000000000000000000000000000000000000000',
    status: true,
    effectiveGasPrice: 2954195850,
    type: '0x2',
    rawLogs: [ [Object] ]
  },
  logs: [
    {
      address: '0x97717A1fd7403a0fA71a3aA6aA6f4095F5284301',
      blockHash: '0x3c1a2a0d680a202743ec9d0ec46777f30c4cc6d9a9586356c287f3f9dd79d0b6',
      blockNumber: 6,
      logIndex: 0,
      removed: false,
      transactionHash: '0x38b81d3544f643b797716aee654b4f53827168a041b6a049694db8703e0d499a',
      transactionIndex: 0,
      id: 'log_e79de9f7',
      event: 'RequestApproval',
      args: [Result]
    }
  ]
}


truffle(development)> await instance.approveRequest(student1, {from: teacher1})
{
  tx: '0x18d539bf26dadf4c2c0eac7235a4618e976050c7692dee4953afd70c4db9e86b',
  receipt: {
    transactionHash: '0x18d539bf26dadf4c2c0eac7235a4618e976050c7692dee4953afd70c4db9e86b',
    transactionIndex: 0,
    blockNumber: 7,
    blockHash: '0xb0337fe0e17f82ab697a0ad106ec12b662af8a89f1939c0e8bbb3b97563b4bda',
    from: '0xbe96d50a7bedb082035aafe3c35b710aa1d2beea',
    to: '0x97717a1fd7403a0fa71a3aa6aa6f4095f5284301',
    cumulativeGasUsed: 54682,
    gasUsed: 54682,
    contractAddress: null,
    logs: [],
    logsBloom: '0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    status: true,
    effectiveGasPrice: 2897773704,
    type: '0x2',
    rawLogs: []
  },
  logs: []
}
truffle(development)> await instance.approveRequest(student1, {from: accounts[7]})
{
  tx: '0x188fbeb96dde72c844b9f158989441e5085787da0dd93905bcf882f6702476d3',
  receipt: {
    transactionHash: '0x188fbeb96dde72c844b9f158989441e5085787da0dd93905bcf882f6702476d3',
    transactionIndex: 0,
    blockNumber: 8,
    blockHash: '0xa06aa4b008cd765c9e0bece524871a8036e6afcc406e6a502c09e55f7bae6836',
    from: '0x1c662d41b2c37a67d9bfd90663595a608cd9686f',
    to: '0x97717a1fd7403a0fa71a3aa6aa6f4095f5284301',
    cumulativeGasUsed: 56762,
    gasUsed: 56762,
    contractAddress: null,
    logs: [ [Object] ],
    logsBloom: '0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000008000000000000000000000000800000000000000000000000000020000000000000010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000080000000000000000000000000000000000080000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000020000000000000000000100000000000000000000000000000000000000000000000000',
    status: true,
    effectiveGasPrice: 2848233250,
    type: '0x2',
    rawLogs: [ [Object] ]
  },
  logs: [
    {
      address: '0x97717A1fd7403a0fA71a3aA6aA6f4095F5284301',
      blockHash: '0xa06aa4b008cd765c9e0bece524871a8036e6afcc406e6a502c09e55f7bae6836',
      blockNumber: 8,
      logIndex: 0,
      removed: false,
      transactionHash: '0x188fbeb96dde72c844b9f158989441e5085787da0dd93905bcf882f6702476d3',
      transactionIndex: 0,
      id: 'log_ffd79473',
      event: 'ApprovalReceived',
      args: [Result]
    }
  ]
}



