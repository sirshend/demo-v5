
import mongoengine
from mongoengine import *
# from mongoengine import Document, StringField, ReferenceField, ListField, EmailField, IntField, DictField

class Exam(Document):
    name = StringField(max_length=255)

    def __str__(self):
        return self.name

class Student(Document):
    name = StringField(max_length=255)
    email = EmailField()
    registration_number = StringField(max_length=50)
    role = StringField(max_length=50)
    password = StringField(max_length=255)
    public_key = StringField(max_length=255)
    private_key = StringField(max_length=255)
    partners = ListField(StringField(max_length=255), blank=True)
    applied_exams = ListField(ReferenceField('Exam', reverse_delete_rule=mongoengine.PULL), blank=True)
    permissions_received = ListField(ReferenceField('Exam', reverse_delete_rule=mongoengine.PULL), blank=True)
    #permissions_ppending = ListField(ReferenceField('Exam', reverse_delete_rule=mongoengine.PULL), blank=True)
    permissions_pending = ListField(StringField(max_length=255), blank=True)
    permissions_obtained = ListField(StringField(max_length=255), blank=True)
    #=IntField(min_value=0, max-value=1)
    courses_grades= DictField()
    cpi=DecimalField()
    # cpi=DecimalField(precision=2)
    total_courses=IntField()
    total_grade=IntField()
    courseC_done= BooleanField(default=False)
    courseC_status= IntField()
    courseD_done= BooleanField(default=False)
    courseD_status= IntField()
    thesis1_done= BooleanField(default=False)
    thesis2_done= BooleanField(default=False)
    qualifying_done= BooleanField(default=False)
    sota_done= BooleanField(default=False)
    defence_done= BooleanField(default=False)
    
    partners_thesis2 = ListField(StringField(max_length=255), blank=True)
    permissions_obtained_thesis2 = ListField(StringField(max_length=255), blank=True)

    partners_qual = ListField(StringField(max_length=255), blank=True)
    permissions_obtained_qual = ListField(StringField(max_length=255), blank=True)

    partners_sota = ListField(StringField(max_length=255), blank=True)
    permissions_obtained_sota = ListField(StringField(max_length=255), blank=True)

    partners_defence = ListField(StringField(max_length=255), blank=True)
    permissions_obtained_defence = ListField(StringField(max_length=255), blank=True)
    
    def __str__(self):
        return self.name

class Professor(Document):
    name = StringField(max_length=255)
    email = EmailField()
    registration_number = StringField(max_length=50)
    role = StringField(max_length=50)
    password = StringField(max_length=255)
    private_key = StringField(max_length=255)
    validate_requests = ListField(ReferenceField('Exam', reverse_delete_rule=mongoengine.PULL), blank=True)

    def __str__(self):
        return self.name

class UserRegistration(Document):
    name = StringField(max_length=255)
    email = EmailField()
    registration_number = StringField(max_length=50)
    role = StringField(max_length=50)
    password = StringField(max_length=255)
    public_key = StringField(max_length=255)
    private_key = StringField(max_length=255)

class UserLogin(Document):
    name = StringField(max_length=255)
    token = StringField(max_length=500)
    email = EmailField()
    password = StringField(max_length=255)


###########################################################
###################################################################
# import mongoengine
# from mongoengine import Document, StringField, ReferenceField, ListField, EmailField

# class Exam(Document):
#     name = StringField(max_length=255)

#     def __str__(self):
#         return self.name

# class Student(Document):
#     name = StringField(max_length=255)
#     email = EmailField()
#     registration_number = StringField(max_length=50)
#     role = StringField(max_length=50)
#     password = StringField(max_length=255)
#     public_key = StringField(max_length=255)
#     private_key = StringField(max_length=255)
#     partners = ListField(StringField(max_length=255), blank=True)
#     applied_exams = ListField(ReferenceField('Exam', reverse_delete_rule=mongoengine.PULL), blank=True)
#     permissions_received = ListField(ReferenceField('Exam', reverse_delete_rule=mongoengine.PULL), blank=True)
#     #permissions_ppending = ListField(ReferenceField('Exam', reverse_delete_rule=mongoengine.PULL), blank=True)
#     permissions_pending = ListField(StringField(max_length=255), blank=True)
#     permissions_obtained = ListField(StringField(max_length=255), blank=True)
    
#     def __str__(self):
#         return self.name

# class Professor(Document):
#     name = StringField(max_length=255)
#     email = EmailField()
#     registration_number = StringField(max_length=50)
#     role = StringField(max_length=50)
#     password = StringField(max_length=255)
#     private_key = StringField(max_length=255)
#     validate_requests = ListField(ReferenceField('Exam', reverse_delete_rule=mongoengine.PULL), blank=True)

#     def __str__(self):
#         return self.name

# class UserRegistration(Document):
#     name = StringField(max_length=255)
#     email = EmailField()
#     registration_number = StringField(max_length=50)
#     role = StringField(max_length=50)
#     password = StringField(max_length=255)
#     public_key = StringField(max_length=255)
#     private_key = StringField(max_length=255)

# class UserLogin(Document):
#     name = StringField(max_length=255)
#     token = StringField(max_length=500)
#     email = EmailField()
#     password = StringField(max_length=255)

########################################################
################################################