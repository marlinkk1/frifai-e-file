n=int(input("digite um numero:"))
if (n>1):
    for i in range(2,n):
     if(n%i==0):
        print("nao e numero primo")
        break
    else:
        print("numero primo")
else:
    print("nao e numero primo")