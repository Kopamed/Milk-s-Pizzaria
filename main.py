total = 0 #start Price
print("Welcome to Milknee's Pizzaria!")


while True:
  
    size = input("What size do you want your pizza to be? Your options are: Small, Medium, Large.")
    
    if size.lower() == "small":
        total += 3.5
        break

    elif size.lower() == "medium" :
        total += 5.0
        break

    elif size.lower() == "large" :
        total += 7.0
        break

    else :
        print ("You gotta pick a size. What do you want a metaphysical pizza?")

while True:
  
    

    size = input("""What crust do you want?
1. Small
2. Medium
3. Large.""")


    if size == "1":
        total += 3.5
        break

    elif size == "2" :
        total += 5.0
        break

    elif size == "3" :
        total += 7.0
        break

    else :
        print ("You gotta pick a size. What do you wnat a metaphysical pizza?")


'''
We can type here and python will ignore this, k?
and also, check the repl.it chat

why you do that?
larg

its easier to choos

'''
        
    
