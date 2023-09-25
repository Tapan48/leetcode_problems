class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
        cache=collections.defaultdict(int) #### mask(configuration)--->maxscore
        
        
        def dfs(mask,opt):
            
            if mask in cache:
                return cache[mask]
        
        
        
        
        
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):


                    if (1<<i)& mask or (1<<j)&mask:
                        continue

                    score=opt*math.gcd(nums[i],nums[j])
                    newmask=mask|(1<<i)|(1<<j)

                    cache[mask]=max(cache[mask],score+dfs(newmask,opt+1))

            return cache[mask] 
        
        
        return dfs(0,1)        
        
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
        
        
        
        
        
        