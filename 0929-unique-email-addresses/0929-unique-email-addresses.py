class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        
        for i,email in enumerate(emails):
            
            
            
            local,domain=email.split("@")
            
            if "+"in local:
            
                 index=local.find("+")
                 useful= email[:index]
            
                 useful2=useful.replace(".","")
            
                 
                
            else:
                useful2=local.replace(".","")
                
            newemail=useful2+"@"+domain
            
            emails[i]=newemail
            
        x=set(emails)
        return len(x)
        
            
             
            
            
           
                
            
            
                
                
                
        