
fac_1=1

num_n=int(input("Please enter a positive value:"))
n=num_n
for i in range(1, num_n+1):
    fac_1=fac_1*i

fact_1=1

while (num_n>0):
    fact_1*=num_n
    num_n-=1
print("The factorial of", n,"! is", fac_1, fact_1,".")