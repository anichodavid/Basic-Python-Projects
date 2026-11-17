def balanced(text):   #Make a function called balanced that takes some text.


    maps = {")":"(", "]":"[", "}":"{"} #if I see ), I should expect (. Same for ] and }


    stack = [] #Start with an empty stack. This is where we stack up opening brackets.

    for char in text:


        if char in "([{": #If the character is an opening bracket


            stack.append(char) #put it on top of the stack


        elif char in ")]}": #Otherwise if it is a closing bracket...


            if not stack: #if stack is empty
                return False

            
            if stack.pop() != maps[char]: #Take the top plate off. Does it match what I expected for this closer? If not…


                return False

            

    return len(stack) == 0 #After checking everything: if the pile is empty, it's balanced (True). If anything is left over, it's not (False)


print(balanced(")"))           
print(balanced("(()"))         
print(balanced("no brackets here")) 
print(balanced("a(b)c[d]e{f}"))   
print(balanced("{ [ ( ) ] }"))    
print(balanced("{[}]"))              
print(balanced("]"))                 
print(balanced("({[)})"))          
print(balanced("([{"))                
print(balanced(")]}"))                





   