
data = { 
        1001: { 'username':'ram','password':'123redhat','bal':50000,'email':'ram@gmail.com','ph_no':1234567890,'addr':'jaipur'},
        1002: { 'username':'shyam','password':'redhat123','bal':51500,'email':'shyam@gmail.com','ph_no':123453490,'addr':'kota'},
        1003: { 'username':'hari','password':'Asimov','bal':12435,'email':'hari@gmail.com','ph_no':1223567230,'addr':'ajmer'},    
     }

import pickle
#import json
f = open('bank.db','wb')

#json.dump(data,f)
pickle.dump(data,f)

f.close()
