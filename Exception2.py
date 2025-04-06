def checkage(age):
    if age<18:
        raise ValueError("Age must be 18")
    else:
        print("You are Eligible")
    
try:
    checkage(16) 
except ValueError as e:
        print(f"Error")  
        
        
class NotEligible(Exception):
    pass
def checkage(age):
        if age<18:
            raise NotEligible("Age must be 18")
        else:
            print("You are eligible")
try:
    checkage(16)
except NotEligible as e:
    print("Error")
                             