# # Function 

# def hello_world():
#     print("Hello world!")
    
# hello_world()

# def sum(num1 , num2):
#     if(type(num1) is not int or type(num2) is not int):
#         return 
#     return num1 + num2

# total = sum( "vicky" , 10)
# print(total)


# def multiple_items(*args):
#     print(args)
#     print(type(args))
    
# multiple_items('dave','vicky', 'vijay ') 


# def add(*num):
#     sum = 0
#     for n in num :
#         sum += n
#     print("SUM:" , sum) 
# add(5,2)    

def func(a , b, *args , option = False, **Kwargs):
    print("")
    print(a, b)
    print(args)
    print(option)
    print(Kwargs)
    
func(1 , 3 ,10 , 20 , Name = "Tom", Salary = 60000)     