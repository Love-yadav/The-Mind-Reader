#this is the simple magic 
#which show you what number you choose in your mind so lets get started
import getpass,random,time
print("************choose two same number in between (0,100) and i will read your mind and tell you final answer*********************************")

user1=int(getpass.getpass(prompt=" user1=enter a first ✌✌✌ number:This is hidden so i can not cheat :it is only in your mind  : "))
user2=int(getpass.getpass(prompt="user2=enter a same number as user1:"))

print("\n")
print("************************you have 10 seconds for solving every steps***************************")
print("you can only give integers,floats")

a=time.sleep(10)
print(a)
print("\n")
print("STEP:1")
print("now add the value of the user1 input and user2 input in your mind:")
print("************************************************************************")
sum=user1+user2


time.sleep(10)
print("\n")
print("STEP:2")
print("now add this number in your total which is in your mind")
randomnumber=random.randint(1,100)
print(f"add this:{randomnumber}")
print("***********************************************************************************")
add=sum+randomnumber

time.sleep(10)
print("\n")
print("step:3")
print("give back the number to your friend which number is selected by you for your friend")
print("*******************************************************************************************")
add1=add-user2

time.sleep(10)
print("\n")
print("STEP:4")
print("now  give the half to the god wich is in your mind")
print("**********************************************************************************")
add2=add1-(add1/2)
print("\n")

print("***************wait i am 😊✌✌✌✌reading your mind look into my eye*******************")
print("\n")
time.sleep(30)
print(f"**************************now your final 😁😁answer is: {add2}******************************")

print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print("++++++++++++++++++++++++++Thanks for Playing+++++++++++++++++++++++++++++++++++++++++++++")
print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")






