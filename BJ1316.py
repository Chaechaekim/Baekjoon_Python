import re
num = int(input())
word_list=[]
group_num = 0
alpha={}

sort_alpha={}

correct=num
n=0

for i in range(num):
    word_list.append(input())
    alpha.clear()
    sort_alpha.clear()
    same_alpha =1
    same_sort_alpha=1
   # print(alpha)
   # print(sort_alpha)
    if(len(word_list[i])==2):
        if(word_list[i][0]!=word_list[i][1]):
            correct+=0
            #print(correct)
    elif(len(word_list[i])!=1):
        sort_word = ''.join(sorted(word_list[i]))
       # print(sort_word)
        for j in range(len(word_list[i])-1) :
            
             if(word_list[i][j]==word_list[i][j+1]):
                 same_alpha+=1
                 alpha[word_list[i][j]]=same_alpha
             elif(word_list[i][j]!=word_list[i][j+1]):
                 if(same_alpha!=0):
                    #same_alpha+=1
                   # alpha[word_list[i][j]]=same_alpha
                    same_alpha = 1
                  
             if(sort_word[j]==sort_word[j+1]):
                    same_sort_alpha+=1
                    sort_alpha[sort_word[j]]=same_sort_alpha
                   # print('same_sort_alpha:'+str(same_sort_alpha))
             else:
                if(same_sort_alpha!=0 ):
                     #same_sort_alpha+=1
                     #sort_alpha[sort_word[j]]=same_sort_alpha
                     same_sort_alpha=1
                   
        
       # print(alpha)
       # print(sort_alpha)

        if(alpha!=sort_alpha):
            correct-=1
          #  print(i)
           # print(correct)

    


    #if(word_list[i]==sort_word):
 #       group_num += 1
#



print(correct)
#print(word_list)
#print(group_num)