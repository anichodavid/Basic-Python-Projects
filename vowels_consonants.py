def count_letters(text):
    vowel = 0
    consonant = 0
    for char in text.strip().lower():
        if char in "aeiou":
            vowel += 1
        elif char in "bcdfghjklmnpqrstvwxyz":
            consonant  += 1
    return vowel, consonant

print(count_letters("Hello, World123"))
print(count_letters("AEIOU"))
print(count_letters(""))
print(count_letters("rhythm"))

        
        
       

    
   
       
        
            
