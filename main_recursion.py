
#recurssion method
sum=0


num_n=int(input("Please enter the value of n:"))

def sum_1(num_n):
    if num_n==0 or num_n==1:
        return num_n
    elif num_n>1:
        return sum_1(num_n-1)+num_n

print("The sum1 is", sum_1(num_n))

while(num_n>0):
    sum+=num_n
    num_n-=1

print("The sum is", sum,".")

