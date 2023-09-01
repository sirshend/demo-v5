In each of shells, first do
cd .. (go to the previous level ```exam_blockchains``` for activating the virtual env)
source v1/bin/activate
cd exam_approval_backend
Once all work is done, deactivate the virtual-env with ```deactivate```


sudo mongod --dbpath .
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
mysql.server stop

in exam_approval_backend with virtualenv on, use
python manage.py migrate
python manage.py runserver


########################################

exam_approval_backend git:(main) mysql.server start
Starting MySQL
 SUCCESS!
➜  exam_approval_backend git:(main) sudo brew services start mysql
Password:
Warning: Taking root:admin ownership of some mysql paths:
  /usr/local/Cellar/mysql/8.0.33_3/bin
  /usr/local/Cellar/mysql/8.0.33_3/bin/mysqld_safe
  /usr/local/opt/mysql
  /usr/local/opt/mysql/bin
  /usr/local/var/homebrew/linked/mysql
This will require manual removal of these paths using `sudo rm` on
brew upgrade/reinstall/uninstall.
Warning: mysql must be run as non-root to start at user login!
==> Successfully started `mysql` (label: homebrew.mxcl.mysql)
➜  exam_approval_backend git:(main) mysql -u root -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 8.0.33 Homebrew

Copyright (c) 2000, 2023, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
#####################################
z1
{
    "name": "stu1" ,
    "role": "student" ,
    "password": "12345",
    "email": "stu1@gmail.com"
}
{
    "message": "User registered successfully",
    "private_key": "96314b41e51561690f4f3a6f812f3bf18b69ed565a8614f2aabefec9c7af0183"
}
{
    "name":  "stu1",
    "password": "12345"
}
{
    "message": "User login successfully",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoic3R1MSIsImV4cCI6MTY5MzcyNjM5Mn0.Ehk59oU1Oo6ESkU74ChkoagOjh50INJCD3FTgtmJ6-c"
}
{
    "name": "stu1",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoic3R1MSIsImV4cCI6MTY5MzcyNjM5Mn0.Ehk59oU1Oo6ESkU74ChkoagOjh50INJCD3FTgtmJ6-c",
    "partners": ["prof1", "prof2"]
}

{
    "name": "stu1",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoic3R1MSIsImV4cCI6MTY5MzcyNjM5Mn0.Ehk59oU1Oo6ESkU74ChkoagOjh50INJCD3FTgtmJ6-c"
}
######################################
z2
{
    "name": "prof1" ,
    "role": "professor" ,
    "password": "12345",
    "email": "prof1@gmail.com"
}
{
    "message": "User registered successfully",
    "private_key": "eea011f28b5ee3011f3e1482844663889300191ea88973299a61d7db7f2e161f"
}
{
    "name":  "prof1",
    "password": "12345"
}
{
    "message": "User login successfully",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjEiLCJleHAiOjE2OTM3MjY1Mjl9.z8z4lA_qB73Q6heDRVQMlF_vEugqNZVfencwKGfJbLg"
}

{
    "name": "prof1",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjEiLCJleHAiOjE2OTM3MjY1Mjl9.z8z4lA_qB73Q6heDRVQMlF_vEugqNZVfencwKGfJbLg",
    "students": ["stu1"]
}


######################################
z3
{
    "name": "prof2" ,
    "role": "professor" ,
    "password": "12345",
    "email": "prof2@gmail.com"
}
{
    "message": "User registered successfully",
    "private_key": "137e979ad121dc95154755fd5da6b2c46ca9fea53f30b030c7a958e817003b94"
}
{
    "name":  "prof2",
    "password": "12345"
}
{
    "message": "User login successfully",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjIiLCJleHAiOjE2OTM3MjY2MDB9.o3JRW7mdMGk3l7OAplo0mCpQmDyLzuVz5nvdx7EAJi4"
}
{
    "name": "prof2",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicHJvZjIiLCJleHAiOjE2OTM3MjY2MDB9.o3JRW7mdMGk3l7OAplo0mCpQmDyLzuVz5nvdx7EAJi4",
    "students": ["stu1"]
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



###############################################################################
###############################################################################
In each of shells, first do
cd .. (go to the previous level ```exam_blockchains``` for activating the virtual env)
source v1/bin/activate
cd exam_approval_backend
Once all work is done, deactivate the virtual-env with ```deactivate```


sudo mongod --dbpath .
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
mysql.server stop

in exam_approval_backend with virtualenv on, use
python manage.py migrate
python manage.py runserver


########################################

echo "# backend-demo-v2" >> README.md
git init
( we are assuming that you have a functional readme already and the project is non-empty.)
git add .
git commit -m "first commit"
git branch -M main
( Replace with your own URL.. or github repository URL )
git remote add origin https://github.com/sirshend/backend-demo-v2.git
git push -u origin main

########################################

exam_approval_backend git:(main) mysql.server start
Starting MySQL
 SUCCESS!
➜  exam_approval_backend git:(main) sudo brew services start mysql
Password:
Warning: Taking root:admin ownership of some mysql paths:
  /usr/local/Cellar/mysql/8.0.33_3/bin
  /usr/local/Cellar/mysql/8.0.33_3/bin/mysqld_safe
  /usr/local/opt/mysql
  /usr/local/opt/mysql/bin
  /usr/local/var/homebrew/linked/mysql
This will require manual removal of these paths using `sudo rm` on
brew upgrade/reinstall/uninstall.
Warning: mysql must be run as non-root to start at user login!
==> Successfully started `mysql` (label: homebrew.mxcl.mysql)
➜  exam_approval_backend git:(main) mysql -u root -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 8.0.33 Homebrew

Copyright (c) 2000, 2023, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.


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



contract-v2 git:(main) ✗ truffle console
truffle(development)> let instance = await School.deployed()
undefined
truffle(development)>  print(instance)
Uncaught ReferenceError: print is not defined
truffle(development)> instance
TruffleContract {
  constructor: [Function: TruffleContract] {
    _constructorMethods: {
      configureNetwork: [Function: configureNetwork],
      setProvider: [Function: setProvider],
      new: [Function: new],
      at: [AsyncFunction: at],
      deployed: [AsyncFunction: deployed],
      defaults: [Function: defaults],
      hasNetwork: [Function: hasNetwork],
      isDeployed: [Function: isDeployed],
      detectNetwork: [AsyncFunction: detectNetwork],
      setNetwork: [Function: setNetwork],
      setNetworkType: [Function: setNetworkType],
      setWallet: [Function: setWallet],
      resetAddress: [Function: resetAddress],
      link: [Function: link],
      clone: [Function: clone],
      addProp: [Function: addProp],
      toJSON: [Function: toJSON],
      decodeLogs: [Function: decodeLogs]
    },
    _properties: {
      contract_name: [Object],
      contractName: [Object],
      gasMultiplier: [Object],
      timeoutBlocks: [Object],
      autoGas: [Object],
      numberFormat: [Object],
      abi: [Object],
      metadata: [Function: metadata],
      network: [Function: network],
      networks: [Function: networks],
      address: [Object],
      transactionHash: [Object],
      links: [Function: links],
      events: [Function: events],
      binary: [Function: binary],
      deployedBinary: [Function: deployedBinary],
      unlinked_binary: [Object],
      bytecode: [Object],
      deployedBytecode: [Object],
      sourceMap: [Object],
      deployedSourceMap: [Object],
      source: [Object],
      sourcePath: [Object],
      legacyAST: [Object],
      ast: [Object],
      compiler: [Object],
      schema_version: [Function: schema_version],
      schemaVersion: [Function: schemaVersion],
      updated_at: [Function: updated_at],
      updatedAt: [Function: updatedAt],
      userdoc: [Function: userdoc],
      devdoc: [Function: devdoc],
      networkType: [Object],
      immutableReferences: [Object],
      generatedSources: [Object],
      deployedGeneratedSources: [Object],
      db: [Object]
    },
    _property_values: {},
    _json: {
      contractName: 'School',
      abi: [Array],
      metadata: '{"compiler":{"version":"0.8.20+commit.a1b79de6"},"language":"Solidity","output":{"abi":[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"student","type":"address"}],"name":"ApprovalReceived","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"student","type":"address"},{"indexed":false,"internalType":"address[]","name":"teachers","type":"address[]"}],"name":"RequestApproval","type":"event"},{"inputs":[{"internalType":"address","name":"student","type":"address"}],"name":"approveRequest","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"teachers","type":"address[]"}],"name":"requestApproval","outputs":[],"stateMutability":"nonpayable","type":"function"}],"devdoc":{"kind":"dev","methods":{},"version":1},"userdoc":{"kind":"user","methods":{},"version":1}},"settings":{"compilationTarget":{"project:/contracts/School.sol":"School"},"evmVersion":"shanghai","libraries":{},"metadata":{"bytecodeHash":"ipfs"},"optimizer":{"enabled":false,"runs":200},"remappings":[]},"sources":{"project:/contracts/School.sol":{"keccak256":"0x38c04a09f6c1e92ae302a2754246b4b8c9185bd39df7eacda3a7fa5a12062c04","license":"MIT","urls":["bzz-raw://0127bd7c8f847a3a193a07fffc4b6c59ce8cc03d025a8a2fdfd4088e9a96ddf3","dweb:/ipfs/QmatoE1Eb3h5TknExkRwF3FjTLWMGJ1J1X76vga9EjhmPD"]}},"version":1}',
      bytecode: '0x608060405234801561000f575f80fd5b506108ff8061001d5f395ff3fe608060405234801561000f575f80fd5b5060043610610034575f3560e01c8063061dff9a14610038578063e31c75c314610054575b5f80fd5b610052600480360381019061004d9190610564565b610070565b005b61006e600480360381019061006991906105f0565b610231565b005b5f805f8373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f2090506100b981336102d8565b6100f8576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016100ef906106bb565b60405180910390fd5b806001015f3373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f205f9054906101000a900460ff1615610184576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161017b90610723565b60405180910390fd5b6001816001015f3373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f205f6101000a81548160ff0219169083151502179055506101e481610383565b1561022d578173ffffffffffffffffffffffffffffffffffffffff167f135b662e7c460f01a8962dabbc952859694282ca1f1bfbacf24ebecc00160d3560405160405180910390a25b5050565b5f805f3373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f2090508282825f01919061028292919061044a565b503373ffffffffffffffffffffffffffffffffffffffff167f57eebaf6a4a7bdcd3e1a60dd32681c63d968f8935f596ee7a4523e5fa6c36db684846040516102cb9291906107fd565b60405180910390a2505050565b5f805f90505b835f0180549050811015610378578273ffffffffffffffffffffffffffffffffffffffff16845f0182815481106103185761031761081f565b5b905f5260205f20015f9054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff160361036557600191505061037d565b808061037090610882565b9150506102de565b505f90505b92915050565b5f805f90505b825f018054905081101561043f57826001015f845f0183815481106103b1576103b061081f565b5b905f5260205f20015f9054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f205f9054906101000a900460ff1661042c575f915050610445565b808061043790610882565b915050610389565b50600190505b919050565b828054828255905f5260205f209081019282156104d6579160200282015b828111156104d557823573ffffffffffffffffffffffffffffffffffffffff16825f6101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555091602001919060010190610468565b5b5090506104e391906104e7565b5090565b5b808211156104fe575f815f9055506001016104e8565b5090565b5f80fd5b5f80fd5b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f6105338261050a565b9050919050565b61054381610529565b811461054d575f80fd5b50565b5f8135905061055e8161053a565b92915050565b5f6020828403121561057957610578610502565b5b5f61058684828501610550565b91505092915050565b5f80fd5b5f80fd5b5f80fd5b5f8083601f8401126105b0576105af61058f565b5b8235905067ffffffffffffffff8111156105cd576105cc610593565b5b6020830191508360208202830111156105e9576105e8610597565b5b9250929050565b5f806020838503121561060657610605610502565b5b5f83013567ffffffffffffffff81111561062357610622610506565b5b61062f8582860161059b565b92509250509250929050565b5f82825260208201905092915050565b7f4f6e6c792072657175657374656420746561636865722063616e20617070726f5f8201527f76652e0000000000000000000000000000000000000000000000000000000000602082015250565b5f6106a560238361063b565b91506106b08261064b565b604082019050919050565b5f6020820190508181035f8301526106d281610699565b9050919050565b7f546561636865722068617320616c726561647920617070726f7665642e0000005f82015250565b5f61070d601d8361063b565b9150610718826106d9565b602082019050919050565b5f6020820190508181035f83015261073a81610701565b9050919050565b5f82825260208201905092915050565b5f819050919050565b61076381610529565b82525050565b5f610774838361075a565b60208301905092915050565b5f61078e6020840184610550565b905092915050565b5f602082019050919050565b5f6107ad8385610741565b93506107b882610751565b805f5b858110156107f0576107cd8284610780565b6107d78882610769565b97506107e283610796565b9250506001810190506107bb565b5085925050509392505050565b5f6020820190508181035f8301526108168184866107a2565b90509392505050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52603260045260245ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52601160045260245ffd5b5f819050919050565b5f61088c82610879565b91507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff82036108be576108bd61084c565b5b60018201905091905056fea2646970667358221220da91eca7d25aca236ca648e21c9d8f2b9106466bafd868836b201ddfe44a007e64736f6c63430008140033',
      deployedBytecode: '0x608060405234801561000f575f80fd5b5060043610610034575f3560e01c8063061dff9a14610038578063e31c75c314610054575b5f80fd5b610052600480360381019061004d9190610564565b610070565b005b61006e600480360381019061006991906105f0565b610231565b005b5f805f8373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f2090506100b981336102d8565b6100f8576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016100ef906106bb565b60405180910390fd5b806001015f3373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f205f9054906101000a900460ff1615610184576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161017b90610723565b60405180910390fd5b6001816001015f3373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f205f6101000a81548160ff0219169083151502179055506101e481610383565b1561022d578173ffffffffffffffffffffffffffffffffffffffff167f135b662e7c460f01a8962dabbc952859694282ca1f1bfbacf24ebecc00160d3560405160405180910390a25b5050565b5f805f3373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f2090508282825f01919061028292919061044a565b503373ffffffffffffffffffffffffffffffffffffffff167f57eebaf6a4a7bdcd3e1a60dd32681c63d968f8935f596ee7a4523e5fa6c36db684846040516102cb9291906107fd565b60405180910390a2505050565b5f805f90505b835f0180549050811015610378578273ffffffffffffffffffffffffffffffffffffffff16845f0182815481106103185761031761081f565b5b905f5260205f20015f9054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff160361036557600191505061037d565b808061037090610882565b9150506102de565b505f90505b92915050565b5f805f90505b825f018054905081101561043f57826001015f845f0183815481106103b1576103b061081f565b5b905f5260205f20015f9054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f205f9054906101000a900460ff1661042c575f915050610445565b808061043790610882565b915050610389565b50600190505b919050565b828054828255905f5260205f209081019282156104d6579160200282015b828111156104d557823573ffffffffffffffffffffffffffffffffffffffff16825f6101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555091602001919060010190610468565b5b5090506104e391906104e7565b5090565b5b808211156104fe575f815f9055506001016104e8565b5090565b5f80fd5b5f80fd5b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f6105338261050a565b9050919050565b61054381610529565b811461054d575f80fd5b50565b5f8135905061055e8161053a565b92915050565b5f6020828403121561057957610578610502565b5b5f61058684828501610550565b91505092915050565b5f80fd5b5f80fd5b5f80fd5b5f8083601f8401126105b0576105af61058f565b5b8235905067ffffffffffffffff8111156105cd576105cc610593565b5b6020830191508360208202830111156105e9576105e8610597565b5b9250929050565b5f806020838503121561060657610605610502565b5b5f83013567ffffffffffffffff81111561062357610622610506565b5b61062f8582860161059b565b92509250509250929050565b5f82825260208201905092915050565b7f4f6e6c792072657175657374656420746561636865722063616e20617070726f5f8201527f76652e0000000000000000000000000000000000000000000000000000000000602082015250565b5f6106a560238361063b565b91506106b08261064b565b604082019050919050565b5f6020820190508181035f8301526106d281610699565b9050919050565b7f546561636865722068617320616c726561647920617070726f7665642e0000005f82015250565b5f61070d601d8361063b565b9150610718826106d9565b602082019050919050565b5f6020820190508181035f83015261073a81610701565b9050919050565b5f82825260208201905092915050565b5f819050919050565b61076381610529565b82525050565b5f610774838361075a565b60208301905092915050565b5f61078e6020840184610550565b905092915050565b5f602082019050919050565b5f6107ad8385610741565b93506107b882610751565b805f5b858110156107f0576107cd8284610780565b6107d78882610769565b97506107e283610796565b9250506001810190506107bb565b5085925050509392505050565b5f6020820190508181035f8301526108168184866107a2565b90509392505050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52603260045260245ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52601160045260245ffd5b5f819050919050565b5f61088c82610879565b91507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff82036108be576108bd61084c565b5b60018201905091905056fea2646970667358221220da91eca7d25aca236ca648e21c9d8f2b9106466bafd868836b201ddfe44a007e64736f6c63430008140033',
      immutableReferences: {},
      generatedSources: [],
      deployedGeneratedSources: [Array],
      sourceMap: '57:1512:0:-:0;;;;;;;;;;;;;;;;;;;',
      deployedSourceMap: '57:1512:0:-:0;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;588:416;;;;;;;;;;;;;:::i;:::-;;:::i;:::-;;361:221;;;;;;;;;;;;;:::i;:::-;;:::i;:::-;;588:416;648:23;674:8;:17;683:7;674:17;;;;;;;;;;;;;;;648:43;;709:30;719:7;728:10;709:9;:30::i;:::-;701:78;;;;;;;;;;;;:::i;:::-;;;;;;;;;798:7;:17;;:29;816:10;798:29;;;;;;;;;;;;;;;;;;;;;;;;;797:30;789:72;;;;;;;;;;;;:::i;:::-;;;;;;;;;904:4;872:7;:17;;:29;890:10;872:29;;;;;;;;;;;;;;;;:36;;;;;;;;;;;;;;;;;;922:19;933:7;922:10;:19::i;:::-;919:79;;;979:7;962:25;;;;;;;;;;;;919:79;638:366;588:416;:::o;361:221::-;434:26;463:8;:20;472:10;463:20;;;;;;;;;;;;;;;434:49;;515:8;;493:10;:19;;:30;;;;;;;:::i;:::-;;554:10;538:37;;;566:8;;538:37;;;;;;;:::i;:::-;;;;;;;;424:158;361:221;;:::o;1010:279::-;1092:4;1112:6;1121:1;1112:10;;1108:153;1128:7;:16;;:23;;;;1124:1;:27;1108:153;;;1198:7;1175:30;;:7;:16;;1192:1;1175:19;;;;;;;;:::i;:::-;;;;;;;;;;;;;;;;;;;:30;;;1172:79;;1232:4;1225:11;;;;;1172:79;1153:3;;;;;:::i;:::-;;;;1108:153;;;;1277:5;1270:12;;1010:279;;;;;:::o;1295:272::-;1361:4;1381:6;1390:1;1381:10;;1377:163;1397:7;:16;;:23;;;;1393:1;:27;1377:163;;;1445:7;:17;;:38;1463:7;:16;;1480:1;1463:19;;;;;;;;:::i;:::-;;;;;;;;;;;;;;;;;;;1445:38;;;;;;;;;;;;;;;;;;;;;;;;;1441:89;;1510:5;1503:12;;;;;1441:89;1422:3;;;;;:::i;:::-;;;;1377:163;;;;1556:4;1549:11;;1295:272;;;;:::o;-1:-1:-1:-;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:::i;:::-;;;:::o;:::-;;;;;;;;;;;;;;;;;;;;;:::o;88:117:1:-;197:1;194;187:12;211:117;320:1;317;310:12;334:126;371:7;411:42;404:5;400:54;389:65;;334:126;;;:::o;466:96::-;503:7;532:24;550:5;532:24;:::i;:::-;521:35;;466:96;;;:::o;568:122::-;641:24;659:5;641:24;:::i;:::-;634:5;631:35;621:63;;680:1;677;670:12;621:63;568:122;:::o;696:139::-;742:5;780:6;767:20;758:29;;796:33;823:5;796:33;:::i;:::-;696:139;;;;:::o;841:329::-;900:6;949:2;937:9;928:7;924:23;920:32;917:119;;;955:79;;:::i;:::-;917:119;1075:1;1100:53;1145:7;1136:6;1125:9;1121:22;1100:53;:::i;:::-;1090:63;;1046:117;841:329;;;;:::o;1176:117::-;1285:1;1282;1275:12;1299:117;1408:1;1405;1398:12;1422:117;1531:1;1528;1521:12;1562:568;1635:8;1645:6;1695:3;1688:4;1680:6;1676:17;1672:27;1662:122;;1703:79;;:::i;:::-;1662:122;1816:6;1803:20;1793:30;;1846:18;1838:6;1835:30;1832:117;;;1868:79;;:::i;:::-;1832:117;1982:4;1974:6;1970:17;1958:29;;2036:3;2028:4;2020:6;2016:17;2006:8;2002:32;1999:41;1996:128;;;2043:79;;:::i;:::-;1996:128;1562:568;;;;;:::o;2136:559::-;2222:6;2230;2279:2;2267:9;2258:7;2254:23;2250:32;2247:119;;;2285:79;;:::i;:::-;2247:119;2433:1;2422:9;2418:17;2405:31;2463:18;2455:6;2452:30;2449:117;;;2485:79;;:::i;:::-;2449:117;2598:80;2670:7;2661:6;2650:9;2646:22;2598:80;:::i;:::-;2580:98;;;;2376:312;2136:559;;;;;:::o;2701:169::-;2785:11;2819:6;2814:3;2807:19;2859:4;2854:3;2850:14;2835:29;;2701:169;;;;:::o;2876:222::-;3016:34;3012:1;3004:6;3000:14;2993:58;3085:5;3080:2;3072:6;3068:15;3061:30;2876:222;:::o;3104:366::-;3246:3;3267:67;3331:2;3326:3;3267:67;:::i;:::-;3260:74;;3343:93;3432:3;3343:93;:::i;:::-;3461:2;3456:3;3452:12;3445:19;;3104:366;;;:::o;3476:419::-;3642:4;3680:2;3669:9;3665:18;3657:26;;3729:9;3723:4;3719:20;3715:1;3704:9;3700:17;3693:47;3757:131;3883:4;3757:131;:::i;:::-;3749:139;;3476:419;;;:::o;3901:179::-;4041:31;4037:1;4029:6;4025:14;4018:55;3901:179;:::o;4086:366::-;4228:3;4249:67;4313:2;4308:3;4249:67;:::i;:::-;4242:74;;4325:93;4414:3;4325:93;:::i;:::-;4443:2;4438:3;4434:12;4427:19;;4086:366;;;:::o;4458:419::-;4624:4;4662:2;4651:9;4647:18;4639:26;;4711:9;4705:4;4701:20;4697:1;4686:9;4682:17;4675:47;4739:131;4865:4;4739:131;:::i;:::-;4731:139;;4458:419;;;:::o;4883:184::-;4982:11;5016:6;5011:3;5004:19;5056:4;5051:3;5047:14;5032:29;;4883:184;;;;:::o;5073:102::-;5142:4;5165:3;5157:11;;5073:102;;;:::o;5181:108::-;5258:24;5276:5;5258:24;:::i;:::-;5253:3;5246:37;5181:108;;:::o;5295:179::-;5364:10;5385:46;5427:3;5419:6;5385:46;:::i;:::-;5463:4;5458:3;5454:14;5440:28;;5295:179;;;;:::o;5480:122::-;5532:5;5557:39;5592:2;5587:3;5583:12;5578:3;5557:39;:::i;:::-;5548:48;;5480:122;;;;:::o;5608:115::-;5680:4;5712;5707:3;5703:14;5695:22;;5608:115;;;:::o;5759:699::-;5888:3;5911:86;5990:6;5985:3;5911:86;:::i;:::-;5904:93;;6021:58;6073:5;6021:58;:::i;:::-;6102:7;6133:1;6118:315;6143:6;6140:1;6137:13;6118:315;;;6213:42;6248:6;6239:7;6213:42;:::i;:::-;6275:63;6334:3;6319:13;6275:63;:::i;:::-;6268:70;;6361:62;6416:6;6361:62;:::i;:::-;6351:72;;6178:255;6165:1;6162;6158:9;6153:14;;6118:315;;;6122:14;6449:3;6442:10;;5893:565;;5759:699;;;;;:::o;6464:393::-;6617:4;6655:2;6644:9;6640:18;6632:26;;6704:9;6698:4;6694:20;6690:1;6679:9;6675:17;6668:47;6732:118;6845:4;6836:6;6828;6732:118;:::i;:::-;6724:126;;6464:393;;;;;:::o;6863:180::-;6911:77;6908:1;6901:88;7008:4;7005:1;6998:15;7032:4;7029:1;7022:15;7049:180;7097:77;7094:1;7087:88;7194:4;7191:1;7184:15;7218:4;7215:1;7208:15;7235:77;7272:7;7301:5;7290:16;;7235:77;;;:::o;7318:233::-;7357:3;7380:24;7398:5;7380:24;:::i;:::-;7371:33;;7426:66;7419:5;7416:77;7413:103;;7496:18;;:::i;:::-;7413:103;7543:1;7536:5;7532:13;7525:20;;7318:233;;;:::o',
      source: '// SPDX-License-Identifier: MIT\n' +
        'pragma solidity ^0.8.0;\n' +
        '\n' +
        'contract School {\n' +
        '    event RequestApproval(address indexed student, address[] teachers);\n' +
        '    event ApprovalReceived(address indexed student);\n' +
        '\n' +
        '    struct Request {\n' +
        '        address[] teachers;\n' +
        '        mapping(address => bool) approvals;\n' +
        '    } \n' +
        '    \n' +
        '    mapping(address => Request) private requests;\n' +
        '\n' +
        '    function requestApproval(address[] calldata teachers) external {\n' +
        '        Request storage newRequest = requests[msg.sender];\n' +
        '        newRequest.teachers = teachers;\n' +
        '        emit RequestApproval(msg.sender, teachers);\n' +
        '    }\n' +
        '\n' +
        '    function approveRequest(address student) external {\n' +
        '        Request storage request = requests[student];\n' +
        '        require(isTeacher(request, msg.sender), "Only requested teacher can approve.");\n' +
        '        require(!request.approvals[msg.sender], "Teacher has already approved.");\n' +
        '\n' +
        '        request.approvals[msg.sender] = true;\n' +
        '\n' +
        '        if(isApproved(request)) {\n' +
        '            emit ApprovalReceived(student);\n' +
        '        }\n' +
        '    }\n' +
        '\n' +
        '    function isTeacher(Request storage request, address teacher) private view returns(bool) {\n' +
        '        for(uint i = 0; i < request.teachers.length; i++) {\n' +
        '            if(request.teachers[i] == teacher) {\n' +
        '                return true;\n' +
        '            }\n' +
        '        }\n' +
        '        return false;\n' +
        '    }\n' +
        '\n' +
        '    function isApproved(Request storage request) private view returns(bool) {\n' +
        '        for(uint i = 0; i < request.teachers.length; i++) {\n' +
        '            if(!request.approvals[request.teachers[i]]) {\n' +
        '                return false;\n' +
        '            }\n' +
        '        }\n' +
        '        return true;\n' +
        '    }\n' +
        '}\n',
      sourcePath: '/Users/sirshendu/codes/contract-v2/contracts/School.sol',
      ast: [Object],
      legacyAST: undefined,
      compiler: [Object],
      networks: [Object],
      schemaVersion: '3.4.14',
      updatedAt: '2023-08-18T08:03:48.723Z',
      networkType: 'ethereum',
      devdoc: [Object],
      userdoc: [Object],
      db: undefined
    },
    configureNetwork: [Function: bound configureNetwork],
    setProvider: [Function: bound setProvider],
    new: [Function: bound new] {
      estimateGas: [Function: bound estimateDeployment],
      request: [Function: bound requestDeployment]
    },
    at: [Function: bound at] AsyncFunction,
    deployed: [Function: bound deployed] AsyncFunction,
    defaults: [Function: bound defaults],
    hasNetwork: [Function: bound hasNetwork],
    isDeployed: [Function: bound isDeployed],
    detectNetwork: [Function: bound detectNetwork] AsyncFunction,
    setNetwork: [Function: bound setNetwork],
    setNetworkType: [Function: bound setNetworkType],
    setWallet: [Function: bound setWallet],
    resetAddress: [Function: bound resetAddress],
    link: [Function: bound link],
    clone: [Function: bound clone],
    addProp: [Function: bound addProp],
    toJSON: [Function: bound toJSON],
    decodeLogs: [Function: bound decodeLogs],
    enums: {},
    class_defaults: { from: '0xF0EcE28B1FA3f9779a09c3E1b418ECB8565b5962' },
    interfaceAdapter: Web3InterfaceAdapter { web3: [Web3Shim] },
    web3: Web3Shim {
      currentProvider: [Getter/Setter],
      _requestManager: [RequestManager],
      givenProvider: null,
      providers: [Object],
      _provider: [HttpProvider],
      setProvider: [Function (anonymous)],
      setRequestManager: [Function (anonymous)],
      BatchRequest: [Function: bound Batch],
      extend: [Function],
      version: '1.10.0',
      utils: [Object],
      eth: [Eth],
      shh: [Shh],
      bzz: [Bzz],
      networkType: 'ethereum'
    },
    currentProvider: HttpProvider {
      withCredentials: undefined,
      timeout: 0,
      headers: undefined,
      agent: undefined,
      connected: false,
      host: 'http://127.0.0.1:8545',
      httpAgent: [Agent],
      send: [Function (anonymous)],
      request: [Function: bound modifiedRequest] AsyncFunction,
      _alreadyWrapped: true
    },
    network_id: '1692260164118',
    disableConfirmationListener: undefined,
    ens: { enabled: false, registryAddress: undefined }
  },
  methods: {
    'requestApproval(address[])': [Function (anonymous)] {
      call: [Function (anonymous)],
      sendTransaction: [Function (anonymous)],
      estimateGas: [Function (anonymous)],
      request: [Function (anonymous)]
    },
    'approveRequest(address)': [Function (anonymous)] {
      call: [Function (anonymous)],
      sendTransaction: [Function (anonymous)],
      estimateGas: [Function (anonymous)],
      request: [Function (anonymous)]
    }
  },
  abi: [
    {
      anonymous: false,
      inputs: [Array],
      name: 'ApprovalReceived',
      type: 'event',
      constant: undefined,
      payable: undefined,
      signature: '0x135b662e7c460f01a8962dabbc952859694282ca1f1bfbacf24ebecc00160d35'
    },
    {
      anonymous: false,
      inputs: [Array],
      name: 'RequestApproval',
      type: 'event',
      constant: undefined,
      payable: undefined,
      signature: '0x57eebaf6a4a7bdcd3e1a60dd32681c63d968f8935f596ee7a4523e5fa6c36db6'
    },
    {
      inputs: [Array],
      name: 'requestApproval',
      outputs: [],
      stateMutability: 'nonpayable',
      type: 'function',
      constant: undefined,
      payable: undefined,
      signature: '0xe31c75c3'
    },
    {
      inputs: [Array],
      name: 'approveRequest',
      outputs: [],
      stateMutability: 'nonpayable',
      type: 'function',
      constant: undefined,
      payable: undefined,
      signature: '0x061dff9a'
    }
  ],
  address: '0x97717A1fd7403a0fA71a3aA6aA6f4095F5284301',
  transactionHash: undefined,
  contract: Contract {
    setProvider: [Function (anonymous)],
    currentProvider: [Getter/Setter],
    _requestManager: RequestManager {
      provider: [HttpProvider],
      providers: [Object],
      subscriptions: Map(0) {}
    },
    givenProvider: null,
    providers: {
      WebsocketProvider: [Function: WebsocketProvider],
      HttpProvider: [Function: HttpProvider],
      IpcProvider: [Function: IpcProvider]
    },
    _provider: HttpProvider {
      withCredentials: undefined,
      timeout: 0,
      headers: undefined,
      agent: undefined,
      connected: false,
      host: 'http://127.0.0.1:8545',
      httpAgent: [Agent],
      send: [Function (anonymous)],
      request: [Function: bound modifiedRequest] AsyncFunction,
      _alreadyWrapped: true
    },
    setRequestManager: [Function (anonymous)],
    BatchRequest: [Function: bound Batch],
    extend: [Function: ex] {
      formatters: [Object],
      utils: [Object],
      Method: [Function: Method]
    },
    clearSubscriptions: [Function (anonymous)],
    options: { address: [Getter/Setter], jsonInterface: [Getter/Setter] },
    handleRevert: [Getter/Setter],
    defaultCommon: [Getter/Setter],
    defaultHardfork: [Getter/Setter],
    defaultChain: [Getter/Setter],
    transactionPollingTimeout: [Getter/Setter],
    transactionPollingInterval: [Getter/Setter],
    transactionConfirmationBlocks: [Getter/Setter],
    transactionBlockTimeout: [Getter/Setter],
    blockHeaderTimeout: [Getter/Setter],
    defaultAccount: [Getter/Setter],
    defaultBlock: [Getter/Setter],
    methods: {
      requestApproval: [Function: bound _createTxObject],
      '0xe31c75c3': [Function: bound _createTxObject],
      'requestApproval(address[])': [Function: bound _createTxObject],
      approveRequest: [Function: bound _createTxObject],
      '0x061dff9a': [Function: bound _createTxObject],
      'approveRequest(address)': [Function: bound _createTxObject]
    },
    events: {
      ApprovalReceived: [Function: bound ],
      '0x135b662e7c460f01a8962dabbc952859694282ca1f1bfbacf24ebecc00160d35': [Function: bound ],
      'ApprovalReceived(address)': [Function: bound ],
      RequestApproval: [Function: bound ],
      '0x57eebaf6a4a7bdcd3e1a60dd32681c63d968f8935f596ee7a4523e5fa6c36db6': [Function: bound ],
      'RequestApproval(address,address[])': [Function: bound ],
      allEvents: [Function: bound ]
    },
    _address: '0x97717A1fd7403a0fA71a3aA6aA6f4095F5284301',
    _jsonInterface: [ [Object], [Object], [Object], [Object] ]
  },
  ApprovalReceived: [Function (anonymous)],
  RequestApproval: [Function (anonymous)],
  requestApproval: [Function (anonymous)] {
    call: [Function (anonymous)],
    sendTransaction: [Function (anonymous)],
    estimateGas: [Function (anonymous)],
    request: [Function (anonymous)]
  },
  approveRequest: [Function (anonymous)] {
    call: [Function (anonymous)],
    sendTransaction: [Function (anonymous)],
    estimateGas: [Function (anonymous)],
    request: [Function (anonymous)]
  },
  sendTransaction: [Function (anonymous)],
  estimateGas: [Function (anonymous)],
  call: [Function (anonymous)],
  send: [Function (anonymous)],
  allEvents: [Function (anonymous)],
  getPastEvents: [Function (anonymous)]
}


###################### private key <---> hex <-----> account and addresses ############################
Convert private key to to-string, then hex, then only we can re-derive an account-like address from this hex value.
We CAN NOT get the account value directly from the private key generated using ECDSA signer. 

exam-blockchains python
Python 3.11.4 (main, Jun 20 2023, 16:59:59) [Clang 14.0.3 (clang-1403.0.22.14.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import ecdsa
>>> private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
>>> private_key_hex = private_key.to_string().hex()
>>> print("Private Key:", private_key)
Private Key: <ecdsa.keys.SigningKey object at 0x10f7badd0>
>>> print("Private Key:", private_key_hex)
Private Key: 9c32953314587fca4600f272c143b575071f91ef633829b2cc974d65b82b080e
>>> print("Private Key:", private_key.to_string())
Private Key: b'\x9c2\x953\x14X\x7f\xcaF\x00\xf2r\xc1C\xb5u\x07\x1f\x91\xefc8)\xb2\xcc\x97Me\xb8+\x08\x0e'
>>> private_key_hex = private_key.hex()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'SigningKey' object has no attribute 'hex'
>>> private_key_hex = private_key.hex().to_string()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'SigningKey' object has no attribute 'hex'
>>> private_key_hex = private_key.to_string().hex()
>>> print("Private Key:", private_key_hex)
Private Key: 9c32953314587fca4600f272c143b575071f91ef633829b2cc974d65b82b080e
>>> private_key= bytes.fromhex(private_key_hex)
>>> import web3
>>> from eth_account import Account
>>> account=Account.from_key(private_key)
>>> print(account.address)
0xdCC5EA41244d99FF25615a1a28A519AF44dB2F3E
>>> add1="0x89E165FC0F1A78366F68bCf917f20E219296D0Df"
>>> print(add1)
0x89E165FC0F1A78366F68bCf917f20E219296D0Df
>>> print(account.address)
0xdCC5EA41244d99FF25615a1a28A519AF44dB2F3E


#####################################################################

from web3 import Web3

# Assuming you have an active Ethereum node URL
ethereum_node_url = 'http://localhost:8545'  # Update this with your Ethereum node URL
web3 = Web3(Web3.HTTPProvider(ethereum_node_url))

@api_view(['POST'])
def apply_for_exam(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        # ... your existing code ...

        # Assuming you have a valid private key in private_key_hex
        private_key = ecdsa.SigningKey.from_string(bytes.fromhex(private_key_hex), curve=ecdsa.SECP256k1)

        # ... your existing code ...

        # Call the smart contract function
        contract_abi = [...]  # Load your contract ABI
        contract_address = '0x89E165FC0F1A78366F68bCf917f20E219296D0Df'  # Your contract address

        contract = web3.eth.contract(address=contract_address, abi=contract_abi)

        # Iterate through the teachers' addresses
        successful_transactions = []
        failed_transactions = []

        for teacher_address in teachers:
            # Send the transaction for each teacher
            transaction = contract.functions.requestApproval([teacher_address]).transact({
                'from': sender_address,  # The sender's Ethereum address
                'gas': 2000000,  # Adjust the gas value as needed
                'gasPrice': web3.toWei('50', 'gwei')  # Adjust the gas price as needed
            })

            # Wait for the transaction to be mined
            transaction_receipt = web3.eth.waitForTransactionReceipt(transaction)

            if transaction_receipt['status'] == 1:
                successful_transactions.append(teacher_address)
            else:
                failed_transactions.append(teacher_address)

        if failed_transactions:
            return Response({'message': 'Some transactions failed', 'failed_transactions': failed_transactions}, status=500)

        # All transactions successful
        # ... your existing code ...

        # Return the response
        return Response({'message': 'Application for exam submitted and transactions successful', 'successful_transactions': successful_transactions})
    else:
        # Return validation error response
        return Response(serializer.errors, status=400)create the swagger documentation
