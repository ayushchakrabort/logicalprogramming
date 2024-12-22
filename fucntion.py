class LOGICAL:
    def add_one_n(self,n):
        sum=0
        for i in range(1,n+1):
            sum+=i
        return sum
    
    def factorial(self,n):
        f=1
        for i in range(1,n+1):
         f*=i
        return f
    
    def factor(self,n):
        for i in range(1,n+1):
            if n%i==0:
                print(i,end=" ")

    def n_factor(self,n,/): 
        c=0
        for i in range(1,n+1):
            if n%i==0:
                c+=1
        return c
    def isprime_no(self,n,/):
        if LOGICAL.n_factor(self,n)==2:
            print(f"{n} is prime")
        else:
            print(f"{n} is not a prime")

    def reverse(self,num):
        num=int(input("n: "))
        rev=0
        while num:
            rem = num %10
            rev= rev * 10 +rem
            num//=10
        print('reversed number: ',rev)

obj=LOGICAL()
# print(obj.add_one_n(5))
# print(obj.factorial(5))
# obj.factor(10)
# print(obj.n_factor(10))
# obj.isprime_no(10)
obj.reverse(123)

