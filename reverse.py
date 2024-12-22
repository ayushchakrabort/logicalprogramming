num=int(input("n: "))
rev=0
while num:
    rem = num %10
    rev= rev * 10 +rem
    num//=10
print('reversed number: ',rev)