# Build in function :- print , len , type, range

# def sum(a,b):
#   sum=a+b
#   return sum

# sum1=sum(12,34)

# print(sum1)

# city=['a','b','c','d','e']

# def length(city):
#     cLenght=len(city)
#     return cLenght

# i = length(city=city)

# print(i)

# city=['r','s','g','a',]

# def city_le(list):
#     for i in list:
#         print(i,end=" ")

# a=city_le(city)
# print(a)

# def fact(num):
#     count = 1
#     for i in range(1,num+1):
#        count*=i
#     return count

# a=fact(100)

# print(a)

#convert 

def convJap(inr):
    conversion_rate = 1.86
    jpy = inr * conversion_rate
    print(f"{inr} INR is equivalent to {jpy} JPY")

# Example usage
convJap(100)