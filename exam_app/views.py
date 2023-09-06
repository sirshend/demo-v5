import jwt
from django.shortcuts import render
# Create your views here.
from datetime import datetime, timedelta
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer, UserLoginSerializer, ExamSerializer, StudentSerializer, ProfessorSerializer
from .models import UserRegistration, UserLogin, Exam, Student, Professor
from .models import Exam, Student, Professor, UserRegistration, UserLogin
from ecdsa import SigningKey, SECP256k1
#import hashlib

## Integrate the blockchain here. 
from web3 import Web3
from eth_account import Account
ganache_url = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
contract_address = "0x442A3cEC2bfFaDB6B054851c09Eb6a2277ab9bDb"
contract_abi = [{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"student","type":"address"}],"name":"ApprovalReceived","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"student","type":"address"}],"name":"ApprovalReceivedA","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"student","type":"address"}],"name":"ApprovalReceivedAA","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"student","type":"address"}],"name":"ApprovalReceivedB","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"student","type":"address"}],"name":"ApprovalReceivedBB","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"student","type":"address"}],"name":"CourseApprovalReceivedC","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"student","type":"address"}],"name":"CourseApprovalReceivedD","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"student","type":"address"}],"name":"CourseApprovalRejectedC","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"student","type":"address"}],"name":"CourseApprovalRejectedD","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"student","type":"address"},{"indexed":False,"internalType":"string","name":"grade","type":"string"}],"name":"CourseGradeAssignedC","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"student","type":"address"},{"indexed":False,"internalType":"string","name":"grade","type":"string"}],"name":"CourseGradeAssignedD","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"student","type":"address"},{"indexed":False,"internalType":"address","name":"teacher","type":"address"}],"name":"CourseRequestApprovalC","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"student","type":"address"},{"indexed":False,"internalType":"address","name":"teacher","type":"address"}],"name":"CourseRequestApprovalD","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"student","type":"address"},{"indexed":False,"internalType":"string","name":"grade","type":"string"}],"name":"GradeAssigned","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"student","type":"address"},{"indexed":False,"internalType":"string","name":"grade","type":"string"}],"name":"GradeAssignedA","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"student","type":"address"},{"indexed":False,"internalType":"string","name":"grade","type":"string"}],"name":"GradeAssignedAA","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"student","type":"address"},{"indexed":False,"internalType":"string","name":"grade","type":"string"}],"name":"GradeAssignedB","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"student","type":"address"},{"indexed":False,"internalType":"string","name":"grade","type":"string"}],"name":"GradeAssignedBB","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"student","type":"address"},{"indexed":False,"internalType":"address[]","name":"teachers","type":"address[]"}],"name":"RequestApproval","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"student","type":"address"},{"indexed":False,"internalType":"address[]","name":"teachers","type":"address[]"}],"name":"RequestApprovalA","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"student","type":"address"},{"indexed":False,"internalType":"address[]","name":"teachers","type":"address[]"}],"name":"RequestApprovalAA","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"student","type":"address"},{"indexed":False,"internalType":"address[]","name":"teachers","type":"address[]"}],"name":"RequestApprovalB","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"student","type":"address"},{"indexed":False,"internalType":"address[]","name":"teachers","type":"address[]"}],"name":"RequestApprovalBB","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"student","type":"address"},{"indexed":False,"internalType":"address","name":"teacher","type":"address"}],"name":"TeacherAdded","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"student","type":"address"},{"indexed":False,"internalType":"address","name":"teacher","type":"address"}],"name":"TeacherAddedA","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"student","type":"address"},{"indexed":False,"internalType":"address","name":"teacher","type":"address"}],"name":"TeacherAddedAA","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"student","type":"address"},{"indexed":False,"internalType":"address","name":"teacher","type":"address"}],"name":"TeacherAddedB","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"student","type":"address"},{"indexed":False,"internalType":"address","name":"teacher","type":"address"}],"name":"TeacherAddedBB","type":"event"},{"inputs":[{"internalType":"address","name":"student","type":"address"},{"internalType":"address","name":"newTeacher","type":"address"}],"name":"addTeacherToRequest","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"student","type":"address"},{"internalType":"address","name":"newTeacher","type":"address"}],"name":"addTeacherToRequestA","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"student","type":"address"},{"internalType":"address","name":"newTeacher","type":"address"}],"name":"addTeacherToRequestAA","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"student","type":"address"},{"internalType":"address","name":"newTeacher","type":"address"}],"name":"addTeacherToRequestB","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"student","type":"address"},{"internalType":"address","name":"newTeacher","type":"address"}],"name":"addTeacherToRequestBB","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"student","type":"address"}],"name":"approveCourseRequestC","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"student","type":"address"}],"name":"approveCourseRequestD","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"student","type":"address"}],"name":"approveRequest","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"student","type":"address"}],"name":"approveRequestA","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"student","type":"address"}],"name":"approveRequestAA","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"student","type":"address"}],"name":"approveRequestB","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"student","type":"address"}],"name":"approveRequestBB","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"student","type":"address"},{"internalType":"string","name":"grade","type":"string"}],"name":"assignCourseGradeC","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"student","type":"address"},{"internalType":"string","name":"grade","type":"string"}],"name":"assignCourseGradeD","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"student","type":"address"},{"internalType":"string","name":"grade","type":"string"}],"name":"assignGrade","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"student","type":"address"},{"internalType":"string","name":"grade","type":"string"}],"name":"assignGradeA","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"student","type":"address"},{"internalType":"string","name":"grade","type":"string"}],"name":"assignGradeAA","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"student","type":"address"},{"internalType":"string","name":"grade","type":"string"}],"name":"assignGradeB","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"student","type":"address"},{"internalType":"string","name":"grade","type":"string"}],"name":"assignGradeBB","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"student","type":"address"}],"name":"getCourseRequestStatusC","outputs":[{"internalType":"enum School.ApplicationStatusC","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"student","type":"address"}],"name":"getCourseRequestStatusD","outputs":[{"internalType":"enum School.ApplicationStatusD","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"student","type":"address"}],"name":"getStudentGrade","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"student","type":"address"}],"name":"getStudentGradeA","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"student","type":"address"}],"name":"getStudentGradeAA","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"student","type":"address"}],"name":"getStudentGradeB","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"student","type":"address"}],"name":"getStudentGradeBB","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"student","type":"address"}],"name":"getStudentGradeC","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"student","type":"address"}],"name":"getStudentGradeD","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"student","type":"address"}],"name":"rejectCourseRequestC","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"student","type":"address"}],"name":"rejectCourseRequestD","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"teachers","type":"address[]"}],"name":"requestApproval","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"teachers","type":"address[]"}],"name":"requestApprovalA","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"teachers","type":"address[]"}],"name":"requestApprovalAA","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"teachers","type":"address[]"}],"name":"requestApprovalB","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"teachers","type":"address[]"}],"name":"requestApprovalBB","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"teacher","type":"address"}],"name":"requestCourseApprovalC","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"teacher","type":"address"}],"name":"requestCourseApprovalD","outputs":[],"stateMutability":"nonpayable","type":"function"}]
contract = web3.eth.contract(address=contract_address, abi=contract_abi)
##
i = 0

#################################################################################################################
###################### Login, Register, KYC stuff ###############################################################
#################################################################################################################

@api_view(['POST'])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        password = serializer.validated_data['password']
        role = serializer.validated_data['role']
        email= serializer.validated_data['email']
        # Check if user already exists
        if UserRegistration.objects(name=name).first():
            return Response({'message': 'User already exists'})
        global i
        priv_account = web3.eth.accounts[i]
        user_registration = UserRegistration(name=name, password=password, role=role, private_key=priv_account)
        i=i+1
        user_registration.save()
        if role == 'student':
            Sttudent = Student(name=name, role= role, email=email, courseC_status= 0, courseD_status=0, cpi=0, total_grade=0, total_courses=0, courseC_done= False, courseD_done=False, thesis1_done=False, thesis2_done=False, qualifying_done=False,sota_done=False,defence_done=False)
            Sttudent.save()
        else:
            Prrofessor = Professor(name=name, role=role, email=email)
            Prrofessor.save()
        # Return the response with the keys
        return Response({'message': 'User registered successfully'})
    else:
        # Return validation error response
        return Response(serializer.errors, status=400)



@api_view(['POST'])
def login_user(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        password = serializer.validated_data['password']
        # Check if user exists and password is correct
        user = UserRegistration.objects(name=name).first()
        if not user:
            return Response({'message': 'User not registered'})
        if user.password != password:
            return Response({'message': 'Password incorrect'})
        token = jwt.encode({
            'name': name,
            'exp': datetime.utcnow() + settings.JWT_EXPIRATION_DELTA
        }, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
        # Update the user's token in the database
        user_login = UserLogin.objects(name=name).first()
        if not user_login:
            user_login = UserLogin(name=name)
        user_login.token = token
        user_login.save()
        # Return the response with the token
        return Response({
            'message': 'User login successfully',
            'token': token
        })
    else:
        # Return validation error response
        return Response(serializer.errors, status=400)

##################################################################################################################################
################## API for List of tasks/actions to be done by student ############################################################
################# Also API for generating transcript #############################################################################
################################################################################################################################## 
@api_view(['POST'])
def student_checklist_todo(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        token = serializer.validated_data['token']
        # Check if user exists and token is valid
        user_login = UserLogin.objects(name=name).first()
        if not user_login:
            return Response({'message': 'User not registered'})
        try:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            if decoded_token['name'] != name:
                raise jwt.DecodeError
            if datetime.fromtimestamp(decoded_token['exp']) < datetime.utcnow():
                raise jwt.ExpiredSignatureError
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Session has ended. Do a fresh login'})
        except jwt.DecodeError:
            return Response({'message': 'Invalid token'})
        # Check if the user has the role 'student'
        user = Student.objects(name=name).first()
        if not user:
            return Response({'message': 'Only students can check status for defence'})
        # Check if 'partners' field is blank
        # Check if all partners are present in 'permissions_obtained' field
        checklistt=[]
        if user.courseC_done == False:
            checklistt.append("Need to finish course C")
        if user.courseD_done == False:
            checklistt.append("Need to finish course D")
        if user.qualifying_done == False:
            checklistt.append("Need to finish qualifying exam")
        if user.thesis1_done == False:
            checklistt.append("Need to finish thesis 1 credits")
        if user.thesis2_done == False:
            checklistt.append("Need to finish thesis 2 credits")
        if user.sota_done == False:
            checklistt.append("Need to appear for SOTA")
        if user.defence_done == False:
            checklistt.append("Need to appear for thesis Defence")
        else: 
            checklistt = "Congrats!!You have finished PhD, and ready for convocation"
        return Response({'You have to': checklistt})
        
        



@api_view(['POST'])
def generate_transcript_till_now(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        token = serializer.validated_data['token']
        # Check if user exists and token is valid
        user_login = UserLogin.objects(name=name).first()
        if not user_login:
            return Response({'message': 'User not registered'})
        try:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            if decoded_token['name'] != name:
                raise jwt.DecodeError
            if datetime.fromtimestamp(decoded_token['exp']) < datetime.utcnow():
                raise jwt.ExpiredSignatureError
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Session has ended. Do a fresh login'})
        except jwt.DecodeError:
            return Response({'message': 'Invalid token'})
        # Check if the user has the role 'student'
        user = Student.objects(name=name).first()
        if not user:
            return Response({'message': 'Only students can check status for defence'})
        # Check if 'partners' field is blank
        # Check if all partners are present in 'permissions_obtained' field
        checklistt=[]
        checklistt.append({"CPI": user.cpi})
        checklistt.append({"number of courses done": user.total_courses})
        if user.courseC_done == False:
            checklistt.append("course C: not done")
        else:
            checklistt.append({"cource C": user.courses_grades["course C"]})
        if user.courseD_done == False:
            checklistt.append("course D: not done")
        else:
            checklistt.append({"cource D": user.courses_grades["course D"]})
        if user.qualifying_done == False:
            checklistt.append("Quals: not done")
        else:
            checklistt.append({"Quals": user.courses_grades["quals"]})
        if user.thesis1_done == False:
            checklistt.append("thesis1: not done")
        else:
            checklistt.append({"thesis1": user.courses_grades["thesis1"]})
        if user.thesis2_done == False:
            checklistt.append("thesis2: not done")
        else:
            checklistt.append({"thesis2": user.courses_grades["thesis2"]})
        if user.sota_done == False:
            checklistt.append("SOTA: not done")
        else:
            checklistt.append({"SOTA": user.courses_grades["sota"]})
        if user.defence_done == False:
            checklistt.append("Defence: not done")
        else:
            checklistt.append({"Defence": user.courses_grades["defence"]})
        return Response({'Transcript': checklistt})
        


###############################################################################################################################################
######################################## Course C (pre-req for Course D) ######################################################################
###############################################################################################################################################

@api_view(['POST'])
def apply_for_courseC(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        token = serializer.validated_data['token']
        # Check if user exists and token is valid
        user_login = UserLogin.objects(name=name).first()
        if not user_login:
            return Response({'message': 'User not registered'})
        try:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            if decoded_token['name'] != name:
                raise jwt.DecodeError
            if datetime.fromtimestamp(decoded_token['exp']) < datetime.utcnow():
                raise jwt.ExpiredSignatureError
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Session has ended. Do a fresh login'})
        except jwt.DecodeError:
            return Response({'message': 'Invalid token'})
        # Check if the user has the role 'student'
        user_register = UserRegistration.objects(name=name).first()
        if user_register.role == "student":
            user = Student.objects(name=name).first()
        else:
            return Response({'message': 'Only students can apply for the courseC'})
        sender_account = user_register.private_key
        user = Student.objects(name=name).first()
        if not user:
            return Response({'message': 'Only students can apply for the courseC'})
        if user.courseC_status != 0:
            return Response({'message': 'Cant apply for Course C. Either already applied before, application pending, already approved, or rejected'})
        # Get the professor's names from the request data
        professors = request.data.get('course-prof', [])
        if not isinstance(professors, list):
            return Response({'message': 'Invalid professors data format'})
        # Check if the professor's name exists in the database
        existing_professors = Professor.objects(name__in=professors)
        if len(existing_professors) != len(professors):
            return Response({'message': 'Professor does not exist in the database'})
        # Add the student's name to the professors' 'permissions_pending' field
        for professor in existing_professors:
            prof_register = UserRegistration.objects(name=professor.name).first()
            acc1=prof_register.private_key
        transaction = contract.functions.requestCourseApprovalC(acc1).transact({
            'from': sender_account})
        # Wait for the transaction to be mined
        transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction)
        if transaction_receipt['status'] == 1:
            user.courseC_status = 1
            user.save()
            return Response({'message': 'Application for courseC submitted successfully. The chain is fine!!',
            'courseC status': user.courseC_status})
        else:
            user.save()
            return Response({'message': 'Trouble in the chain!!'})
    else:
        # Return validation error response
        return Response(serializer.errors, status=400)



@api_view(['POST'])
def approve_courseC(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        token = serializer.validated_data['token']
        # Check if user exists and token is valid
        user_login = UserLogin.objects(name=name).first()
        if not user_login:
            return Response({'message': 'User not registered'})
        try:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            if decoded_token['name'] != name:
                raise jwt.DecodeError
            if datetime.fromtimestamp(decoded_token['exp']) < datetime.utcnow():
                raise jwt.ExpiredSignatureError
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Session has ended. Do a fresh login'})
        except jwt.DecodeError:
            return Response({'message': 'Invalid token'})
        # Check if the user has the role 'professor'
        user = Professor.objects(name=name).first()
        if not user:
            return Response({'message': 'Only the profe can approve requests for Course C'})
        # Check if the user has the role 'professor'
        user_register = UserRegistration.objects(name=name).first()
        if user_register.role == "professor":
            user = Professor.objects(name=name).first()
        else:
            return Response({'message': 'Only professors are allowed'})
        # Get the list of student names from the request data
        sender_account = user_register.private_key
        students = request.data.get('student', [])
        if not isinstance(students, list):
            return Response({'message': 'Invalid students data format'})
        # Check if the student names exist in the database
        existing_students = Student.objects(name__in=students)
        if len(existing_students) != len(students):
            return Response({'message': 'Some students do not exist in the database'})
        # Process each student and update their 'permissions_obtained' field
        for student in existing_students:
            if student.courseC_status != 1:
                return Response({'message': 'Cant approve request for Course C. Such an application isnt pending, or, hasnt come from the student yet'})
            tea1= user_register.private_key
            stu1= UserRegistration.objects(name=student.name).first()
            stu2= stu1.private_key
            transaction = contract.functions.approveCourseRequestC(stu2).transact({'from': tea1})
            transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction)
            if transaction_receipt['status'] == 1:
                student.courseC_status = 2
                student.save()
                return Response({'message': 'Application for Course C has been approved!!', 'by': user_register.name, 'courseC_status': student.courseC_status })
            else:
                student.save()
                return Response({'message': ' Trouble in the chain!!'})
        # Return the response
        return Response({'message': 'Some error with processing. Check input types'})
    else:
        # Return validation error response
        return Response(serializer.errors, status=400)




@api_view(['POST'])
def reject_courseC(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        token = serializer.validated_data['token']
        # Check if user exists and token is valid
        user_login = UserLogin.objects(name=name).first()
        if not user_login:
            return Response({'message': 'User not registered'})
        try:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            if decoded_token['name'] != name:
                raise jwt.DecodeError
            if datetime.fromtimestamp(decoded_token['exp']) < datetime.utcnow():
                raise jwt.ExpiredSignatureError
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Session has ended. Do a fresh login'})
        except jwt.DecodeError:
            return Response({'message': 'Invalid token'})
        # Check if the user has the role 'professor'
        user = Professor.objects(name=name).first()
        if not user:
            return Response({'message': 'Only the profe can reject requests for Course C'})
        # Check if the user has the role 'professor'
        user_register = UserRegistration.objects(name=name).first()
        if user_register.role == "professor":
            user = Professor.objects(name=name).first()
        else:
            return Response({'message': 'Only professors are allowed'})
        # Get the list of student names from the request data
        sender_account = user_register.private_key
        students = request.data.get('student', [])
        if not isinstance(students, list):
            return Response({'message': 'Invalid students data format'})
        # Check if the student names exist in the database
        existing_students = Student.objects(name__in=students)
        if len(existing_students) != len(students):
            return Response({'message': 'Some students do not exist in the database'})
        # Process each student and update their 'permissions_obtained' field
        for student in existing_students:
            if student.courseC_status != 1:
                return Response({'message': 'Cant reject request for Course C. Such an application isnt pending, or, hasnt come from the student yet'})
            tea1= user_register.private_key
            stu1= UserRegistration.objects(name=student.name).first()
            stu2= stu1.private_key
            transaction = contract.functions.rejectCourseRequestC(stu2).transact({'from': tea1})
            transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction)
            if transaction_receipt['status'] == 1:
                student.courseC_status = 3
                student.save()
                return Response({'message': 'Application for Course C has been rejected!!', 'by': user_register.name, 'courseC status': student.courseC_status})
            else:
                student.save()
                return Response({'message': ' Trouble in the chain!!'})
        # Return the response
        return Response({'message': 'Some error with processing. Check input types'})
    else:
        # Return validation error response
        return Response(serializer.errors, status=400)



@api_view(['POST'])
def assign_grade_courseC(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        token = serializer.validated_data['token']
        # Check if user exists and token is valid
        user_login = UserLogin.objects(name=name).first()
        if not user_login:
            return Response({'message': 'User not registered'})
        try:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            if decoded_token['name'] != name:
                raise jwt.DecodeError
            if datetime.fromtimestamp(decoded_token['exp']) < datetime.utcnow():
                raise jwt.ExpiredSignatureError
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Session has ended. Do a fresh login'})
        except jwt.DecodeError:
            return Response({'message': 'Invalid token'})
        # Check if the user has the role 'professor'
        user = Professor.objects(name=name).first()
        if not user:
            return Response({'message': 'Only professors can approve requests for exams'})
        # Check if the user has the role 'professor'
        user_register = UserRegistration.objects(name=name).first()
        if user_register.role == "professor":
            user = Professor.objects(name=name).first()
        else:
            return Response({'message': 'Only professors are allowed'})
        # Get the list of student names from the request data
        students = request.data.get('student', [])
        grade = request.data.get('grade')
        if not isinstance(students, list):
            return Response({'message': 'Invalid students data format'})
        # Check if the student names exist in the database
        existing_students = Student.objects(name__in=students)
        if len(existing_students) != len(students):
            return Response({'message': 'Some students do not exist in the database'})
        # Process each student and update their 'permissions_obtained' field
        for student in existing_students:
            if student.courseC_status != 2:
                return Response({'message': 'Cant submit grades for Course C. The application for the course by the student has not been approved.'})
            if grade == "A":
                student.courseC_done = True
                student.total_grade = student.total_grade + 10*10
                student.total_courses = student.total_courses + 1
                student.cpi = student.total_grade / (student.total_courses*10)
                student.courses_grades["course C"] = "A"
                student.save()
            elif grade == "B":
                student.courseC_done = True
                student.total_grade = student.total_grade + 10*8
                student.total_courses = student.total_courses + 1
                student.cpi = student.total_grade / (student.total_courses*10)
                student.courses_grades["course C"] = "B"
                student.save()
            elif grade == "C":
                student.courseC_done = True
                student.total_grade = student.total_grade + 10*6
                student.total_courses = student.total_courses + 1
                student.cpi = student.total_grade / (student.total_courses*10)
                student.courses_grades["course C"] = "C"
                student.save()
            elif grade == "D":
                student.courseC_done = True
                student.total_grade = student.total_grade + 10*4
                student.total_courses = student.total_courses + 1
                student.cpi = student.total_grade / (student.total_courses*10)
                student.courses_grades["course C"] = "D"
                student.save()
            elif grade == "F":
                student.courseC_done = False
                student.total_grade = student.total_grade + 10*0
                student.total_courses = student.total_courses + 1
                student.cpi = student.total_grade / (student.total_courses*10)
                student.courses_grades["course C"] = "F"
                student.save()
            else:
                return Response({'Submitted grade must be A, B, C, D or F. Any other grades are invalid.'})
            tea1= user_register.private_key
            stu1= UserRegistration.objects(name=student.name).first()
            stu2= stu1.private_key
            transaction = contract.functions.assignCourseGradeC(stu2, grade).transact({'from': tea1})
            transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction)
            if transaction_receipt['status'] == 1:
                return Response({'message': 'Grade submitted!!', 'by': user_register.name, 'student': student.name, 'grade for courseC': grade, "Pass/fail": student.courseC_done, "CPI": student.cpi, "Total courses": student.total_courses  })
            else:
                return Response({'message': 'Grade not submitted. Trouble in the chain!!'})
        # Return the response
        return Response({'message': 'Some error with processing. Check input types'})
    else:
        # Return validation error response
        return Response(serializer.errors, status=400)

## two helper apis, one directly shows students grades, the other shows student's application status for the course
## both call external functions on the blockchain, so can be called by anyone from the backend using web3.py 


@api_view(['POST'])
def get_student_grade_courseC(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        # Check if the user has the role 'student'
        user_register = UserRegistration.objects(name=name).first()
        if not user_register:
            return Response({'message': 'this student has not registered. So cant have a grade for this course'})
        if user_register.role == "student":
            user = Student.objects(name=name).first()
        else:
            return Response({'message': 'Only students can get a grade for a course'})
        user = Student.objects(name=name).first()
        if not user:
            return Response({'message': 'Only students can apply for the Course C'})
        student_address = user_register.private_key
        grade = contract.functions.getStudentGradeC(student_address).call()
        return Response("The student has the following grade: " + grade)

@api_view(['POST'])
def get_student_application_courseC(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        # Check if the user has the role 'student'
        user_register = UserRegistration.objects(name=name).first()
        if not user_register:
            return Response({'message': 'this student has not registered. So cant have an application status for this course'})
        if user_register.role == "student":
            user = Student.objects(name=name).first()
        else:
            return Response({'message': 'Only students can get an approval for a course'})
        user = Student.objects(name=name).first()
        if not user:
            return Response({'message': 'Only students can apply for the Course C'})
        student_address = user_register.private_key
        course_statuss = contract.functions.getCourseRequestStatusC(student_address).call()
        return Response({"Application status of student":  course_statuss})

###############################################################################################################################################
######################################## Course D ( the total credits of C and D determine if allowed to sit for qualifying exams) ############
###############################################################################################################################################

@api_view(['POST'])
def apply_for_courseD(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        token = serializer.validated_data['token']
        # Check if user exists and token is valid
        user_login = UserLogin.objects(name=name).first()
        if not user_login:
            return Response({'message': 'User not registered'})
        try:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            if decoded_token['name'] != name:
                raise jwt.DecodeError
            if datetime.fromtimestamp(decoded_token['exp']) < datetime.utcnow():
                raise jwt.ExpiredSignatureError
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Session has ended. Do a fresh login'})
        except jwt.DecodeError:
            return Response({'message': 'Invalid token'})
        # Check if the user has the role 'student'
        user_register = UserRegistration.objects(name=name).first()
        if user_register.role == "student":
            user = Student.objects(name=name).first()
        else:
            return Response({'message': 'Only students can apply for the courseD'})
        sender_account = user_register.private_key
        user = Student.objects(name=name).first()
        if not user:
            return Response({'message': 'Only students can apply for the courseD'})
        if not user.courseC_done:
            return Response({'message': 'Application for Course D failed. Can not apply for Course D without doing Course C first. C is pre-req'})
        if user.courseD_status != 0:
            return Response({'message': 'Cant apply for Course D. Either already applied before, application pending, already approved, or rejected'})
        # Get the professor's names from the request data
        professors = request.data.get('course-prof', [])
        if not isinstance(professors, list):
            return Response({'message': 'Invalid professors data format'})
        # Check if the professor's name exists in the database
        existing_professors = Professor.objects(name__in=professors)
        if len(existing_professors) != len(professors):
            return Response({'message': 'Professor does not exist in the database'})
        # Add the student's name to the professors' 'permissions_pending' field
        for professor in existing_professors:
            prof_register = UserRegistration.objects(name=professor.name).first()
            acc1=prof_register.private_key
        transaction = contract.functions.requestCourseApprovalD(acc1).transact({
            'from': sender_account})
        # Wait for the transaction to be mined
        transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction)
        if transaction_receipt['status'] == 1:
            user.courseD_status = 1
            user.save()
            return Response({'message': 'Application for courseD submitted successfully. The chain is fine!!',
            'courseD status': user.courseD_status})
        else:
            user.save()
            return Response({'message': 'Trouble in the chain!!'})
    else:
        # Return validation error response
        return Response(serializer.errors, status=400)



@api_view(['POST'])
def approve_courseD(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        token = serializer.validated_data['token']
        # Check if user exists and token is valid
        user_login = UserLogin.objects(name=name).first()
        if not user_login:
            return Response({'message': 'User not registered'})
        try:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            if decoded_token['name'] != name:
                raise jwt.DecodeError
            if datetime.fromtimestamp(decoded_token['exp']) < datetime.utcnow():
                raise jwt.ExpiredSignatureError
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Session has ended. Do a fresh login'})
        except jwt.DecodeError:
            return Response({'message': 'Invalid token'})
        # Check if the user has the role 'professor'
        user = Professor.objects(name=name).first()
        if not user:
            return Response({'message': 'Only the profe can approve requests for Course D'})
        # Check if the user has the role 'professor'
        user_register = UserRegistration.objects(name=name).first()
        if user_register.role == "professor":
            user = Professor.objects(name=name).first()
        else:
            return Response({'message': 'Only professors are allowed'})
        # Get the list of student names from the request data
        sender_account = user_register.private_key
        students = request.data.get('student', [])
        if not isinstance(students, list):
            return Response({'message': 'Invalid students data format'})
        # Check if the student names exist in the database
        existing_students = Student.objects(name__in=students)
        if len(existing_students) != len(students):
            return Response({'message': 'Some students do not exist in the database'})
        # Process each student and update their 'permissions_obtained' field
        for student in existing_students:
            if not student.courseC_done:
                return Response({'message': 'Application for Course D failed. Can not apply for Course D without doing Course C first. C is pre-req'})
            if student.courseD_status != 1:
                return Response({'message': 'Cant approve request for Course D. Such an application isnt pending, or, hasnt come from the student yet'})
            tea1= user_register.private_key
            stu1= UserRegistration.objects(name=student.name).first()
            stu2= stu1.private_key
            transaction = contract.functions.approveCourseRequestD(stu2).transact({'from': tea1})
            transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction)
            if transaction_receipt['status'] == 1:
                student.courseD_status = 2
                student.save()
                return Response({'message': 'Application for Course D has been approved!!', 'by': user_register.name, 'courseD_status': student.courseD_status })
            else:
                student.save()
                return Response({'message': ' Trouble in the chain!!'})
        # Return the response
        return Response({'message': 'Some error with processing. Check input types'})
    else:
        # Return validation error response
        return Response(serializer.errors, status=400)




@api_view(['POST'])
def reject_courseD(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        token = serializer.validated_data['token']
        # Check if user exists and token is valid
        user_login = UserLogin.objects(name=name).first()
        if not user_login:
            return Response({'message': 'User not registered'})
        try:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            if decoded_token['name'] != name:
                raise jwt.DecodeError
            if datetime.fromtimestamp(decoded_token['exp']) < datetime.utcnow():
                raise jwt.ExpiredSignatureError
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Session has ended. Do a fresh login'})
        except jwt.DecodeError:
            return Response({'message': 'Invalid token'})
        # Check if the user has the role 'professor'
        user = Professor.objects(name=name).first()
        if not user:
            return Response({'message': 'Only the profe can reject requests for Course D'})
        # Check if the user has the role 'professor'
        user_register = UserRegistration.objects(name=name).first()
        if user_register.role == "professor":
            user = Professor.objects(name=name).first()
        else:
            return Response({'message': 'Only professors are allowed'})
        # Get the list of student names from the request data
        sender_account = user_register.private_key
        students = request.data.get('student', [])
        if not isinstance(students, list):
            return Response({'message': 'Invalid students data format'})
        # Check if the student names exist in the database
        existing_students = Student.objects(name__in=students)
        if len(existing_students) != len(students):
            return Response({'message': 'Some students do not exist in the database'})
        # Process each student and update their 'permissions_obtained' field
        for student in existing_students:
            if not student.courseC_done:
                return Response({'message': 'Application for Course D failed. Can not apply for Course D without doing Course C first. C is pre-req'})
            if student.courseD_status != 1:
                return Response({'message': 'Cant reject request for Course D. Such an application isnt pending, or, hasnt come from the student yet'})
            tea1= user_register.private_key
            stu1= UserRegistration.objects(name=student.name).first()
            stu2= stu1.private_key
            transaction = contract.functions.rejectCourseRequestD(stu2).transact({'from': tea1})
            transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction)
            if transaction_receipt['status'] == 1:
                student.courseD_status = 3
                student.save()
                return Response({'message': 'Application for Course D has been rejected!!', 'by': user_register.name, 'courseD status': student.courseD_status})
            else:
                student.save()
                return Response({'message': ' Trouble in the chain!!'})
        # Return the response
        return Response({'message': 'Some error with processing. Check input types'})
    else:
        # Return validation error response
        return Response(serializer.errors, status=400)



@api_view(['POST'])
def assign_grade_courseD(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        token = serializer.validated_data['token']
        # Check if user exists and token is valid
        user_login = UserLogin.objects(name=name).first()
        if not user_login:
            return Response({'message': 'User not registered'})
        try:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            if decoded_token['name'] != name:
                raise jwt.DecodeError
            if datetime.fromtimestamp(decoded_token['exp']) < datetime.utcnow():
                raise jwt.ExpiredSignatureError
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Session has ended. Do a fresh login'})
        except jwt.DecodeError:
            return Response({'message': 'Invalid token'})
        # Check if the user has the role 'professor'
        user = Professor.objects(name=name).first()
        if not user:
            return Response({'message': 'Only professors can approve requests for exams'})
        # Check if the user has the role 'professor'
        user_register = UserRegistration.objects(name=name).first()
        if user_register.role == "professor":
            user = Professor.objects(name=name).first()
        else:
            return Response({'message': 'Only professors are allowed'})
        # Get the list of student names from the request data
        students = request.data.get('student', [])
        grade = request.data.get('grade')
        if not isinstance(students, list):
            return Response({'message': 'Invalid students data format'})
        # Check if the student names exist in the database
        existing_students = Student.objects(name__in=students)
        if len(existing_students) != len(students):
            return Response({'message': 'Some students do not exist in the database'})
        # Process each student and update their 'permissions_obtained' field
        for student in existing_students:
            if not student.courseC_done:
                return Response({'message': 'Can not deal with Course D without doing Course C first. C is pre-req'})
            if student.courseD_status != 2:
                return Response({'message': 'Cant submit grades for Course D. The application for the course by the student has not been approved.'})
            if grade == "A":
                student.courseD_done = True
                student.total_grade = student.total_grade + 10*10
                student.total_courses = student.total_courses + 1
                student.cpi = student.total_grade / (student.total_courses*10)
                student.courses_grades["course D"] = "A"
                student.save()
            elif grade == "B":
                student.courseD_done = True
                student.total_grade = student.total_grade + 10*8
                student.total_courses = student.total_courses + 1
                student.cpi = student.total_grade / (student.total_courses*10)
                student.courses_grades["course D"] = "B"
                student.save()
            elif grade == "C":
                student.courseD_done = True
                student.total_grade = student.total_grade + 10*6
                student.total_courses = student.total_courses + 1
                student.cpi = student.total_grade / (student.total_courses*10)
                student.courses_grades["course D"] = "C"
                student.save()
            elif grade == "D":
                student.courseD_done = True
                student.total_grade = student.total_grade + 10*4
                student.total_courses = student.total_courses + 1
                student.cpi = student.total_grade / (student.total_courses*10)
                student.courses_grades["course D"] = "D"
                student.save()
            elif grade == "F":
                student.courseD_done = False
                student.total_grade = student.total_grade + 10*0
                student.total_courses = student.total_courses + 1
                student.cpi = student.total_grade / (student.total_courses*10)
                student.courses_grades["course D"] = "F"
                student.save()
            else:
                return Response({'Submitted grade must be A, B, C, D or F. Any other grades are invalid.'})
            tea1= user_register.private_key
            stu1= UserRegistration.objects(name=student.name).first()
            stu2= stu1.private_key
            transaction = contract.functions.assignCourseGradeD(stu2, grade).transact({'from': tea1})
            transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction)
            if transaction_receipt['status'] == 1:
                return Response({'message': 'Grade submitted!!', 'by': user_register.name, 'student': student.name, 'grade for courseD': grade, "Pass/fail": student.courseD_done, "CPI": student.cpi, "Total courses": student.total_courses  })
            else:
                return Response({'message': 'Grade not submitted. Trouble in the chain!!'})
        # Return the response
        return Response({'message': 'Some error with processing. Check input types'})
    else:
        # Return validation error response
        return Response(serializer.errors, status=400)

## two helper apis, one directly shows students grades, the other shows student's application status for the course
## both call external functions on the blockchain, so can be called by anyone from the backend using web3.py 


@api_view(['POST'])
def get_student_grade_courseD(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        # Check if the user has the role 'student'
        user_register = UserRegistration.objects(name=name).first()
        if not user_register:
            return Response({'message': 'this student has not registered. So cant have a grade for this course'})
        if user_register.role == "student":
            user = Student.objects(name=name).first()
        else:
            return Response({'message': 'Only students can get a grade for a course'})
        user = Student.objects(name=name).first()
        if not user:
            return Response({'message': 'Only students can apply for the Course D'})
        student_address = user_register.private_key
        grade = contract.functions.getStudentGradeD(student_address).call()
        return Response("The student has the following grade: " + grade)

@api_view(['POST'])
def get_student_application_courseD(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        # Check if the user has the role 'student'
        user_register = UserRegistration.objects(name=name).first()
        if not user_register:
            return Response({'message': 'this student has not registered. So cant have an application status for this course'})
        if user_register.role == "student":
            user = Student.objects(name=name).first()
        else:
            return Response({'message': 'Only students can get an approval for a course'})
        user = Student.objects(name=name).first()
        if not user:
            return Response({'message': 'Only students can apply for the Course D'})
        student_address = user_register.private_key
        course_statuss = contract.functions.getCourseRequestStatusD(student_address).call()
        return Response({"Application status of student":  course_statuss})


###############################################################################################################################################
############################################# Qualifying exams (allowed to sit for qual. exam, only if you complete atleast 2 courses #########
################################################################################################################################################

@api_view(['POST'])
def apply_for_qual(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        token = serializer.validated_data['token']
        # Check if user exists and token is valid
        user_login = UserLogin.objects(name=name).first()
        if not user_login:
            return Response({'message': 'User not registered'})
        try:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            if decoded_token['name'] != name:
                raise jwt.DecodeError
            if datetime.fromtimestamp(decoded_token['exp']) < datetime.utcnow():
                raise jwt.ExpiredSignatureError
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Session has ended. Do a fresh login'})
        except jwt.DecodeError:
            return Response({'message': 'Invalid token'})    
        # Check if the user has the role 'student'
        user_register = UserRegistration.objects(name=name).first()
        if user_register.role == "student":
            user = Student.objects(name=name).first()
        else:
            return Response({'message': 'Only students can apply for the Qualifying exam'})
        sender_account = user_register.private_key
        user = Student.objects(name=name).first()
        if not user:
            return Response({'message': 'Only students can apply for the Qualifying exam'})
        if user.total_courses < 2:
            return Response({'message': 'Need to complete atleast 2 courses before taking Qualifying Exams'})
        # Get the list of professors' names from the request data
        professors = request.data.get('prof', [])
        if not isinstance(professors, list):
            return Response({'message': 'Invalid professors data format'})
        # Check if the professors' names exist in the database
        existing_professors = Professor.objects(name__in=professors)
        if len(existing_professors) != len(professors):
            return Response({'message': 'Some professors do not exist in the database'})
        # Add professors to the student's 'partners' field
        user.partners_qual = professors
        user.save()
        teachers=[]
        # Add the student's name to the professors' 'permissions_pending' field
        for professor in existing_professors:
            prof_register = UserRegistration.objects(name=professor.name).first()
            acc1=prof_register.private_key
            teachers.append(acc1)
            prof_register.save()
            professor.save()
        transaction = contract.functions.requestApprovalA(teachers).transact({
            'from': sender_account})
        # Wait for the transaction to be mined
        transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction)
        if transaction_receipt['status'] == 1:
            return Response({'message': 'Application for Qualifying Exam submitted successfully. The chain is fine!!'})
        else:
            return Response({'message': 'Trouble in the chain!!'})
    else:
        # Return validation error response
        return Response(serializer.errors, status=400)



@api_view(['POST'])
def approve_qual(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        token = serializer.validated_data['token']
        # Check if user exists and token is valid
        user_login = UserLogin.objects(name=name).first()
        if not user_login:
            return Response({'message': 'User not registered'})
        try:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            if decoded_token['name'] != name:
                raise jwt.DecodeError
            if datetime.fromtimestamp(decoded_token['exp']) < datetime.utcnow():
                raise jwt.ExpiredSignatureError
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Session has ended. Do a fresh login'})
        except jwt.DecodeError:
            return Response({'message': 'Invalid token'})
        # Check if the user has the role 'professor'
        user = Professor.objects(name=name).first()
        if not user:
            return Response({'message': 'Only professors can approve requests for qualifying exam'})
        # Check if the user has the role 'professor'
        user_register = UserRegistration.objects(name=name).first()
        if user_register.role == "professor":
            user = Professor.objects(name=name).first()
        else:
            return Response({'message': 'Only professors are allowed to approve qualifying exam requests'})
        # Get the list of student names from the request data
        students = request.data.get('student', [])
        if not isinstance(students, list):
            return Response({'message': 'Invalid students data format'})
        # Check if the student names exist in the database
        existing_students = Student.objects(name__in=students)
        if len(existing_students) != len(students):
            return Response({'message': 'Some students do not exist in the database'})
        # Process each student and update their 'permissions_obtained' field
        for student in existing_students:
            if name in student.partners_qual:
                if student.total_courses < 2:
                    return Response({'message': 'Need to complete atleast 2 courses before taking Qualifying Exams'})
                tea1= user_register.private_key
                stu1= UserRegistration.objects(name=student.name).first()
                stu2= stu1.private_key
                transaction = contract.functions.approveRequestA(stu2).transact({'from': tea1})
                transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction)
                if transaction_receipt['status'] == 1:
                    student.permissions_obtained_qual.append(name)
                    student.save()
                    return Response({'message': 'Application for Quals has been approved!!', 'by': user_register.name})
                else:
                    return Response({'message': ' Trouble in the chain!!'})
        # Return the response
        return Response({'message': 'Some error with processing. Check input types'})
    else:
        # Return validation error response
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def assign_grade_qual(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        token = serializer.validated_data['token']
        # Check if user exists and token is valid
        user_login = UserLogin.objects(name=name).first()
        if not user_login:
            return Response({'message': 'User not registered'})
        try:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            if decoded_token['name'] != name:
                raise jwt.DecodeError
            if datetime.fromtimestamp(decoded_token['exp']) < datetime.utcnow():
                raise jwt.ExpiredSignatureError
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Session has ended. Do a fresh login'})
        except jwt.DecodeError:
            return Response({'message': 'Invalid token'})
        # Check if the user has the role 'professor'
        user = Professor.objects(name=name).first()
        if not user:
            return Response({'message': 'Only professors can assign grades for Qualifying exam'})
        # Check if the user has the role 'professor'
        user_register = UserRegistration.objects(name=name).first()
        if user_register.role == "professor":
            user = Professor.objects(name=name).first()
        else:
            return Response({'message': 'Only professors are allowed'})
        # Get the list of student names from the request data
        students = request.data.get('student', [])
        grade = request.data.get('grade')
        if not isinstance(students, list):
            return Response({'message': 'Invalid students data format'})
        # Check if the student names exist in the database
        existing_students = Student.objects(name__in=students)
        if len(existing_students) != len(students):
            return Response({'message': 'Some students do not exist in the database'})
        # Process each student and update their 'permissions_obtained' field
        for student in existing_students:
            if name in student.partners_qual:
                if student.total_courses < 2:
                    return Response({'message': 'Need to complete atleast 2 courses before taking Qualifying Exams'})
                if grade == "S":
                    student.courses_grades["quals"]=grade
                    student.qualifying_done = True
                    student.save()
                elif grade == "X":
                    student.courses_grades["quals"]=grade
                    student.qualifying_done = False
                    student.save()
                else:
                    student.qualifying_done = False
                    student.save()
                    return Response({'message': 'Grades for Quals MUST be EITHER S or X. Any other grade is invalid'})
                tea1= user_register.private_key
                stu1= UserRegistration.objects(name=student.name).first()
                stu2= stu1.private_key
                transaction = contract.functions.assignGradeA(stu2, grade).transact({'from': tea1})
                transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction)
                if transaction_receipt['status'] == 1:
                    return Response({'message': 'Grade submitted!!', 'grade for qualifying exam': grade})
                else:
                    return Response({'message': 'Grade not submitted. Trouble in the chain!!'})
        # Return the response
        return Response({'message': 'Some error with processing. Check input types'})
    else:
        # Return validation error response
        return Response(serializer.errors, status=400)



@api_view(['POST'])
def check_status_qual(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        token = serializer.validated_data['token']
        # Check if user exists and token is valid
        user_login = UserLogin.objects(name=name).first()
        if not user_login:
            return Response({'message': 'User not registered'})
        try:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            if decoded_token['name'] != name:
                raise jwt.DecodeError
            if datetime.fromtimestamp(decoded_token['exp']) < datetime.utcnow():
                raise jwt.ExpiredSignatureError
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Session has ended. Do a fresh login'})
        except jwt.DecodeError:
            return Response({'message': 'Invalid token'})
        # Check if the user has the role 'student'
        user = Student.objects(name=name).first()
        if not user:
            return Response({'message': 'Only students can check status for the applied exam'})
        # Check if 'partners' field is blank
        # Check if all partners are present in 'permissions_obtained' field
        missing_permissions = [partner for partner in user.partners_qual if partner not in user.permissions_obtained_qual]
        if missing_permissions:
            return Response({'message': 'Some permissions are pending', 'missing_permissions': missing_permissions})
        else:
            return Response({'message': 'All professors approved. You can sit for the qualifying exam', 'qual_status': user.qualifying_done})
    else:
        # Return validation error response
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def get_grade_qual(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        # Check if the user has the role 'student'
        user_register = UserRegistration.objects(name=name).first()
        if not user_register:
            return Response({'message': 'this student has not registered. So cant have a grade in Quals'})
        if user_register.role == "student":
            user = Student.objects(name=name).first()
        else:
            return Response({'message': 'Only students can get a Quals grade, not profs'})
        user = Student.objects(name=name).first()
        if not user:
            return Response({'message': 'Only students can appear for Quals'})
        student_address = user_register.private_key
        grade = contract.functions.getStudentGradeA(student_address).call()
        return Response({"grade for Quals":  grade})



##############################################################################################################################
################################ Thesis 1 (can only take thesis once you have passed qualifying exams) #######################
##############################################################################################################################

@api_view(['POST'])
def apply_for_thesis1(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        token = serializer.validated_data['token']
        # Check if user exists and token is valid
        user_login = UserLogin.objects(name=name).first()
        if not user_login:
            return Response({'message': 'User not registered'})
        try:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            if decoded_token['name'] != name:
                raise jwt.DecodeError
            if datetime.fromtimestamp(decoded_token['exp']) < datetime.utcnow():
                raise jwt.ExpiredSignatureError
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Session has ended. Do a fresh login'})
        except jwt.DecodeError:
            return Response({'message': 'Invalid token'})    
        # Check if the user has the role 'student'
        user_register = UserRegistration.objects(name=name).first()
        if user_register.role == "student":
            user = Student.objects(name=name).first()
        else:
            return Response({'message': 'Only students can apply for the Thesis-1'})
        sender_account = user_register.private_key
        user = Student.objects(name=name).first()
        if not user:
            return Response({'message': 'Only students can apply for the Thesis-1'})
        # Get the list of professors' names from the request data
        if user.qualifying_done == False:
            return Response({'message': 'Need to pass qualifying exam before starting first thesis credits'})
        professors = request.data.get('profs_guides', [])
        if not isinstance(professors, list):
            return Response({'message': 'Invalid professors data format'})
        # Check if the professors' names exist in the database
        existing_professors = Professor.objects(name__in=professors)
        if len(existing_professors) != len(professors):
            return Response({'message': 'Some professors do not exist in the database'})
        # Add professors to the student's 'partners' field
        user.partners = professors
        user.save()
        teachers=[]
        # Add the student's name to the professors' 'permissions_pending' field
        for professor in existing_professors:
            prof_register = UserRegistration.objects(name=professor.name).first()
            acc1=prof_register.private_key
            teachers.append(acc1)
            prof_register.save()
            professor.save()
        transaction = contract.functions.requestApproval(teachers).transact({
            'from': sender_account})
        # Wait for the transaction to be mined
        transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction)
        if transaction_receipt['status'] == 1:
            return Response({'message': 'Application for Theis 1 submitted successfully. The chain is fine!!'})
        else:
            return Response({'message': 'Trouble in the chain!!'})
    else:
        # Return validation error response
        return Response(serializer.errors, status=400)



@api_view(['POST'])
def approve_thesis1(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        token = serializer.validated_data['token']
        # Check if user exists and token is valid
        user_login = UserLogin.objects(name=name).first()
        if not user_login:
            return Response({'message': 'User not registered'})
        try:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            if decoded_token['name'] != name:
                raise jwt.DecodeError
            if datetime.fromtimestamp(decoded_token['exp']) < datetime.utcnow():
                raise jwt.ExpiredSignatureError
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Session has ended. Do a fresh login'})
        except jwt.DecodeError:
            return Response({'message': 'Invalid token'})
        # Check if the user has the role 'professor'
        user = Professor.objects(name=name).first()
        if not user:
            return Response({'message': 'Only professors can approve requests for thesis'})
        # Check if the user has the role 'professor'
        user_register = UserRegistration.objects(name=name).first()
        if user_register.role == "professor":
            user = Professor.objects(name=name).first()
        else:
            return Response({'message': 'Only professors are allowed to approve thesis requests'})
        # Get the list of student names from the request data
        students = request.data.get('student', [])
        if not isinstance(students, list):
            return Response({'message': 'Invalid students data format'})
        # Check if the student names exist in the database
        existing_students = Student.objects(name__in=students)
        if len(existing_students) != len(students):
            return Response({'message': 'Some students do not exist in the database'})
        # Process each student and update their 'permissions_obtained' field
        for student in existing_students:
            if name in student.partners:
                if not student.qualifying_done:
                    return Response({'message': 'Need to pass qualifying exam before starting first thesis credits'})
                tea1= user_register.private_key
                stu1= UserRegistration.objects(name=student.name).first()
                stu2= stu1.private_key
                transaction = contract.functions.approveRequest(stu2).transact({'from': tea1})
                transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction)
                if transaction_receipt['status'] == 1:
                    student.permissions_obtained.append(name)
                    student.save()
                    return Response({'message': 'Application for thesis1 has been approved!!', 'by': user_register.name})
                else:
                    return Response({'message': ' Trouble in the chain!!'})
        # Return the response
        return Response({'message': 'Some error with processing. Check input types'})
    else:
        # Return validation error response
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def assign_grade_thesis1(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        token = serializer.validated_data['token']
        # Check if user exists and token is valid
        user_login = UserLogin.objects(name=name).first()
        if not user_login:
            return Response({'message': 'User not registered'})
        try:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            if decoded_token['name'] != name:
                raise jwt.DecodeError
            if datetime.fromtimestamp(decoded_token['exp']) < datetime.utcnow():
                raise jwt.ExpiredSignatureError
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Session has ended. Do a fresh login'})
        except jwt.DecodeError:
            return Response({'message': 'Invalid token'})
        # Check if the user has the role 'professor'
        user = Professor.objects(name=name).first()
        if not user:
            return Response({'message': 'Only professors can assign grades for thesis'})
        # Check if the user has the role 'professor'
        user_register = UserRegistration.objects(name=name).first()
        if user_register.role == "professor":
            user = Professor.objects(name=name).first()
        else:
            return Response({'message': 'Only professors are allowed'})
        # Get the list of student names from the request data
        students = request.data.get('student', [])
        grade = request.data.get('grade')
        if not isinstance(students, list):
            return Response({'message': 'Invalid students data format'})
        # Check if the student names exist in the database
        existing_students = Student.objects(name__in=students)
        if len(existing_students) != len(students):
            return Response({'message': 'Some students do not exist in the database'})
        # Process each student and update their 'permissions_obtained' field
        for student in existing_students:
            if name in student.partners:
                if not student.qualifying_done:
                    return Response({'message': 'Need to pass qualifying exam before starting first thesis credits'})
                if grade == "S":
                    student.courses_grades["thesis1"]=grade
                    student.thesis1_done = True
                    student.save()
                elif grade == "X":
                    student.courses_grades["thesis1"]=grade
                    student.thesis1_done = False
                    student.save()
                else:
                    student.thesis1_done = False
                    student.save()
                    return Response({'message': 'Grades for Thesis 1 MUST be EITHER S or X. Any other grade is invalid'})
                tea1= user_register.private_key
                stu1= UserRegistration.objects(name=student.name).first()
                stu2= stu1.private_key
                transaction = contract.functions.assignGrade(stu2, grade).transact({'from': tea1})
                transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction)
                if transaction_receipt['status'] == 1:
                    return Response({'message': 'Grade submitted!!', 'grade for thesis1': grade})
                else:
                    return Response({'message': 'Grade not submitted. Trouble in the chain!!'})
        # Return the response
        return Response({'message': 'Some error with processing. Check input types'})
    else:
        # Return validation error response
        return Response(serializer.errors, status=400)



@api_view(['POST'])
def add_extra_thesis1_advisor(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        token = serializer.validated_data['token']
        # Check if user exists and token is valid
        user_login = UserLogin.objects(name=name).first()
        if not user_login:
            return Response({'message': 'User not registered'})
        try:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            if decoded_token['name'] != name:
                raise jwt.DecodeError
            if datetime.fromtimestamp(decoded_token['exp']) < datetime.utcnow():
                raise jwt.ExpiredSignatureError
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Session has ended. Do a fresh login'})
        except jwt.DecodeError:
            return Response({'message': 'Invalid token'})
        # Check if the user has the role 'professor'
        user = Professor.objects(name=name).first()
        if not user:
            return Response({'message': 'Only professors can assign extra thesis advisor for already existing ones'})
        # Check if the user has the role 'professor'
        user_register = UserRegistration.objects(name=name).first()
        if user_register.role == "professor":
            user = Professor.objects(name=name).first()
        else:
            return Response({'message': 'Only professors are allowed'})
        # Get the list of student names from the request data
        students = request.data.get('student', [])
        prof_name = request.data.get('extra_thesis_advisor')
        prof_namee= UserRegistration.objects(name=prof_name).first()
        prof_key2= prof_namee.private_key
        if not isinstance(students, list):
            return Response({'message': 'Invalid students data format'})
        # Check if the student names exist in the database
        existing_students = Student.objects(name__in=students)
        if len(existing_students) != len(students):
            return Response({'message': 'Some students do not exist in the database'})
        # Process each student and update their 'permissions_obtained' field
        for student in existing_students:
            if name in student.partners:
                if not student.qualifying_done:
                    return Response({'message': 'Need to pass qualifying exam before starting first thesis credits'})
                tea1= user_register.private_key
                stu1= UserRegistration.objects(name=student.name).first()
                stu2= stu1.private_key
                transaction = contract.functions.addTeacherToRequest(stu2, prof_key2).transact({'from': tea1})
                transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction)
                if transaction_receipt['status'] == 1:
                    student.partners.append(prof_name)
                    student.save()
                    return Response({'message': 'Extra prof added to list of thesis advisers!!'})
                else:
                    return Response({'message': 'Extra advisor not added. Trouble in the chain!!'})
        # Return the response
        return Response({'message': 'Some error with processing. Check input types'})
    else:
        # Return validation error response
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def check_status_thesis1(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        token = serializer.validated_data['token']
        # Check if user exists and token is valid
        user_login = UserLogin.objects(name=name).first()
        if not user_login:
            return Response({'message': 'User not registered'})
        try:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            if decoded_token['name'] != name:
                raise jwt.DecodeError
            if datetime.fromtimestamp(decoded_token['exp']) < datetime.utcnow():
                raise jwt.ExpiredSignatureError
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Session has ended. Do a fresh login'})
        except jwt.DecodeError:
            return Response({'message': 'Invalid token'})
        # Check if the user has the role 'student'
        user = Student.objects(name=name).first()
        if not user:
            return Response({'message': 'Only students can check status for the applied exam'})
        # Check if 'partners' field is blank
        # Check if all partners are present in 'permissions_obtained' field
        missing_permissions = [partner for partner in user.partners if partner not in user.permissions_obtained]
        if missing_permissions:
            return Response({'message': 'Some permissions are pending', 'missing_permissions': missing_permissions})
        else:
            return Response({'message': 'All professors approved. You can sit for the exam'})
    else:
        # Return validation error response
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def get_grade_thesis1(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        # Check if the user has the role 'student'
        user_register = UserRegistration.objects(name=name).first()
        if not user_register:
            return Response({'message': 'this student has not registered. So cant have a thesis grade'})
        if user_register.role == "student":
            user = Student.objects(name=name).first()
        else:
            return Response({'message': 'Only students can get a thesis grae, not profs'})
        user = Student.objects(name=name).first()
        if not user:
            return Response({'message': 'Only students can appear for thesis'})
        student_address = user_register.private_key
        grade = contract.functions.getStudentGrade(student_address).call()
        return Response({"grade for thesis 1":  grade})

######################################################################################################################################################
########################### Thesis 2 , thesis 1 and thesis 2 will have same set of advisors ##########################################################
############################thesis 2 to be done only after thesis 1 is done ###########################################################
################################## Thesis 2 must have the same set of advisors as thesis 1 (obviously) ####################################################################################################################

@api_view(['POST'])
def apply_for_thesis2(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        token = serializer.validated_data['token']
        # Check if user exists and token is valid
        user_login = UserLogin.objects(name=name).first()
        if not user_login:
            return Response({'message': 'User not registered'})
        try:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            if decoded_token['name'] != name:
                raise jwt.DecodeError
            if datetime.fromtimestamp(decoded_token['exp']) < datetime.utcnow():
                raise jwt.ExpiredSignatureError
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Session has ended. Do a fresh login'})
        except jwt.DecodeError:
            return Response({'message': 'Invalid token'})    
        # Check if the user has the role 'student'
        user_register = UserRegistration.objects(name=name).first()
        if user_register.role == "student":
            user = Student.objects(name=name).first()
        else:
            return Response({'message': 'Only students can apply for the Thesis-2'})
        sender_account = user_register.private_key
        user = Student.objects(name=name).first()
        if not user:
            return Response({'message': 'Only students can apply for the Thesis-2'})
        if user.thesis1_done == False:
            return Response({'message': 'Need to pass thesis1 before starting thesis2'})
        # Get the list of professors' names from the request data
        #professors = request.data.get('partners', [])
        ## The set of advisers for thesis 2 should be the same as thesis 1 
        ## so need to take the set of advisers as input, instead directly take thesis 1 partners 
        professors =[]
        for guy in user.partners:
            professors.append(guy)
        if not isinstance(professors, list):
            return Response({'message': 'Invalid professors data format'})
        # Check if the professors' names exist in the database
        existing_professors = Professor.objects(name__in=professors)
        if len(existing_professors) != len(professors):
            return Response({'message': 'Some professors do not exist in the database'})
        # Add professors to the student's 'partners' field
        user.partners_thesis2 = professors
        user.save()
        teachers=[]
        # Add the student's name to the professors' 'permissions_pending' field
        for professor in existing_professors:
            prof_register = UserRegistration.objects(name=professor.name).first()
            acc1=prof_register.private_key
            teachers.append(acc1)
            prof_register.save()
            professor.save()
        transaction = contract.functions.requestApprovalAA(teachers).transact({
            'from': sender_account})
        # Wait for the transaction to be mined
        transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction)
        if transaction_receipt['status'] == 1:
            return Response({'message': 'Application for Thesis 2 submitted successfully. The chain is fine!!'})
        else:
            return Response({'message': 'Trouble in the chain!!'})
    else:
        # Return validation error response
        return Response(serializer.errors, status=400)



@api_view(['POST'])
def approve_thesis2(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        token = serializer.validated_data['token']
        # Check if user exists and token is valid
        user_login = UserLogin.objects(name=name).first()
        if not user_login:
            return Response({'message': 'User not registered'})
        try:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            if decoded_token['name'] != name:
                raise jwt.DecodeError
            if datetime.fromtimestamp(decoded_token['exp']) < datetime.utcnow():
                raise jwt.ExpiredSignatureError
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Session has ended. Do a fresh login'})
        except jwt.DecodeError:
            return Response({'message': 'Invalid token'})
        # Check if the user has the role 'professor'
        user = Professor.objects(name=name).first()
        if not user:
            return Response({'message': 'Only professors can approve requests for thesis'})
        # Check if the user has the role 'professor'
        user_register = UserRegistration.objects(name=name).first()
        if user_register.role == "professor":
            user = Professor.objects(name=name).first()
        else:
            return Response({'message': 'Only professors are allowed to approve thesis requests'})
        # Get the list of student names from the request data
        students = request.data.get('student', [])
        if not isinstance(students, list):
            return Response({'message': 'Invalid students data format'})
        # Check if the student names exist in the database
        existing_students = Student.objects(name__in=students)
        if len(existing_students) != len(students):
            return Response({'message': 'Some students do not exist in the database'})
        # Process each student and update their 'permissions_obtained' field
        for student in existing_students:
            if name in student.partners_thesis2:
                if student.thesis1_done == False:
                    return Response({'message': 'Need to pass thesis1 before starting thesis2'})
                tea1= user_register.private_key
                stu1= UserRegistration.objects(name=student.name).first()
                stu2= stu1.private_key
                transaction = contract.functions.approveRequestAA(stu2).transact({'from': tea1})
                transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction)
                if transaction_receipt['status'] == 1:
                    student.permissions_obtained_thesis2.append(name)
                    student.save()
                    return Response({'message': 'Application for thesis2 has been approved!!', 'by': user_register.name})
                else:
                    return Response({'message': ' Trouble in the chain!!'})
        # Return the response
        return Response({'message': 'Some error with processing. Check input types'})
    else:
        # Return validation error response
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def assign_grade_thesis2(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        token = serializer.validated_data['token']
        # Check if user exists and token is valid
        user_login = UserLogin.objects(name=name).first()
        if not user_login:
            return Response({'message': 'User not registered'})
        try:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            if decoded_token['name'] != name:
                raise jwt.DecodeError
            if datetime.fromtimestamp(decoded_token['exp']) < datetime.utcnow():
                raise jwt.ExpiredSignatureError
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Session has ended. Do a fresh login'})
        except jwt.DecodeError:
            return Response({'message': 'Invalid token'})
        # Check if the user has the role 'professor'
        user = Professor.objects(name=name).first()
        if not user:
            return Response({'message': 'Only professors can assign grades for thesis'})
        # Check if the user has the role 'professor'
        user_register = UserRegistration.objects(name=name).first()
        if user_register.role == "professor":
            user = Professor.objects(name=name).first()
        else:
            return Response({'message': 'Only professors are allowed'})
        # Get the list of student names from the request data
        students = request.data.get('student', [])
        grade = request.data.get('grade')
        if not isinstance(students, list):
            return Response({'message': 'Invalid students data format'})
        # Check if the student names exist in the database
        existing_students = Student.objects(name__in=students)
        if len(existing_students) != len(students):
            return Response({'message': 'Some students do not exist in the database'})
        # Process each student and update their 'permissions_obtained' field
        for student in existing_students:
            if name in student.partners_thesis2:
                if student.thesis1_done == False:
                    return Response({'message': 'Need to pass thesis1 before starting thesis2'})
                if grade == "S":
                    student.courses_grades["thesis2"]=grade
                    student.thesis2_done = True
                    student.save()
                elif grade == "X":
                    student.courses_grades["thesis2"]=grade
                    student.thesis2_done = False
                    student.save()
                else:
                    student.thesis2_done = False
                    student.save()
                    return Response({'message': 'Grades for Thesis 2 MUST be EITHER S or X. Any other grade is invalid'})
                tea1= user_register.private_key
                stu1= UserRegistration.objects(name=student.name).first()
                stu2= stu1.private_key
                transaction = contract.functions.assignGradeAA(stu2, grade).transact({'from': tea1})
                transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction)
                if transaction_receipt['status'] == 1:
                    return Response({'message': 'Grade submitted!!', 'grade for thesis2': grade})
                else:
                    return Response({'message': 'Grade not submitted. Trouble in the chain!!'})
        # Return the response
        return Response({'message': 'Some error with processing. Check input types'})
    else:
        # Return validation error response
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def check_status_thesis2(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        token = serializer.validated_data['token']
        # Check if user exists and token is valid
        user_login = UserLogin.objects(name=name).first()
        if not user_login:
            return Response({'message': 'User not registered'})
        try:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            if decoded_token['name'] != name:
                raise jwt.DecodeError
            if datetime.fromtimestamp(decoded_token['exp']) < datetime.utcnow():
                raise jwt.ExpiredSignatureError
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Session has ended. Do a fresh login'})
        except jwt.DecodeError:
            return Response({'message': 'Invalid token'})
        # Check if the user has the role 'student'
        user = Student.objects(name=name).first()
        if not user:
            return Response({'message': 'Only students can check status for thesis 2'})
        # Check if 'partners' field is blank
        # Check if all partners are present in 'permissions_obtained' field
        missing_permissions = [partner for partner in user.partners_thesis2 if partner not in user.permissions_obtained_thesis2]
        if missing_permissions:
            return Response({'message': 'Some permissions are pending', 'missing_permissions': missing_permissions})
        else:
            return Response({'message': 'All professors approved. You can start thesis 2'})
    else:
        # Return validation error response
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def get_grade_thesis2(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        # Check if the user has the role 'student'
        user_register = UserRegistration.objects(name=name).first()
        if not user_register:
            return Response({'message': 'this student has not registered. So cant have a thesis grade'})
        if user_register.role == "student":
            user = Student.objects(name=name).first()
        else:
            return Response({'message': 'Only students can get a thesis grae, not profs'})
        user = Student.objects(name=name).first()
        if not user:
            return Response({'message': 'Only students can appear for thesis'})
        student_address = user_register.private_key
        grade = contract.functions.getStudentGradeAA(student_address).call()
        return Response({"grade for thesis 2":  grade})


###############################################################################################################################
######################## SOTA .. can be done anytime after quals (even before thesis credits are over) ########################
####################### SOTA professors' committee should have atleast all the thesis advisers as well ########################
################### Some extra profs can also be added to SOTA committee by thesis adviser ####################################
###############################################################################################################################


@api_view(['POST'])
def apply_for_sota(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        token = serializer.validated_data['token']
        # Check if user exists and token is valid
        user_login = UserLogin.objects(name=name).first()
        if not user_login:
            return Response({'message': 'User not registered'})
        try:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            if decoded_token['name'] != name:
                raise jwt.DecodeError
            if datetime.fromtimestamp(decoded_token['exp']) < datetime.utcnow():
                raise jwt.ExpiredSignatureError
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Session has ended. Do a fresh login'})
        except jwt.DecodeError:
            return Response({'message': 'Invalid token'})    
        # Check if the user has the role 'student'
        user_register = UserRegistration.objects(name=name).first()
        if user_register.role == "student":
            user = Student.objects(name=name).first()
        else:
            return Response({'message': 'Only students can apply for SOTA'})
        sender_account = user_register.private_key
        user = Student.objects(name=name).first()
        if not user:
            return Response({'message': 'Only students can apply for SOTA'})
        # Get the list of professors' names from the request data
        if user.qualifying_done == False:
            return Response({'message': 'Need to pass qualifying exam before SOTA'})
        ## The set of advisers for sota should have all the thesis advisers, along with extra (if any) appointed by thesis adviser
        ## so no need to take the set of advisers as input by user, instead directly take thesis 1 partners 
        professors =[]
        for guy in user.partners:
            professors.append(guy)
        #professors = request.data.get('partners', [])
        if not isinstance(professors, list):
            return Response({'message': 'Invalid professors data format'})
        # Check if the professors' names exist in the database
        existing_professors = Professor.objects(name__in=professors)
        if len(existing_professors) != len(professors):
            return Response({'message': 'Some professors do not exist in the database'})
        # Add professors to the student's 'partners' field
        user.partners_sota = professors
        user.save()
        teachers=[]
        # Add the student's name to the professors' 'permissions_pending' field
        for professor in existing_professors:
            prof_register = UserRegistration.objects(name=professor.name).first()
            acc1=prof_register.private_key
            teachers.append(acc1)
            prof_register.save()
            professor.save()
        transaction = contract.functions.requestApprovalB(teachers).transact({
            'from': sender_account})
        # Wait for the transaction to be mined
        transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction)
        if transaction_receipt['status'] == 1:
            return Response({'message': 'Application for SOTA submitted successfully. The chain is fine!!'})
        else:
            return Response({'message': 'Trouble in the chain!!'})
    else:
        # Return validation error response
        return Response(serializer.errors, status=400)



@api_view(['POST'])
def approve_sota(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        token = serializer.validated_data['token']
        # Check if user exists and token is valid
        user_login = UserLogin.objects(name=name).first()
        if not user_login:
            return Response({'message': 'User not registered'})
        try:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            if decoded_token['name'] != name:
                raise jwt.DecodeError
            if datetime.fromtimestamp(decoded_token['exp']) < datetime.utcnow():
                raise jwt.ExpiredSignatureError
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Session has ended. Do a fresh login'})
        except jwt.DecodeError:
            return Response({'message': 'Invalid token'})
        # Check if the user has the role 'professor'
        user = Professor.objects(name=name).first()
        if not user:
            return Response({'message': 'Only professors can approve requests for SOTA'})
        # Check if the user has the role 'professor'
        user_register = UserRegistration.objects(name=name).first()
        if user_register.role == "professor":
            user = Professor.objects(name=name).first()
        else:
            return Response({'message': 'Only professors are allowed to approve SOTA requests'})
        # Get the list of student names from the request data
        students = request.data.get('student', [])
        if not isinstance(students, list):
            return Response({'message': 'Invalid students data format'})
        # Check if the student names exist in the database
        existing_students = Student.objects(name__in=students)
        if len(existing_students) != len(students):
            return Response({'message': 'Some students do not exist in the database'})
        # Process each student and update their 'permissions_obtained' field
        for student in existing_students:
            if name in student.partners_sota:
                if not student.qualifying_done:
                    return Response({'message': 'Need to pass qualifying exam before SOTA'})
                tea1= user_register.private_key
                stu1= UserRegistration.objects(name=student.name).first()
                stu2= stu1.private_key
                transaction = contract.functions.approveRequestB(stu2).transact({'from': tea1})
                transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction)
                if transaction_receipt['status'] == 1:
                    student.permissions_obtained_sota.append(name)
                    student.save()
                    return Response({'message': 'Application for SOTA has been approved!!', 'by': user_register.name})
                else:
                    return Response({'message': ' Trouble in the chain!!'})
        # Return the response
        return Response({'message': 'Some error with processing. Check input types'})
    else:
        # Return validation error response
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def assign_grade_sota(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        token = serializer.validated_data['token']
        # Check if user exists and token is valid
        user_login = UserLogin.objects(name=name).first()
        if not user_login:
            return Response({'message': 'User not registered'})
        try:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            if decoded_token['name'] != name:
                raise jwt.DecodeError
            if datetime.fromtimestamp(decoded_token['exp']) < datetime.utcnow():
                raise jwt.ExpiredSignatureError
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Session has ended. Do a fresh login'})
        except jwt.DecodeError:
            return Response({'message': 'Invalid token'})
        # Check if the user has the role 'professor'
        user = Professor.objects(name=name).first()
        if not user:
            return Response({'message': 'Only professors can assign grades for SOTA'})
        # Check if the user has the role 'professor'
        user_register = UserRegistration.objects(name=name).first()
        if user_register.role == "professor":
            user = Professor.objects(name=name).first()
        else:
            return Response({'message': 'Only professors are allowed'})
        # Get the list of student names from the request data
        students = request.data.get('student', [])
        grade = request.data.get('grade')
        if not isinstance(students, list):
            return Response({'message': 'Invalid students data format'})
        # Check if the student names exist in the database
        existing_students = Student.objects(name__in=students)
        if len(existing_students) != len(students):
            return Response({'message': 'Some students do not exist in the database'})
        # Process each student and update their 'permissions_obtained' field
        for student in existing_students:
            if name in student.partners_sota:
                if not student.qualifying_done:
                    return Response({'message': 'Need to pass qualifying exam before SOTA'})
                if grade == "S":
                    student.courses_grades["sota"]=grade
                    student.sota_done = True
                    student.save()
                elif grade == "X":
                    student.courses_grades["sota"]=grade
                    student.sota_done = False
                    student.save()
                else:
                    student.sota_done = False
                    student.save()
                    return Response({'message': 'Grades for SOTA MUST be EITHER S or X. Any other grade is invalid'})
                tea1= user_register.private_key
                stu1= UserRegistration.objects(name=student.name).first()
                stu2= stu1.private_key
                transaction = contract.functions.assignGradeB(stu2, grade).transact({'from': tea1})
                transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction)
                if transaction_receipt['status'] == 1:
                    return Response({'message': 'Grade submitted!!', 'grade for sota': grade})
                else:
                    return Response({'message': 'Grade not submitted. Trouble in the chain!!'})
        # Return the response
        return Response({'message': 'Some error with processing. Check input types'})
    else:
        # Return validation error response
        return Response(serializer.errors, status=400)



@api_view(['POST'])
def add_extra_sota_advisor(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        token = serializer.validated_data['token']
        # Check if user exists and token is valid
        user_login = UserLogin.objects(name=name).first()
        if not user_login:
            return Response({'message': 'User not registered'})
        try:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            if decoded_token['name'] != name:
                raise jwt.DecodeError
            if datetime.fromtimestamp(decoded_token['exp']) < datetime.utcnow():
                raise jwt.ExpiredSignatureError
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Session has ended. Do a fresh login'})
        except jwt.DecodeError:
            return Response({'message': 'Invalid token'})
        # Check if the user has the role 'professor'
        user = Professor.objects(name=name).first()
        if not user:
            return Response({'message': 'Only professors can assign extra SOTA profs to already existing ones'})
        # Check if the user has the role 'professor'
        user_register = UserRegistration.objects(name=name).first()
        if user_register.role == "professor":
            user = Professor.objects(name=name).first()
        else:
            return Response({'message': 'Only professors are allowed'})
        # Get the list of student names from the request data
        students = request.data.get('student', [])
        prof_name = request.data.get('extra_sota_advisor')
        prof_namee= UserRegistration.objects(name=prof_name).first()
        prof_key2= prof_namee.private_key
        if not isinstance(students, list):
            return Response({'message': 'Invalid students data format'})
        # Check if the student names exist in the database
        existing_students = Student.objects(name__in=students)
        if len(existing_students) != len(students):
            return Response({'message': 'Some students do not exist in the database'})
        # Process each student and update their 'permissions_obtained' field
        for student in existing_students:
            if name in student.partners_sota:
                if not student.qualifying_done:
                    return Response({'message': 'Need to pass qualifying exam before sota'})
                tea1= user_register.private_key
                stu1= UserRegistration.objects(name=student.name).first()
                stu2= stu1.private_key
                transaction = contract.functions.addTeacherToRequestB(stu2, prof_key2).transact({'from': tea1})
                transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction)
                if transaction_receipt['status'] == 1:
                    student.partners_sota.append(prof_name)
                    student.save()
                    return Response({'message': 'Extra prof added to list of SOTA advisers!!'})
                else:
                    return Response({'message': 'Extra SOTA advisor not added. Trouble in the chain!!'})
        # Return the response
        return Response({'message': 'Some error with processing. Check input types'})
    else:
        # Return validation error response
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def check_status_sota(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        token = serializer.validated_data['token']
        # Check if user exists and token is valid
        user_login = UserLogin.objects(name=name).first()
        if not user_login:
            return Response({'message': 'User not registered'})
        try:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            if decoded_token['name'] != name:
                raise jwt.DecodeError
            if datetime.fromtimestamp(decoded_token['exp']) < datetime.utcnow():
                raise jwt.ExpiredSignatureError
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Session has ended. Do a fresh login'})
        except jwt.DecodeError:
            return Response({'message': 'Invalid token'})
        # Check if the user has the role 'student'
        user = Student.objects(name=name).first()
        if not user:
            return Response({'message': 'Only students can check status for the SOTA exam'})
        # Check if 'partners' field is blank
        # Check if all partners are present in 'permissions_obtained' field
        missing_permissions = [partner for partner in user.partners_sota if partner not in user.permissions_obtained_sota]
        if missing_permissions:
            return Response({'message': 'Some permissions are pending', 'missing_permissions': missing_permissions})
        else:
            return Response({'message': 'All professors approved. You can sit for SOTA'})
    else:
        # Return validation error response
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def get_grade_sota(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        # Check if the user has the role 'student'
        user_register = UserRegistration.objects(name=name).first()
        if not user_register:
            return Response({'message': 'this student has not registered. So cant have a SOTA grade'})
        if user_register.role == "student":
            user = Student.objects(name=name).first()
        else:
            return Response({'message': 'Only students can get a SOTA grade, not profs'})
        user = Student.objects(name=name).first()
        if not user:
            return Response({'message': 'Only students can appear for SOTA'})
        student_address = user_register.private_key
        grade = contract.functions.getStudentGradeB(student_address).call()
        return Response({"grade for SOTA":  grade})



###############################################################################################################################
######################## Defence .. can be done anytime after both SOTA and thesis credits are OVER ########################
####################### Defence committee should have atleast all the thesis advisers as well ########################
################### Some extra profs can also be added to Defence committee by thesis adviser ####################################
###############################################################################################################################



@api_view(['POST'])
def apply_for_defence(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        token = serializer.validated_data['token']
        # Check if user exists and token is valid
        user_login = UserLogin.objects(name=name).first()
        if not user_login:
            return Response({'message': 'User not registered'})
        try:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            if decoded_token['name'] != name:
                raise jwt.DecodeError
            if datetime.fromtimestamp(decoded_token['exp']) < datetime.utcnow():
                raise jwt.ExpiredSignatureError
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Session has ended. Do a fresh login'})
        except jwt.DecodeError:
            return Response({'message': 'Invalid token'})    
        # Check if the user has the role 'student'
        user_register = UserRegistration.objects(name=name).first()
        if user_register.role == "student":
            user = Student.objects(name=name).first()
        else:
            return Response({'message': 'Only students can apply for defence'})
        sender_account = user_register.private_key
        user = Student.objects(name=name).first()
        if not user:
            return Response({'message': 'Only students can apply for defence'})
        # Get the list of professors' names from the request data
        if user.qualifying_done == False:
            return Response({'message': 'Need to pass qualifying exam before defence'})
        ## The set of advisers for sota should have all the thesis advisers, along with extra (if any) appointed by thesis adviser
        ## so no need to take the set of advisers as input by user, instead directly take thesis 1 partners 
        if user.sota_done == False:
            return Response({'message': 'Need to finish SOTA before defence'})
        professors =[]
        for guy in user.partners:
            professors.append(guy)
        #professors = request.data.get('partners', [])
        if not isinstance(professors, list):
            return Response({'message': 'Invalid professors data format'})
        # Check if the professors' names exist in the database
        existing_professors = Professor.objects(name__in=professors)
        if len(existing_professors) != len(professors):
            return Response({'message': 'Some professors do not exist in the database'})
        # Add professors to the student's 'partners' field
        user.partners_defence = professors
        user.save()
        teachers=[]
        # Add the student's name to the professors' 'permissions_pending' field
        for professor in existing_professors:
            prof_register = UserRegistration.objects(name=professor.name).first()
            acc1=prof_register.private_key
            teachers.append(acc1)
            prof_register.save()
            professor.save()
        transaction = contract.functions.requestApprovalBB(teachers).transact({
            'from': sender_account})
        # Wait for the transaction to be mined
        transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction)
        if transaction_receipt['status'] == 1:
            return Response({'message': 'Application for Defence submitted successfully. The chain is fine!!'})
        else:
            return Response({'message': 'Trouble in the chain!!'})
    else:
        # Return validation error response
        return Response(serializer.errors, status=400)



@api_view(['POST'])
def approve_defence(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        token = serializer.validated_data['token']
        # Check if user exists and token is valid
        user_login = UserLogin.objects(name=name).first()
        if not user_login:
            return Response({'message': 'User not registered'})
        try:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            if decoded_token['name'] != name:
                raise jwt.DecodeError
            if datetime.fromtimestamp(decoded_token['exp']) < datetime.utcnow():
                raise jwt.ExpiredSignatureError
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Session has ended. Do a fresh login'})
        except jwt.DecodeError:
            return Response({'message': 'Invalid token'})
        # Check if the user has the role 'professor'
        user = Professor.objects(name=name).first()
        if not user:
            return Response({'message': 'Only professors can approve requests for Defence'})
        # Check if the user has the role 'professor'
        user_register = UserRegistration.objects(name=name).first()
        if user_register.role == "professor":
            user = Professor.objects(name=name).first()
        else:
            return Response({'message': 'Only professors are allowed to approve Defence requests'})
        # Get the list of student names from the request data
        students = request.data.get('student', [])
        if not isinstance(students, list):
            return Response({'message': 'Invalid students data format'})
        # Check if the student names exist in the database
        existing_students = Student.objects(name__in=students)
        if len(existing_students) != len(students):
            return Response({'message': 'Some students do not exist in the database'})
        # Process each student and update their 'permissions_obtained' field
        for student in existing_students:
            if name in student.partners_defence:
                if not student.qualifying_done:
                    return Response({'message': 'Need to pass qualifying exam before Defence'})
                if not student.sota_done:
                    return Response({'message': 'Need to finish SOTA before defence'})
                tea1= user_register.private_key
                stu1= UserRegistration.objects(name=student.name).first()
                stu2= stu1.private_key
                transaction = contract.functions.approveRequestBB(stu2).transact({'from': tea1})
                transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction)
                if transaction_receipt['status'] == 1:
                    student.permissions_obtained_defence.append(name)
                    student.save()
                    return Response({'message': 'Application for Defence has been approved!!', 'by': user_register.name})
                else:
                    return Response({'message': ' Trouble in the chain!!'})
        # Return the response
        return Response({'message': 'Some error with processing. Check input types'})
    else:
        # Return validation error response
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def assign_grade_defence(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        token = serializer.validated_data['token']
        # Check if user exists and token is valid
        user_login = UserLogin.objects(name=name).first()
        if not user_login:
            return Response({'message': 'User not registered'})
        try:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            if decoded_token['name'] != name:
                raise jwt.DecodeError
            if datetime.fromtimestamp(decoded_token['exp']) < datetime.utcnow():
                raise jwt.ExpiredSignatureError
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Session has ended. Do a fresh login'})
        except jwt.DecodeError:
            return Response({'message': 'Invalid token'})
        # Check if the user has the role 'professor'
        user = Professor.objects(name=name).first()
        if not user:
            return Response({'message': 'Only professors can assign grades for SOTA'})
        # Check if the user has the role 'professor'
        user_register = UserRegistration.objects(name=name).first()
        if user_register.role == "professor":
            user = Professor.objects(name=name).first()
        else:
            return Response({'message': 'Only professors are allowed'})
        # Get the list of student names from the request data
        students = request.data.get('student', [])
        grade = request.data.get('grade')
        if not isinstance(students, list):
            return Response({'message': 'Invalid students data format'})
        # Check if the student names exist in the database
        existing_students = Student.objects(name__in=students)
        if len(existing_students) != len(students):
            return Response({'message': 'Some students do not exist in the database'})
        # Process each student and update their 'permissions_obtained' field
        for student in existing_students:
            if name in student.partners_defence:
                if not student.qualifying_done:
                    return Response({'message': 'Need to pass qualifying exam before defence'})
                if not student.sota_done:
                    return Response({'message': 'Need to finish SOTA before defence'})
                if grade == "S":
                    student.courses_grades["defence"]=grade
                    student.defence_done = True
                    student.save()
                elif grade == "X":
                    student.courses_grades["defence"]=grade
                    student.defence_done = False
                    student.save()
                else:
                    student.defence_done = False
                    student.save()
                    return Response({'message': 'Grades for defence MUST be EITHER S or X. Any other grade is invalid'})
                tea1= user_register.private_key
                stu1= UserRegistration.objects(name=student.name).first()
                stu2= stu1.private_key
                transaction = contract.functions.assignGradeBB(stu2, grade).transact({'from': tea1})
                transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction)
                if transaction_receipt['status'] == 1:
                    return Response({'message': 'Grade submitted!!', 'grade for defence': grade})
                else:
                    return Response({'message': 'Grade not submitted. Trouble in the chain!!'})
        # Return the response
        return Response({'message': 'Some error with processing. Check input types'})
    else:
        # Return validation error response
        return Response(serializer.errors, status=400)



@api_view(['POST'])
def add_extra_defence_advisor(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        token = serializer.validated_data['token']
        # Check if user exists and token is valid
        user_login = UserLogin.objects(name=name).first()
        if not user_login:
            return Response({'message': 'User not registered'})
        try:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            if decoded_token['name'] != name:
                raise jwt.DecodeError
            if datetime.fromtimestamp(decoded_token['exp']) < datetime.utcnow():
                raise jwt.ExpiredSignatureError
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Session has ended. Do a fresh login'})
        except jwt.DecodeError:
            return Response({'message': 'Invalid token'})
        # Check if the user has the role 'professor'
        user = Professor.objects(name=name).first()
        if not user:
            return Response({'message': 'Only professors can assign extra defence profs to already existing ones'})
        # Check if the user has the role 'professor'
        user_register = UserRegistration.objects(name=name).first()
        if user_register.role == "professor":
            user = Professor.objects(name=name).first()
        else:
            return Response({'message': 'Only professors are allowed'})
        # Get the list of student names from the request data
        students = request.data.get('student', [])
        prof_name = request.data.get('extra_defence_advisor')
        prof_namee= UserRegistration.objects(name=prof_name).first()
        prof_key2= prof_namee.private_key
        if not isinstance(students, list):
            return Response({'message': 'Invalid students data format'})
        # Check if the student names exist in the database
        existing_students = Student.objects(name__in=students)
        if len(existing_students) != len(students):
            return Response({'message': 'Some students do not exist in the database'})
        # Process each student and update their 'permissions_obtained' field
        for student in existing_students:
            if name in student.partners_defence:
                if not student.qualifying_done:
                    return Response({'message': 'Need to pass qualifying exam before defence'})
                if not student.sota_done:
                    return Response({'message': 'Need to finish SOTA before defence'})
                tea1= user_register.private_key
                stu1= UserRegistration.objects(name=student.name).first()
                stu2= stu1.private_key
                transaction = contract.functions.addTeacherToRequestBB(stu2, prof_key2).transact({'from': tea1})
                transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction)
                if transaction_receipt['status'] == 1:
                    student.partners_defence.append(prof_name)
                    student.save()
                    return Response({'message': 'Extra prof added to list of defence advisers!!'})
                else:
                    return Response({'message': 'Extra defence advisor not added. Trouble in the chain!!'})
        # Return the response
        return Response({'message': 'Some error with processing. Check input types'})
    else:
        # Return validation error response
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def check_status_defence(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        token = serializer.validated_data['token']
        # Check if user exists and token is valid
        user_login = UserLogin.objects(name=name).first()
        if not user_login:
            return Response({'message': 'User not registered'})
        try:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            if decoded_token['name'] != name:
                raise jwt.DecodeError
            if datetime.fromtimestamp(decoded_token['exp']) < datetime.utcnow():
                raise jwt.ExpiredSignatureError
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Session has ended. Do a fresh login'})
        except jwt.DecodeError:
            return Response({'message': 'Invalid token'})
        # Check if the user has the role 'student'
        user = Student.objects(name=name).first()
        if not user:
            return Response({'message': 'Only students can check status for defence'})
        # Check if 'partners' field is blank
        # Check if all partners are present in 'permissions_obtained' field
        missing_permissions = [partner for partner in user.partners_defence if partner not in user.permissions_obtained_defence]
        if missing_permissions:
            return Response({'message': 'Some permissions are pending', 'missing_permissions': missing_permissions})
        else:
            return Response({'message': 'All professors approved. You can sit for defence'})
    else:
        # Return validation error response
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def get_grade_defence(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        # Check if the user has the role 'student'
        user_register = UserRegistration.objects(name=name).first()
        if not user_register:
            return Response({'message': 'this student has not registered. So cant have a defence grade'})
        if user_register.role == "student":
            user = Student.objects(name=name).first()
        else:
            return Response({'message': 'Only students can get a defence grade, not profs'})
        user = Student.objects(name=name).first()
        if not user:
            return Response({'message': 'Only students can appear for defence'})
        student_address = user_register.private_key
        grade = contract.functions.getStudentGradeBB(student_address).call()
        return Response({"grade for defence":  grade})












#############################################################################################################################################
#############################################################################################################################################
##############################!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#######################################
#############################################################################################################################################
#############################################################################################################################################


