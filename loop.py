# a=input("Enter a word : ")
# b=int(input("which table you want to print:" ))

# count=1
# while (count<=b):
#     print(a)
#     count+=1
# count=1
# while (count<=10):
#     print(f"{b} x {count} = {b * count}")
#     count+=1

# n=[1,4,9,16,25,36,49,64,81,100]
# snum=9;
# count=0
# while (count < len(n)):
#     if(n[count]==snum):
#         print("Found in list", count)
#     count += 1

# i = 1
# while i <= 10:
#     if (i == 6):
#         break
#     print(i)
#     i += 1



listt=[1,4,9,16,25,36,49,64,81,100]
ind=0
for el in listt:
    if(el==4):
        print("elment found" , el, "and index is ", ind)
        break
    print(el)
    ind+=1

