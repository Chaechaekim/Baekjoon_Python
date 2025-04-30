import sys
input=sys.stdin.readline
N=input().rstrip()
N=int(N)
t=0
S,M,L,XL,XXL,XXXL=map(int,input().rstrip().split())
T,P=map(int,input().rstrip().split())
if S!=0:
    if S%T!=0:
        t+=(S//T)+1
    else:
        t+=S//T
if M!=0:
    if M%T!=0:
        t+=(M//T)+1
    else:
        t+=M//T
if L!=0:
    if L%T!=0:
        t+=(L//T)+1
    else:
        t+=L//T
if XL!=0:
    if XL%T!=0:
        t+=(XL//T)+1
    else:
        t+=XL//T
if XXL!=0:
    if XXL%T!=0:
        t+=(XXL//T)+1
    else:
        t+=XXL//T
if XXXL!=0:
    if XXXL%T!=0:
        t+=(XXXL//T)+1
    else:
        t+=XXXL//T
pd=N//P
pr=N%P
print(t)
print(pd,pr)