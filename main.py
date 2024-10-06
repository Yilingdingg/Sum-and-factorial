

sum=0


num_n=int(input("Please enter the value of n:"))

if num_n<=0:
    num_n=int(input("Your value is negative, please neter a positive number:"))

while(num_n>0):
    sum+=num_n
    num_n-=1

print("The sum is", sum,".")

