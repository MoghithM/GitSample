import re
x="The rain in spain"
y=re.search("^The.*spain$",x)
if y:
    print("yes the match is correct")
else:
    print("Not matching with the pattern") 
    
x="The rain in spain"
y=re.findall("ai",x)
print(y)

z=re.search("\s",x)
z=re.split("\s",x)  #splitted with the white space
print(z) 

re.sub("\s","$",x) #replce all white space with $  

#Pattern matches one or more digits
pattern=r"\d+"
text="There are 123 apples"
match=re.search(pattern,text)
if match:
    print("Match found:",match.group())  
    

pattern=r"(\d+)-(\d+)-(\d+)"
text="The event is on 2025-03-26"
match=re.search(pattern,text)
if match:
    print("Year:",match.group(1))
    print("Month-Day:",match.group(2))  
    print("Month-Day:",match.group(3))  
    