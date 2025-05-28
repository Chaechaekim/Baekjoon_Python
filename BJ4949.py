import sys
from collections import deque
input=sys.stdin.readline
stack=deque([])
while True:
        str_list=input().rstrip()
        if str_list=='.':
                break
        else:
            for i in range(len(str_list)):
                   if len(stack)==0 and (str_list[i]=='('or str_list[i]==')' or str_list[i]=='[' or str_list[i]==']'):
                          stack.append(str_list[i])
                   else:
                        if str_list[i]==')' and stack[-1]=='(':
                          stack.pop()
                        elif str_list[i]==']'and stack[-1]=='[':
                          stack.pop()
                        elif str_list[i]=='('or str_list[i]==')' or str_list[i]=='[' or str_list[i]==']':
                          stack.append(str_list[i])
            if len(stack)==0:
                print('yes')
            else:print('no')
            stack.clear()