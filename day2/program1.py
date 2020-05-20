def odd_even():
    if n&1==0:
        return print("Even")
    return print("Odd")

def prime():
    c=0
    for i in range(2,n+1):
        if n%i==0:
            c+=1
    if c==1:
        print("prime")
    else:
        print("not prime")
        
def palindrome():
    n1=str(n)[::-1]
    if int(n1)==n:
        print('palindrome')
    else:
        print("not palindrome")
        
def armstrong():
    l=str(n)
    t=n
    sum=0
    while(t!=0):
        sum+=(t%10)**len(l)
        t=t//10
    if sum==n:
        print("armstrong")

    else:
        print("not armstrong")
        

n=int(input())
def main():
    odd_even()
    prime()
    palindrome()
    armstrong()
main()
