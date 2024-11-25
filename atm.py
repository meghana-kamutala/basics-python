print("*"*20,"ATM MACHINE","*"*20)
amount = int(input("enter the amount: "))
l = [500,200,100,50,20,10,5,2,1]
c = 0
for i in l:
    Notes = amount//i
    c = c+Notes
    print(f"{i}Notes --> {Notes}")
    amount = amount%i
print("minimum number of NotesL: ",c)    