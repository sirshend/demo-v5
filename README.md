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

in exam_approval_backend with virtualenv on, use
python manage.py migrate
python manage.py runserver


########################################

 ########### Local testing of the APIs
 ## Student 
register 
{
    "name": "stu1114" ,
    "role": "student" ,
    "password": "12345",
    "email": "stu1114@gmail.com"
}
login
{
    "name":  "stu1114",
    "password": "12345"
}

{
    "message": "User login successfully",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoic3R1MTExNCIsImV4cCI6MTY5NDUwMzUyNH0.kE8fJfmzsBDiPjkY5oTJB7ntapxMbs8oX8YwcZSarfA"
}

{
    "name": "stu1114",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoic3R1MTExNCIsImV4cCI6MTY5NDUwMzUyNH0.kE8fJfmzsBDiPjkY5oTJB7ntapxMbs8oX8YwcZSarfA",
    "course-prof": ["prof1114"]
}
{
    "name": "stu1114",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoic3R1MTExNCIsImV4cCI6MTY5NDUwMzUyNH0.kE8fJfmzsBDiPjkY5oTJB7ntapxMbs8oX8YwcZSarfA",
    "partners": ["prof1114"]
}
 ## Teacher

 teacher 1

register 
{
    "name": "prof1114" ,
    "role": "professor" ,
    "password": "12345",
    "email": "prof1114@gmail.com"
}
login
{
    "name":  "prof1114",
    "password": "12345"
}
{
    "message": "User login successfully",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjExMTQiLCJleHAiOjE2OTQ1MDM1MDB9.yIBZrdlC0qDEOAE--4XqhxJls4WDkuo8oLoYd_297Mo"
}

{
    "name": "prof1114",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjExMTQiLCJleHAiOjE2OTQ1MDM1MDB9.yIBZrdlC0qDEOAE--4XqhxJls4WDkuo8oLoYd_297Mo",
    "students": ["stu1114"]
}

{
    "name": "prof1114",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjExMTQiLCJleHAiOjE2OTQ1MDM1MDB9.yIBZrdlC0qDEOAE--4XqhxJls4WDkuo8oLoYd_297Mo",
    "students": ["stu1114"],
    "grade": "A"
}
{
    "name": "prof1114",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjExMTQiLCJleHAiOjE2OTQ1MDM1MDB9.yIBZrdlC0qDEOAE--4XqhxJls4WDkuo8oLoYd_297Mo",
    "students": ["stu1114"],
    "extra_thesis_advisor":"prof1115"
}
 teacher 2

 register 
{
    "name": "prof1115" ,
    "role": "professor" ,
    "password": "12345",
    "email": "prof1115@gmail.com"
}
 login
{
    "name":  "prof1115",
    "password": "12345"
}
{
    "message": "User login successfully",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjExMTUiLCJleHAiOjE2OTQ1MDM0NzJ9.l0MUxHf6TZkjC6jIv3X4z65JGK2ZHHmK-TkUpwxCmsM"
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



