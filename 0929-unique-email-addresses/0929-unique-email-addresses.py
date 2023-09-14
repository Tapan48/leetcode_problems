class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        
        unique=set()
        
        for email in emails:
            
            local,domain=email.split("@")
            local=local.split("+")[0]
            local=local.replace(".","")
            
            unique.add((local,domain))
        return len(unique)     
            
        
        
#         for i,email in enumerate(emails):
            
            
            
#             local,domain=email.split("@")
            
#             if "+"in local:
            
#                  index=local.find("+")
#                  useful= email[:index]
            
#                  useful2=useful.replace(".","")
            
                 
                
#             else:
#                 useful2=local.replace(".","")
                
#             newemail=useful2+"@"+domain
            
#             emails[i]=newemail
            
#         x=set(emails)
#         return len(x)
        
            
             
            
#             In summary, the time complexity is O(n * m), and the space complexity is O(n), where n is the number of email addresses and m is the average length of an email address
           
                
            
            
                
                
                
        