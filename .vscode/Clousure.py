 # Closure is a function having access to the scope of its parent function after the parent function has returned 


def parent_function(name):
    coins= 3
    
    def player():
        nonlocal coins
        coins += 1
        print(coins)
        
        if coins > 1 :
            print('\n' + name + ' has '  + str(coins) +" coins left")
        elif coins == 1:
            print('\n' + name + ' has' + str(coins) +" coins left")
        else:
            print("\n" + name +  "has" +  "Out of coins")
                    
    return player                
         
       
tommy = parent_function("vicky")        
tommy()
tommy()
tommy()
tommy()