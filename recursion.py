# def show(num):
#     if(num==0):
#         return
#     print(num)
#     show(num-1)
    
# show(5)


# def fact(num):
#     if(num==0 or num ==1):
#         return 1
#     else:
#         return num * fact(num-1)
    
# a=fact(4)
# print(a)

# def nat_sum(num):
#     if(num==0):
#         return 0
#     return nat_sum(num-1) + num
    
# a=nat_sum(3)

# print(a)

def list_fun(list,ind):
    if(ind==len(list)):
        return
    print(list_fun(list, ind+1))
    
list1=["apple","mango","banana","cherry"]

list_fun(list1,0)