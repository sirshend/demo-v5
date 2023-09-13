We have few main targets:
1. refactor the code .. the smart contract should simplify the code with enums and a full student profile struct(and corresponding exam mappings) instead of too many separate exam based structs 
2. perhaps make each exam a separate contract??
3. incorporate erc tokens
4. More APIs for the admin, professor profile differentiation based on guides v/s non-guide, revocation, X/F grades, non-consent to applications need to clear the structs and corresponding backend state variables 
5. Sync the stet variables (enums on blockchain vs state variables on backend)
6. make some mock-up of the frontend
7. Publish Sir's email, my code demo, and swagger-ise the existing APIs
8. Conevrt everything to javascript
9. Add the fancy bells and whistles-- redis events, caching, separate microservices for each, optimisations, testings, loggings and other services/middleware 
10. Estimate the gas fees-- experiment with this.. try polygon, ethereum, testnets and also what about deploying on our own blockchain ??
11. Deploy on remote servers.. db, backend, smart contracts etc

In each of shells, first do
cd .. (go to the previous level ```exam_blockchains``` for activating the virtual env)
source v1/bin/activate
cd exam_approval_backend
Once all work is done, deactivate the virtual-env with ```deactivate```

MySQL and mongod, mongosh are immaterial now. 
I have removed any mysql dependency. 
And mongo is running remotely. So no headaches about these stuffs anymore. Nice!!
