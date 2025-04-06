try:
    num=int(Input("Enter a number"))
    result=10/num
except ValueError as e:
    print(f"Invalid input: {e}")
except ZeroDivisionError as e:
    print("Cannot divided by zero")
except Exception as e:
    print("An unexpected")
else:
    print(f"Result:{result}")
finally:
    print("Code executed successfully") 
    
                       