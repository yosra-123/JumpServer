from datetime import datetime
from time import time
import uuid
from .split_text import split
from .WordList import get_word
from .PhraseList import get_phrase
from .ServicesList import get_service
# from .Random import updateWeb
def verifyU(Username,Service,Name):
    data=open("/opt/jumpserver/apps/users/users.txt","r")
    file = data.read()
   # print(file.split()[0])
  # Username = input("Enter your username :")
    split()
    c= get_service(Service)
    a= get_word() 
    b= get_phrase()
    pwd1 = b[1]+c[1]+a[1]+c[2]+"v1"            
    modified_pwd = pwd1.replace("v1", 'v{}'.format(1) )
    id=uuid.uuid4()
    f = open("/opt/jumpserver/apps/users/users.txt", "a")
    f.write(str(id)+","+Name+","+Username+","+str((datetime.timestamp(datetime.now())))+","+modified_pwd+"\n")
    f.close()
    # updateWeb()
    return modified_pwd

#print(verifyU("a","Gmail",'b'))