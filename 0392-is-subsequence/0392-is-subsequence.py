class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        i,j=0,0


        while i<len(s) and j<len(t): ### two pointer approach      tc o(s+t)        sc o(1)


            if s[i]==t[j]:

                i+=1
                j+=1

            else:

                j+=1

        if i==len(s):         ### if i out of bound that means we found all characters of s in t
            return True

        else:                ### if j out of bound that means for particular i we didnt find the j return False
            return False                














        # arr=[]                ### wrong  code


        # for  i in range(len(s)):

        #     for j in range(len(t)):


        #         if s[i]==t[j] and j not in arr:

        #             arr.append(j)
        #             break

        # print(arr)            

        # if sorted(arr)==arr and len(arr)==len(s):
        #     return True



        # return False                
