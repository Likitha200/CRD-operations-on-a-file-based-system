import threading 
from threading import*
import time
import json

with open('C:/Users/BJ Reddy/Documents/data.txt')as f:
     dic=json.load(f) #loading jason object
     f.close()
with open('C:/Users/BJ Reddy/Documents/data.txt','w')as fi:
     json.dump(dic,fi) #writes dic object to fi 
     fi.close()
    
#create operation-It has three parameters,key,value,timeout where the timeout is optional.

def create(key,val,timeout=0):
    if key in dic:
        print("error: this key already exists") #error message1
    else:
        if(key.isalpha()): #checks if key_name has alphabets or not.
            if len(dic)<(1024*1024*1024) and val<=(16*1024): #condition for file size less than 1GB and Jasonobject value less than 16KB 
                if timeout==0:
                    k=[val,timeout]
                else:
                    k=[val,time.time()+timeout]#time.time() method gets the current time.
                if len(key)<=32: #condition for input key_name capped at 32chars
                    dic[key]=k
            else:
                print("error: Memory limit exceeded!")#error message2
        else:
            print("error: Invalid key_name!")#error message3

#read operation-It has one parameter, key_name.
            
def read(key):
    if key not in dic:
        print("error: given key does not exist in database. Please enter a valid key") #error message4
    else:
        s=dic[key]
        if s[1]!=0:     #if timeout is given and is not equal to 0.
            if time.time()<s[1]: #comparing the present time with expiry time
                str1=key+":"+str(s[0]) #It returns the value in the format of JasonObject i.e.,"keyname:value"
                return str1
            else:
                print("error: time-to-live of",key,"has expired") #error message5
        else:          #if timeout is not given. 
            str1=key+":"+str(s[0])
            return str1

#delete operation-It has one parameter, keyname.

def delete(key):
    if key not in dic: #checks if key is present in dictionary or not.
        print("error: given key does not exist in database. Please enter a valid key") #error message6
    else:
        l=dic[key]
        if l[1]!=0:
            if time.time()<l[1]: #comparing the current time with expiry time
                del dic[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") #error message7
        else:
            del dic[key]
            print("key is successfully deleted")
