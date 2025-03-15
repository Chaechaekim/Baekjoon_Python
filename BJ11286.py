import heapq
q=[]
N=int(input())
p_num=0

for _ in range(N):
    num=int(input())
    if num==0:
        if len(q)==0:
            print(num)
        else:
            print(heapq.heappop(q)[1])
    elif num<0:
        p_num=num*(-1)-0.1
        heapq.heappush(q,(p_num,num))
    else:
        p_num=num*(1.0)
        heapq.heappush(q,(p_num,num))
"""
from queue import PriorityQueue
q=PriorityQueue()
N=int(input())
p_num=0

for _ in range(N):
    num=int(input())
    if num==0:
        if q.empty():
            print(num)
        else:
            print(q.get()[1])
    elif num<0:
        p_num=num*(-1)-0.1
        q.put((p_num,num))
    else:
        p_num=num*(1.0)
        q.put((p_num,num))
"""


"""
from queue import PriorityQueue
q=PriorityQueue()
N=int(input())
ans_list=[0]*N
p_num=0
count=0
#n=N-0.1
#print(n)

for i in range(N):
   num=int(input())
   if num==0:
      if q.qsize()==0:
         ans_list[count]=0
         #print('if',i,ans_list)
         count+=1
      else:
         ans_list[count]=q.get()[1]
         #print('else',i,ans_list)
         #print(q)
         count+=1
   elif num<0:
      p_num=num*(-1)-0.1
      q.put((p_num,num))
      #print('q:',q)
   else:
      q.put((num,num))
      #print('q:',q)

for j in range(count):
   print(ans_list[j])
"""