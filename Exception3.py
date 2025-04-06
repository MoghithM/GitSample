import os
if os.path.exists("text.txt"):
  with open('text.txt','r')as file:
    content=file.read()
    print(content)
else:
    print("File does not exist!")