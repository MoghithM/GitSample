import re
x="The rain in spain"
y=re.search("^The.*spain$",x)
if y:
    print("yes the match is correct")
else:
    print("Not matching with the pattern")    
    