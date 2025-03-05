N,M=map(int,input().split(' ')) #N과 M input 받기
n_matrix =[] #N*N 표표
m_matrix=[] #x1,y1,x2,y2 저장
sum_matrix=[]
sum_num=0
ans=0


for _ in range(N):
    n_matrix.append(list(map(int,input().split(' '))))
    
for i in range(N+1):
    sum_matrix.append([])
    for j in range(N+1):
        if j==0 or i==0:
            sum_matrix[i].append(0)
        else:
            sum_num=sum_matrix[i][j-1]+sum_matrix[i-1][j]-sum_matrix[i-1][j-1]+n_matrix[i-1][j-1]
            sum_matrix[i].append(sum_num)
#print(sum_matrix)
            
for i in range(M):
    x1,y1,x2,y2=map(int,input().split(' '))
    ans=sum_matrix[x2][y2]-sum_matrix[x1-1][y2]-sum_matrix[x2][y1-1]+sum_matrix[x1-1][y1-1]
    print(ans)
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [[0] * (n + 1)]
D = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    A_row = [0] + list(map(int, input().split()))
    A.append(A_row)

# 누적 합 배열 생성
for i in range(1, n + 1):
    for j in range(1, n + 1):
        D[i][j] = D[i][j - 1] + D[i - 1][j] - D[i - 1][j - 1] + A[i][j]

# 질의 처리
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]  # 수정된 부분
    print(result)
"""
