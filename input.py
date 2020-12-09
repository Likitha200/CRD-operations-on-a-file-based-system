#demonstration on how to access and perform operations on a main file

#import mainfile as a library 

import sourcecode as z
#importing the main file("sourcecode" is the name of the file) as a library 

z.create("car",20)
#to create a key with key_name,value given and with no time-to-live property

z.create("src",60,120) 
#to create a key with key_name,value given and with time-to-live property value given(number of seconds)

z.read("car")
#it returns the value of the respective key in Jasonobject format 'key_name:value'

z.read("src")
#it returns the value of the respective key in Jasonobject format if the TIME-TO-LIVE IS NOT EXPIRED else it returns an ERROR

z.create("car",40)
#it returns an ERROR since the key_name already exists in the database

z.delete("car")
#it deletes the respective key and its value from the datastore

z.read("src")
#it gives error since the TIME-TO-LIVE has expired

z.delete("car")
#it gives "key doesnot exist" error as key is deleted earlier

#we can access these using multiple threads-it helps in doing multiple operations simultaneously.
t1=Thread(target=create,args=(key_name,value,timeout)) #as per the operation one can give target create or read or delete
t1.start()
t1.sleep()
t2=Thread(target=read,args=(key_name)) #as per the operation one can give target create or read or delete
t2.start()
t2.sleep()
t3=Thread(target=delete,args=(key_name)) #as per the operation one can give target create or read or delete
t3.start()
t3.sleep()
#and so on upto tn

#the code also returns other errors such as 
#"invalidkey" if key_length is greater than 32 or key_name contains any numeric,special characters etc.,
#"key doesnot exist" if key_name was mis-spelt or deleted earlier
#"File memory limit reached" if file memory exceeds 1GB
