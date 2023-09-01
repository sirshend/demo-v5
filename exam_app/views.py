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

##
## Integrate the blockchain here. 
from web3 import Web3
from eth_account import Account
ganache_url = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
#contract_address = "0x89E165FC0F1A78366F68bCf917f20E219296D0Df"
#contract_address = "0x89E165FC0F1A78366F68bCf917f20E219296D0Df"
contract_address = "0x343d832ab1c2b01A2569dba8f56C929Fa9e41998"
contract_abi = [{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"student","type":"address"}],"name":"ApprovalReceived","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"student","type":"address"},{"indexed":False,"internalType":"address[]","name":"teachers","type":"address[]"}],"name":"RequestApproval","type":"event"},{"inputs":[{"internalType":"address","name":"student","type":"address"}],"name":"approveRequest","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"teachers","type":"address[]"}],"name":"requestApproval","outputs":[],"stateMutability":"nonpayable","type":"function"}]
contract = web3.eth.contract(address=contract_address, abi=contract_abi)
##
i = 0

@api_view(['POST'])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    #return Response({'message': 'User registered successfully'})
    # if serializer.is_valid():
    #     # Perform registration logic here (create user, generate private key, store in DB)
    #     # use PyECDSA here to generate private keys
    #     # Store user details in the database
    #     # Return a success response
    #     return Response({'message': 'User registered successfully'})
    # else:
    #     # Return validation error response
    #     return Response(serializer.errors, status=400)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        password = serializer.validated_data['password']
        role = serializer.validated_data['role']
        email= serializer.validated_data['email']

        # Check if user already exists
        if UserRegistration.objects(name=name).first():
            return Response({'message': 'User already exists'})

        # Generate and store keys using your ecdsa signer code (to be added later)
        # For now, just assume some dummy keys are generated
        private_key = SigningKey.generate(curve=SECP256k1)
        private_key_hex = private_key.to_string().hex()
        # hash_object = hashlib.sha256(private_key)
        # hash_hex = hash_object.hexdigest()
        # Store the user details in the database
        # user = UserRegistration(name=name, password=password, role=role, public_key=public_key, private_key=private_key)
        # user.save()
        user_registration = UserRegistration(name=name, password=password, role=role, private_key=private_key_hex)
        user_registration.save()
        if role == 'student':
            Sttudent = Student(name=name, role= role, email=email)
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
    #return Response({'message': 'User login successfully'})
    # if serializer.is_valid():
    #     # Perform login logic here (verify credentials, generate access token, etc.)
    #     # Return a success response with the access token
    #     return Response({'message': 'User logged in successfully', 'access_token': 'your_access_token'})
    # else:
    #     # Return validation error response
    #     return Response(serializer.errors, status=400)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        password = serializer.validated_data['password']

        # Check if user exists and password is correct
        user = UserRegistration.objects(name=name).first()
        if not user:
            return Response({'message': 'User not registered'})

        if user.password != password:
            return Response({'message': 'Password incorrect'})

        # Generate JWT token
        # token = jwt.encode({
        #     'name': name,
        #     'exp': datetime.utcnow() + timedelta(minutes=settings.JWT_EXPIRATION_DELTA)
        # }, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)

        # Generate JWT token
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



@api_view(['POST'])
def apply_for_exam(request):
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
            return Response({'message': 'Only students can apply for the exam'})
        # s1= user_register.private_key
        # s2= bytes.fromhex(s1)
        # sender_account= Account.from_key(s2)
        # sender_account = web3.eth.get_accounts()[i]
        global i
        sender_account = web3.eth.accounts[i]
        i = i + 1
        user_register.private_key = sender_account
        user_register.save()
        
        user = Student.objects(name=name).first()
        if not user:
            return Response({'message': 'Only students can apply for the exam'})

        # Get the list of professors' names from the request data
        professors = request.data.get('partners', [])
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
            #professor.permissions_pending.append(name)
            # prof_name = professor.name
            # prof_user = UserRegistration.objects(name=prof_name).first()
            # key1= prof_user.private_key
            # key2= bytes.fromhex(key1)
            # account1= Account.from_key(key2)
            # #teachers.append(account1.address)
            # teachers.append(account1)
            acc1 = web3.eth.accounts[i]
            i = i + 1
            teachers.append(acc1)
            prof_register = UserRegistration.objects(name=professor.name).first()
            prof_register.private_key = acc1
            prof_register.save()
            professor.save()
        # # The sender's Ethereum address
        # 'gas': 2000000,  # Adjust the gas value as needed
        # 'gasPrice': web3.toWei('50', 'gwei')  # Adjust the gas price as needed
        # transaction = contract.functions.requestApproval(teachers).transact({
        #     'from': sender_account.address})
        transaction = contract.functions.requestApproval(teachers).transact({
            'from': sender_account})
        # Wait for the transaction to be mined
        transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction)

        if transaction_receipt['status'] == 1:
            return Response({'message': 'Application for exam submitted successfully. The chain is fine!!'})
        else:
            return Response({'message': 'Application for exam NOT successfull. Trouble in the chain!!'})
        # Return the response
        #return Response({'message': 'Application for exam submitted successfully'})
    else:
        # Return validation error response
        return Response(serializer.errors, status=400)



@api_view(['POST'])
def approve_requests(request):
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
        students = request.data.get('students', [])
        if not isinstance(students, list):
            return Response({'message': 'Invalid students data format'})

        # Check if the student names exist in the database
        existing_students = Student.objects(name__in=students)
        if len(existing_students) != len(students):
            return Response({'message': 'Some students do not exist in the database'})

        # Process each student and update their 'permissions_obtained' field
        for student in existing_students:
            if name in student.partners:
                #student.partners.remove(name)  # Remove professor from student's 'partners' list
                tea1= user_register.private_key
                stu1= UserRegistration.objects(name=student.name).first()
                stu2= stu1.private_key
                transaction = contract.functions.approveRequest(stu2).transact({'from': tea1})
                transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction)
                if transaction_receipt['status'] == 1:
                    student.permissions_obtained.append(name)
                    student.save()
                    return Response({'message': 'Application for exam has been approved. The chain is fine!!'})
                    #return Response({'message': 'Application for exam has been approved. The chain is fine!!'})
                    #return Response({'message': 'Application for exam submitted successfully. The chain is fine!!'})
                else:
                    return Response({'message': 'exam request not Approved. Trouble in the chain!!'})
                # student.permissions_obtained.append(name)  # Add professor to student's 'permissions_obtained' list
                # student.save()

        # Return the response
        return Response({'message': 'Some error with processing. Check input types'})
        #return Response({'message': 'Application for exam has been approved. The chain is fine!!'})
    else:
        # Return validation error response
        return Response(serializer.errors, status=400)

@api_view(['POST'])
def check_status(request):
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
        # if not user.partners:
        #     return Response({'message': 'User has not applied for an exam'})

        # Check if all partners are present in 'permissions_obtained' field
        missing_permissions = [partner for partner in user.partners if partner not in user.permissions_obtained]
        if missing_permissions:
            return Response({'message': 'Some permissions are pending', 'missing_permissions': missing_permissions})
        else:
            return Response({'message': 'All professors approved. You can sit for the exam'})
    else:
        # Return validation error response
        return Response(serializer.errors, status=400)







###################################################################################################################
###################################################################################################################

# import jwt
# from django.shortcuts import render
# # Create your views here.
# from datetime import datetime, timedelta
# from django.conf import settings
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .serializers import UserRegistrationSerializer, UserLoginSerializer, ExamSerializer, StudentSerializer, ProfessorSerializer
# from .models import UserRegistration, UserLogin, Exam, Student, Professor
# from .models import Exam, Student, Professor, UserRegistration, UserLogin
# from ecdsa import SigningKey, SECP256k1
# #import hashlib

# ##
# ## Integrate the blockchain here. 
# from web3 import Web3
# from eth_account import Account
# ganache_url = "http://127.0.0.1:8545"
# web3 = Web3(Web3.HTTPProvider(ganache_url))
# #contract_address = "0x89E165FC0F1A78366F68bCf917f20E219296D0Df"
# #contract_address = "0x89E165FC0F1A78366F68bCf917f20E219296D0Df"
# contract_address = "0x853AE30c3a160412aE69Ef539827237DC7B510D9"
# contract_abi = [{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"student","type":"address"}],"name":"ApprovalReceived","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"student","type":"address"},{"indexed":False,"internalType":"address[]","name":"teachers","type":"address[]"}],"name":"RequestApproval","type":"event"},{"inputs":[{"internalType":"address","name":"student","type":"address"}],"name":"approveRequest","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"teachers","type":"address[]"}],"name":"requestApproval","outputs":[],"stateMutability":"nonpayable","type":"function"}]
# contract = web3.eth.contract(address=contract_address, abi=contract_abi)
# ##
# i = 0

# @api_view(['POST'])
# def register_user(request):
#     serializer = UserRegistrationSerializer(data=request.data)
#     #return Response({'message': 'User registered successfully'})
#     # if serializer.is_valid():
#     #     # Perform registration logic here (create user, generate private key, store in DB)
#     #     # use PyECDSA here to generate private keys
#     #     # Store user details in the database
#     #     # Return a success response
#     #     return Response({'message': 'User registered successfully'})
#     # else:
#     #     # Return validation error response
#     #     return Response(serializer.errors, status=400)
#     if serializer.is_valid():
#         name = serializer.validated_data['name']
#         password = serializer.validated_data['password']
#         role = serializer.validated_data['role']
#         email= serializer.validated_data['email']

#         # Check if user already exists
#         if UserRegistration.objects(name=name).first():
#             return Response({'message': 'User already exists'})

#         # Generate and store keys using your ecdsa signer code (to be added later)
#         # For now, just assume some dummy keys are generated
#         private_key = SigningKey.generate(curve=SECP256k1)
#         private_key_hex = private_key.to_string().hex()
#         # hash_object = hashlib.sha256(private_key)
#         # hash_hex = hash_object.hexdigest()
#         # Store the user details in the database
#         # user = UserRegistration(name=name, password=password, role=role, public_key=public_key, private_key=private_key)
#         # user.save()
#         user_registration = UserRegistration(name=name, password=password, role=role, private_key=private_key_hex)
#         user_registration.save()
#         if role == 'student':
#             Sttudent = Student(name=name, role= role, email=email)
#             Sttudent.save()
#         else:
#             Prrofessor = Professor(name=name, role=role, email=email)
#             Prrofessor.save()
#         # Return the response with the keys
#         return Response({'message': 'User registered successfully'})
#     else:
#         # Return validation error response
#         return Response(serializer.errors, status=400)



# @api_view(['POST'])
# def login_user(request):
#     serializer = UserLoginSerializer(data=request.data)
#     #return Response({'message': 'User login successfully'})
#     # if serializer.is_valid():
#     #     # Perform login logic here (verify credentials, generate access token, etc.)
#     #     # Return a success response with the access token
#     #     return Response({'message': 'User logged in successfully', 'access_token': 'your_access_token'})
#     # else:
#     #     # Return validation error response
#     #     return Response(serializer.errors, status=400)
#     if serializer.is_valid():
#         name = serializer.validated_data['name']
#         password = serializer.validated_data['password']

#         # Check if user exists and password is correct
#         user = UserRegistration.objects(name=name).first()
#         if not user:
#             return Response({'message': 'User not registered'})

#         if user.password != password:
#             return Response({'message': 'Password incorrect'})

#         # Generate JWT token
#         # token = jwt.encode({
#         #     'name': name,
#         #     'exp': datetime.utcnow() + timedelta(minutes=settings.JWT_EXPIRATION_DELTA)
#         # }, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)

#         # Generate JWT token
#         token = jwt.encode({
#             'name': name,
#             'exp': datetime.utcnow() + settings.JWT_EXPIRATION_DELTA
#         }, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)

#         # Update the user's token in the database
#         user_login = UserLogin.objects(name=name).first()
#         if not user_login:
#             user_login = UserLogin(name=name)
#         user_login.token = token
#         user_login.save()

#         # Return the response with the token
#         return Response({
#             'message': 'User login successfully',
#             'token': token
#         })
#     else:
#         # Return validation error response
#         return Response(serializer.errors, status=400)



# @api_view(['POST'])
# def apply_for_exam(request):
#     serializer = UserLoginSerializer(data=request.data)
#     if serializer.is_valid():
#         name = serializer.validated_data['name']
#         token = serializer.validated_data['token']

#         # Check if user exists and token is valid
#         user_login = UserLogin.objects(name=name).first()
#         if not user_login:
#             return Response({'message': 'User not registered'})

#         try:
#             decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
#             if decoded_token['name'] != name:
#                 raise jwt.DecodeError
#             if datetime.fromtimestamp(decoded_token['exp']) < datetime.utcnow():
#                 raise jwt.ExpiredSignatureError
#         except jwt.ExpiredSignatureError:
#             return Response({'message': 'Session has ended. Do a fresh login'})
#         except jwt.DecodeError:
#             return Response({'message': 'Invalid token'})

#         # Check if the user has the role 'student'
#         user_register = UserRegistration.objects(name=name).first()
#         if user_register.role == "student":
#             user = Student.objects(name=name).first()
#         else:
#             return Response({'message': 'Only students can apply for the exam'})
#         # s1= user_register.private_key
#         # s2= bytes.fromhex(s1)
#         # sender_account= Account.from_key(s2)
#         # sender_account = web3.eth.get_accounts()[i]
#         global i
#         sender_account = web3.eth.accounts[i]
#         i = i + 1
#         user_register.private_key = sender_account
#         user_register.save()
        
#         user = Student.objects(name=name).first()
#         if not user:
#             return Response({'message': 'Only students can apply for the exam'})

#         # Get the list of professors' names from the request data
#         professors = request.data.get('partners', [])
#         if not isinstance(professors, list):
#             return Response({'message': 'Invalid professors data format'})

#         # Check if the professors' names exist in the database
#         existing_professors = Professor.objects(name__in=professors)
#         if len(existing_professors) != len(professors):
#             return Response({'message': 'Some professors do not exist in the database'})

#         # Add professors to the student's 'partners' field
#         user.partners = professors
#         user.save()
#         teachers=[]
#         # Add the student's name to the professors' 'permissions_pending' field
#         for professor in existing_professors:
#             #professor.permissions_pending.append(name)
#             # prof_name = professor.name
#             # prof_user = UserRegistration.objects(name=prof_name).first()
#             # key1= prof_user.private_key
#             # key2= bytes.fromhex(key1)
#             # account1= Account.from_key(key2)
#             # #teachers.append(account1.address)
#             # teachers.append(account1)
#             acc1 = web3.eth.accounts[i]
#             i = i + 1
#             teachers.append(acc1)
#             prof_register = UserRegistration.objects(name=professor.name).first()
#             prof_register.private_key = acc1
#             prof_register.save()
#             professor.save()
#         # # The sender's Ethereum address
#         # 'gas': 2000000,  # Adjust the gas value as needed
#         # 'gasPrice': web3.toWei('50', 'gwei')  # Adjust the gas price as needed
#         # transaction = contract.functions.requestApproval(teachers).transact({
#         #     'from': sender_account.address})
#         transaction = contract.functions.requestApproval(teachers).transact({
#             'from': sender_account})
#         # Wait for the transaction to be mined
#         transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction)

#         if transaction_receipt['status'] == 1:
#             return Response({'message': 'Application for exam submitted successfully. The chain is fine!!'})
#         else:
#             return Response({'message': 'Application for exam NOT successfull. Trouble in the chain!!'})
#         # Return the response
#         #return Response({'message': 'Application for exam submitted successfully'})
#     else:
#         # Return validation error response
#         return Response(serializer.errors, status=400)



# @api_view(['POST'])
# def approve_requests(request):
#     serializer = UserLoginSerializer(data=request.data)
#     if serializer.is_valid():
#         name = serializer.validated_data['name']
#         token = serializer.validated_data['token']

#         # Check if user exists and token is valid
#         user_login = UserLogin.objects(name=name).first()
#         if not user_login:
#             return Response({'message': 'User not registered'})

#         try:
#             decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
#             if decoded_token['name'] != name:
#                 raise jwt.DecodeError
#             if datetime.fromtimestamp(decoded_token['exp']) < datetime.utcnow():
#                 raise jwt.ExpiredSignatureError
#         except jwt.ExpiredSignatureError:
#             return Response({'message': 'Session has ended. Do a fresh login'})
#         except jwt.DecodeError:
#             return Response({'message': 'Invalid token'})

#         # Check if the user has the role 'professor'
#         user = Professor.objects(name=name).first()
#         if not user:
#             return Response({'message': 'Only professors can approve requests for exams'})

#         # Check if the user has the role 'professor'
#         user_register = UserRegistration.objects(name=name).first()
#         if user_register.role == "professor":
#             user = Professor.objects(name=name).first()
#         else:
#             return Response({'message': 'Only professors are allowed'})

#         # Get the list of student names from the request data
#         students = request.data.get('students', [])
#         if not isinstance(students, list):
#             return Response({'message': 'Invalid students data format'})

#         # Check if the student names exist in the database
#         existing_students = Student.objects(name__in=students)
#         if len(existing_students) != len(students):
#             return Response({'message': 'Some students do not exist in the database'})

#         # Process each student and update their 'permissions_obtained' field
#         for student in existing_students:
#             if name in student.partners:
#                 #student.partners.remove(name)  # Remove professor from student's 'partners' list
#                 tea1= user_register.private_key
#                 stu1= UserRegistration.objects(name=student.name).first()
#                 stu2= stu1.private_key
#                 transaction = contract.functions.approveRequest(stu2).transact({'from': tea1})
#                 transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction)
#                 if transaction_receipt['status'] == 1:
#                     student.permissions_obtained.append(name)
#                     student.save()
#                     return Response({'message': 'Application for exam has been approved. The chain is fine!!'})
#                     #return Response({'message': 'Application for exam has been approved. The chain is fine!!'})
#                     #return Response({'message': 'Application for exam submitted successfully. The chain is fine!!'})
#                 else:
#                     return Response({'message': 'exam request not Approved. Trouble in the chain!!'})
#                 # student.permissions_obtained.append(name)  # Add professor to student's 'permissions_obtained' list
#                 # student.save()

#         # Return the response
#         return Response({'message': 'Some error with processing. Check input types'})
#         #return Response({'message': 'Application for exam has been approved. The chain is fine!!'})
#     else:
#         # Return validation error response
#         return Response(serializer.errors, status=400)

# @api_view(['POST'])
# def check_status(request):
#     serializer = UserLoginSerializer(data=request.data)
#     if serializer.is_valid():
#         name = serializer.validated_data['name']
#         token = serializer.validated_data['token']

#         # Check if user exists and token is valid
#         user_login = UserLogin.objects(name=name).first()
#         if not user_login:
#             return Response({'message': 'User not registered'})

#         try:
#             decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
#             if decoded_token['name'] != name:
#                 raise jwt.DecodeError
#             if datetime.fromtimestamp(decoded_token['exp']) < datetime.utcnow():
#                 raise jwt.ExpiredSignatureError
#         except jwt.ExpiredSignatureError:
#             return Response({'message': 'Session has ended. Do a fresh login'})
#         except jwt.DecodeError:
#             return Response({'message': 'Invalid token'})

#         # Check if the user has the role 'student'
#         user = Student.objects(name=name).first()
#         if not user:
#             return Response({'message': 'Only students can check status for the applied exam'})

#         # Check if 'partners' field is blank
#         # if not user.partners:
#         #     return Response({'message': 'User has not applied for an exam'})

#         # Check if all partners are present in 'permissions_obtained' field
#         missing_permissions = [partner for partner in user.partners if partner not in user.permissions_obtained]
#         if missing_permissions:
#             return Response({'message': 'Some permissions are pending', 'missing_permissions': missing_permissions})
#         else:
#             return Response({'message': 'All professors approved. You can sit for the exam'})
#     else:
#         # Return validation error response
#         return Response(serializer.errors, status=400)