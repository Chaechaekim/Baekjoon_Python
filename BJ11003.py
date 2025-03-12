from collections import deque

N,L=map(int,input().split())
a_list=list(map(int,input().split()))
#a_list=[1000000000]*(L-1)+a_list
aq_list=[0]*N
q = deque()
start_index=0
end_index=L
num=0
ans_list=[0]*N
k=0
for j in range(N):
        aq_list[j]=[j,a_list[j]]
        
#print(aq_list)
#print(aq_list[1][1])
ans_list[0]=a_list[0]
q.append(aq_list[0])
#print(q[0])
for i in range(1,N):
        if  q and q[k][0]<=i-L:
                       #print('lq',i,q.popleft())
                       q.popleft()
                        
                        
        if a_list[i-1]>=a_list[i]:
                while q and q[-1][1]>=a_list[i]:
                    #print('q',i,q.pop())
                    q.pop()
                q.append(aq_list[i])
                #print('+',q)
             
        else:
                q.append(aq_list[i])
                #print('+',q)

        if q:
                ans_list[i]=q[0][1]
                
        
        
        
print(*ans_list)  
"""
from collections import deque
N,L=map(int,input().split())
a_list=list(map(int,input().split()))
q=deque()
for i in range(N):
        while q and q[-1][1]>=a_list[i]:
                q.pop()
        q.append((i,a_list[i]))
        if q[0][0]<= (i-L):
                q.popleft()
        print(q[0][1],end=' ')
"""
"""
from collections import deque

N,L=map(int,input().split())
a_list=list(map(int,input().split()))
#a_list=[1000000000]*(L-1)+a_list
aq_list=[0]*N
q = deque()
start_index=0
end_index=L
num=0
ans_list=[0]*N
k=0
for j in range(N):
        aq_list[j]=[j,a_list[j]]
        
#print(aq_list)
#print(aq_list[1][1])
ans_list[0]=a_list[0]
q.append(aq_list[0])
#print(q[0])
for i in range(1,N):
        if i>=L:
                while q and q[k][0]<=i-L:
                       #print('lq',i,q.popleft())
                       q.popleft()
                        
                        
        if a_list[i-1]>=a_list[i]:
                while q and q[-1][1]>=a_list[i]:
                    #print('q',i,q.pop())
                    q.pop()
                q.append(aq_list[i])
                #print('+',q)
             
        else:
                q.append(aq_list[i])
                #print('+',q)

        if q:
                ans_list[i]=q[0][1]
                
        
        
        
print(*ans_list)  
"""
"""
from collections import deque

N,L=map(int,input().split())
a_list=list(map(int,input().split()))
#a_list=[1000000000]*(L-1)+a_list
aq_list=[0]*N
q = deque()
start_index=0
end_index=L
num=0
ans_list=[0]*N
k=0
for j in range(N):
        aq_list[j]=[j,a_list[j]]
        
#print(aq_list)
#print(aq_list[1][1])
ans_list[0]=a_list[0]
q.append(aq_list[0])
#print(q[0])
for i in range(1,N):
        if i>=L:
                while q and q[k][0]<=i-L:
                       #print('lq',i,q.popleft())
                       q.popleft()
                        
                        
        if a_list[i-1]>=a_list[i]:
                while q and q[-1][1]>=a_list[i]:
                    #print('q',i,q.pop())
                    q.pop()
                q.append(aq_list[i])
                #print('+',q)
             
        else:
                q.append(aq_list[i])
                #print('+',q)

        if q:
                ans_list[i]=q[0][1]
                
        
        
        
print(*ans_list)  
""" 
        
        
               

"""
N,L=map(int,input().split())
a_list=list(map(int,input().split()))
a_list=[1000000000]*(L-1)+a_list
ans_list=[0]*N
for i in range(N):
        ans_list[i]=min(a_list[i:i+L])
print(*ans_list)
"""

"""
N,L=map(int,input().split())
a_list=list(map(int,input().split()))
ans_list=[0]*N
for i in range(N):
    if (i-L+1)<0:
        ans_list[i]=a_list[0]
        #print(a_list[0])
    else:
        ans_list[i]=min(a_list[i-L+1:i+1])
        #print(min(a_list[i-L+1:i+1]))
        #print(a_list[i-L+1:i+1])
print(*ans_list)

"""