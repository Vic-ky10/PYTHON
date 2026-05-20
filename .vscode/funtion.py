# # # Function 

# # def hello_world():
# #     print("Hello world!")
    
# # hello_world()

# # def sum(num1 , num2):
# #     if(type(num1) is not int or type(num2) is not int):
# #         return 
# #     return num1 + num2

# # total = sum( "vicky" , 10)
# # print(total)


# # def multiple_items(*args):
# #     print(args)
# #     print(type(args))
    
# # multiple_items('dave','vicky', 'vijay ') 


# # def add(*num):
# #     sum = 0
# #     for n in num :
# #         sum += n
# #     print("SUM:" , sum) 
# # add(5,2)    

# def func(a , b, *args , option = False, **Kwargs):
#     print("")
#     print(a, b)
#     print(args)
#     print(option)
#     print(Kwargs)
    
# func(1 , 3 ,10 , 20 , Name = "Tom", Salary = 60000)       


# #Recursion

# def add_one(num):
    
#     if(num >= 9):
#         return num + 1 
#     total = num +1 
#     print(total)
    
#     return add_one(total)

# mynewtotal = add_one(0)
# print(mynewtotal)       



# def recursive_factorial(n):
#     if n ==1 :
#         return n
#     else:
#         return n* recursive_factorial(n-1)
    
    
name = "vigneshwaran"
age = 22
    
def another():
    age = 21
    def greeting(name):
        print(age)
        print(name)
        greeting("vikcy")
        
another()        
    
        