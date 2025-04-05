def fun1(msg): #outer function
    def fun2(): #inner function 
        print(msg)
    fun2()
fun1("Hello")