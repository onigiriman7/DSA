def merge(intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        for i in range(len(intervals)-1):
            print(i)
            if intervals[i][1] >= intervals[i+1][0]:
                ans.append([intervals[i][0],intervals[i+1][1]])
                #print(i)
                i += 2
                #print(i)
            else:
                ans.append(intervals[i])
        return ans

#merge([[1,2],[5,6],[7,10],[8,18],[19,20]])


def dup(text):
    #return array with counts
    countArr = [0 for x in range(ord("z"))]
    counts = []
    for i in text:
        countArr[ord(i)] += 1
    for i in text:
        if (i, countArr[ord(i)]) not in counts:
            counts.append((i, countArr[ord(i)]))
    return counts
#print(dup("hekko"))


def rot(text, rotText):
    #return true or false
    com = text+text
    if com.find(rotText) !=  -1:
        return True
    return False

#print(rot("ABCD", "BADC"))

def Le(s):
		# Code here
		 
		m = 0
		for i in range(len(s)-1):
		    
		    if s[i] == s[i+1]:
		       count  =0
		       j = i
		       while s[j] == s[j+1]:
		           count += 1
		           if count>m:
		               m = count
                    
		return m
#print(Le("axxxy"))

def perm(S, start, n, res):
    s = list(S)
    
    if start == n:
        
        res = s
        print("".join(s))
    else:
        for i in range(n-1):
            s[i], s[start] = s[start], s[i]
            perm(s, start+1, n, res)
            s[i] ,s[start] = s[start], s[i]

#perm("ABCD",0,4,[])
# 0000111100110011
def balance(S, n):
    count = 0
    stack = []
    n = len(S)
    print("initial stack" + str(stack))
    top =-1
    for i in range(0,n-1):
        print(stack)
        print("top: "+str(top)+" i: "+str(i))
        



        if top == -1:
            print("stack empty")
            stack.append(S[i])
            top +=1
            print(stack)
            print("top: "+str(top)+" i: "+str(i))
            
        else:
            if stack[top] == "0":
                if S[i] == "0":
                    stack.append(S[i])
                    top +=1
                    continue
                if S[i] == "1" :
                    stack.pop()
                    top-=1
                    print("popped")
                    if len(stack) != 0 and S[i+1] == stack[top]:
                        count += 1
                        print("counted")
                        continue
                    if len(stack) == 0:
                        count+=1
                        print("counted")
                        continue
            if stack[top] == "1":
                if S[i] == "1":
                    stack.append(S[i])
                    top +=1
                    continue
                if S[i] == "0":
                    stack.pop()
                    top-=1
                    if len(stack) != 0 and S[i+1] == stack[top]:
                        count += 1
                        print("counted")
                        continue
                    if len(stack) == 0:
                        count+=1
                        print("counted")
                        continue

        
    return count

#print("answer: "+ str(balance("0111100010",16)))




# 1111000010101111
# i = 4 stack =[0000]


def maxSubStr(S, n):
    n = len(S)
    # To store the count of 0s and 1s
    count0 = 0
    count1 = 0
      
    # To store the count of maximum 
    # substrings str can be divided into
    cnt = 0
      
    for i in range(n):
        if S[i] == '0':
            count0 += 1
        else:
            count1 += 1
              
        if count0 == count1:
            cnt += 1
  
# It is not possible to 
    # split the string
    if count0 != count1:
        return -1
              
    return cnt
  

#print(maxSubStr("01111001111111111010",1))

def solveWordWrap(nums, k):
		#Code here
    sol = []
    i =0
    
    while i < len(nums):
        llength = 0
        
        if nums[i]+1 >= k:
            
            sol.append([i+1,i+1])
        elif nums[i]+1 <k:
            llength += nums[i]+1
            j = i+1
            while llength  <= k and j<len(nums):
                if llength + nums[j] + 1 <=k:
                    llength += nums[j] +1
                else:
                    
                    break
                j += 1
            
            sol.append([i+1,j])
            i = j-1
            # i += 1
        i+=1
    return sol
print(solveWordWrap([7,5,6 ,5 ,6 ,1 ,1 ,10 ,8], 12))