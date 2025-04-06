import os
try:
    with open('text.txt','r')as file:
        data=file.read()
    with open('text1.text','w') as filewrite: 
           filewrite.write(data)
           print("File copied successfully")
           
except FileNotFoundError:
    print("Input or Output operation file")
except IOError as e:
    print(f"I/O Exception:(e)")
except Exception as e:
    print("An Unexpected error")     
       