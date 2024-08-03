# task 1
s=(input("enter letters "))
dict={}    
for i in s:  
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)
l1=list(dict.values())
l2=list(dict.keys())
print(l1)
print(l2)
if l1.count(l1[0])==len(l1):
    print(0) 
else:
    print(min(l1)) 


# task2 
n=int(input("how many rounds "))
l3=[]
for i in range(n):
    r=tuple(eval(input("enter player number,score")))
    l3.append(r)
print(l3) 
for i in range(len(l3)):   
    
    print(l3[i][0],end=" ")

# task 4
dict={

}
option=input("remove,add,view all,search")
name=input("enter your name ")
phone=float(input("enter your phone number"))
def add(name,phone):
        dict["name"]=name
        dict["phone"]=phone
print(dict)
add(name,phone)
def remove(name,phone):
    if option=="remove":
        re=input("what to remove ")  

        if re == name:
            del dict["name"]
            del dict["phone"]
            print("removed succesfly")
        else:
            print("not found")
print(dict)
remove(name,phone)        
def view(name,phone):
    if option=="view":
        print(dict)
view(name,phone) 
def search(name):
    if option=="search":
        se=input("enter name to search by")
        if se==name:    
            print(f"phone number of this name:{dict["phone"]}")
search(name)           


#task 3
l5=set(eval(input("enter list")))
print(l5)